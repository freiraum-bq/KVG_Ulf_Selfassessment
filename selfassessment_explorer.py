# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo",
#     "pandas",
#     "openpyxl",
#     "altair",
# ]
# ///

import marimo

__generated_with = "0.19.9"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import altair as alt

    return alt, mo, pd


@app.cell
def _(mo):
    mo.md("""
    # 📊 Self-Assessment Questionnaire Explorer

    Explore the self-assessment responses from your team project.
    Students answered this questionnaire for **each group** they participated in.

    Use the tabs below to explore different aspects of the data.
    """)
    return


@app.cell
def _(pd):
    # Load data - adjust path as needed
    DATA_URL = "https://github.com/freiraum-bq/KVG_Ulf_Selfassessment/raw/main/answers.xlsx"

    df = pd.read_excel(DATA_URL)

    # Clean column names for easier access
    df.columns = [
        'timestamp', 'email', 'name', 'team',
        'start_date', 'end_date', 'star_response',
        'skills_learned', 'task_division', 'task_process',
        'disagreements', 'group_outcome', 'continue_doing',
        'stop_doing', 'start_doing',
        'score_contribution', 'score_dynamics', 'score_reflection'
    ]

    # Extract numeric scores (1-4) from the text
    def extract_score(text):
        if pd.isna(text):
            return None
        return int(str(text).split(' - ')[0])

    df['contribution_score'] = df['score_contribution'].apply(extract_score)
    df['dynamics_score'] = df['score_dynamics'].apply(extract_score)
    df['reflection_score'] = df['score_reflection'].apply(extract_score)

    # Clean name inconsistencies (e.g., trailing spaces)
    df['name'] = df['name'].str.strip()
    return (df,)


@app.cell
def _(df, mo):
    # Summary stats
    n_responses = len(df)
    n_students = df['name'].nunique()
    n_teams = df['team'].nunique()

    mo.md(
        f"""
        ## 📈 Overview

        | Metric | Value |
        |--------|-------|
        | Total Responses | **{n_responses}** |
        | Unique Students | **{n_students}** |
        | Teams Covered | **{n_teams}** |
        | Avg Responses per Student | **{n_responses/n_students:.1f}** |
        """
    )
    return


@app.cell
def _(mo):
    # Create tabs for navigation
    tabs = mo.ui.tabs({
        "👤 By Student": "student",
        "👥 By Team": "team",
        "📊 Distributions": "distribution",
    })
    tabs
    return (tabs,)


@app.cell
def _(df, mo, tabs):
    mo.stop(tabs.value != "👤 By Student")

    # Student selector
    students = sorted(df['name'].unique())
    student_dropdown = mo.ui.dropdown(
        options={name: name for name in students},
        label="Select a student",
        value=students[0]
    )
    student_dropdown
    return (student_dropdown,)


@app.cell
def _(df, mo, student_dropdown, tabs):
    mo.stop(tabs.value != "👤 By Student")

    selected_student = student_dropdown.value
    student_data = df[df['name'] == selected_student]

    teams_participated = student_data['team'].tolist()

    def _build_student_score_table(data, teams):
        _score_keys = ['contribution_score', 'dynamics_score', 'reflection_score']
        _avg_c = data['contribution_score'].mean()
        _avg_d = data['dynamics_score'].mean()
        _avg_r = data['reflection_score'].mean()

        if len(teams) > 1:
            _header = "| Category | " + " | ".join(teams) + " | Average |"
            _sep = "|----------|" + "|".join(["------" for _ in teams]) + "|---------|"
            _cat_labels = ['Contribution', 'Group Dynamics', 'Reflection']
            _rows = []
            for _cat, _key in zip(_cat_labels, _score_keys):
                _per_group = " | ".join(
                    str(int(r[_key])) if r[_key] is not None else "–"
                    for _, r in data.iterrows()
                )
                _avg = data[_key].mean()
                _rows.append(f"| {_cat} | {_per_group} | **{_avg:.2f}** |")

            _per_group_overall = " | ".join(
                f"{0.5 * r['contribution_score'] + 0.3 * r['dynamics_score'] + 0.2 * r['reflection_score']:.2f}"
                if all(r[k] is not None for k in _score_keys) else "–"
                for _, r in data.iterrows()
            )
            _overall = 0.5 * _avg_c + 0.3 * _avg_d + 0.2 * _avg_r
            _rows.append(f"| **Overall** | {_per_group_overall} | **{_overall:.2f}** |")
            return "\n        ".join([_header, _sep] + _rows)
        else:
            _overall = 0.5 * _avg_c + 0.3 * _avg_d + 0.2 * _avg_r
            return f"""| Category | Score |
        |----------|-------|
        | Contribution | **{_avg_c:.2f}** |
        | Group Dynamics | **{_avg_d:.2f}** |
        | Reflection | **{_avg_r:.2f}** |
        | **Overall** | **{_overall:.2f}** |"""

    mo.md(
        f"""
        ## 👤 {selected_student}

        **Teams participated in ({len(teams_participated)}):**
        {', '.join(teams_participated)}

        ### Self-Assessment Scores (1=Best, 4=Lowest)

        {_build_student_score_table(student_data, teams_participated)}
        """
    )
    return (student_data,)


@app.cell
def _(mo, student_data, tabs):
    mo.stop(tabs.value != "👤 By Student")

    # Group selector for viewing detailed responses
    group_options = ["All groups"] + student_data['team'].tolist()
    student_group_dropdown = mo.ui.dropdown(
        options=group_options,
        label="View responses for",
        value="All groups"
    )
    student_group_dropdown
    return (student_group_dropdown,)


@app.cell
def _(mo, pd, student_data, student_group_dropdown, tabs):
    mo.stop(tabs.value != "👤 By Student")

    selected_group = student_group_dropdown.value
    if selected_group == "All groups":
        filtered = student_data
    else:
        filtered = student_data[student_data['team'] == selected_group]

    text_questions = [
        ("STAR Method Response", "star_response"),
        ("Skills Learned", "skills_learned"),
        ("How Were Tasks Divided?", "task_division"),
        ("What to Continue", "continue_doing"),
        ("What to Stop", "stop_doing"),
        ("What to Start", "start_doing"),
    ]

    def _build_text_responses(data):
        sections = []
        for _, r in data.iterrows():
            start = r['start_date'].strftime('%Y-%m-%d') if pd.notna(r['start_date']) else 'N/A'
            end = r['end_date'].strftime('%Y-%m-%d') if pd.notna(r['end_date']) else 'N/A'

            parts = [f"### {r['team']}", f"**Period:** {start} → {end}", ""]
            for label, col in text_questions:
                val = str(r[col]) if pd.notna(r[col]) else None
                if val and len(val) > 5:
                    parts.append(f"**{label}:**")
                    parts.append(f"> {val}")
                    parts.append("")

            sections.append(mo.md("\n".join(parts)))
        return sections

    mo.vstack([mo.md("---")] + _build_text_responses(filtered))
    return


@app.cell
def _(df, mo, tabs):
    mo.stop(tabs.value != "👥 By Team")

    teams = sorted(df['team'].unique())
    team_dropdown = mo.ui.dropdown(
        options={team: team for team in teams},
        label="Select a team",
        value=teams[0]
    )
    team_dropdown
    return (team_dropdown,)


@app.cell
def _(df, mo, tabs, team_dropdown):
    mo.stop(tabs.value != "👥 By Team")

    selected_team = team_dropdown.value
    team_data = df[df['team'] == selected_team]

    show_individual_scores = mo.ui.checkbox(label="Show individual scores", value=False)

    mo.vstack([
        mo.md(f"## 👥 Team: {selected_team}"),
        show_individual_scores,
    ])
    return show_individual_scores, team_data


@app.cell
def _(mo, show_individual_scores, tabs, team_data):
    mo.stop(tabs.value != "👥 By Team")

    def _build_team_score_table(data, show_individual):
        _members = data['name'].unique().tolist()
        _score_keys = ['contribution_score', 'dynamics_score', 'reflection_score']
        _avg_c = data['contribution_score'].mean()
        _avg_d = data['dynamics_score'].mean()
        _avg_r = data['reflection_score'].mean()

        if show_individual and len(_members) > 1:
            _header = "| Category | " + " | ".join(_members) + " | Average |"
            _sep = "|----------|" + "|".join(["------" for _ in _members]) + "|---------|"
            _cat_labels = ['Contribution', 'Group Dynamics', 'Reflection']
            _rows = []
            for _cat, _key in zip(_cat_labels, _score_keys):
                _per_member = " | ".join(
                    str(int(r[_key])) if r[_key] is not None else "–"
                    for _, r in data.iterrows()
                )
                _avg = data[_key].mean()
                _rows.append(f"| {_cat} | {_per_member} | **{_avg:.2f}** |")

            _per_member_overall = " | ".join(
                f"{0.5 * r['contribution_score'] + 0.3 * r['dynamics_score'] + 0.2 * r['reflection_score']:.2f}"
                if all(r[k] is not None for k in _score_keys) else "–"
                for _, r in data.iterrows()
            )
            _overall = 0.5 * _avg_c + 0.3 * _avg_d + 0.2 * _avg_r
            _rows.append(f"| **Overall** | {_per_member_overall} | **{_overall:.2f}** |")
            return "\n        ".join([_header, _sep] + _rows), _members
        else:
            _overall = 0.5 * _avg_c + 0.3 * _avg_d + 0.2 * _avg_r
            return f"""| Category | Average |
        |----------|---------|
        | Contribution | **{_avg_c:.2f}** |
        | Group Dynamics | **{_avg_d:.2f}** |
        | Reflection | **{_avg_r:.2f}** |
        | **Overall** | **{_overall:.2f}** |""", _members

    _table, _members = _build_team_score_table(team_data, show_individual_scores.value)

    mo.md(
        f"""
        **Members ({len(_members)}):** {', '.join(_members)}

        ### Team Scores (1=Best, 4=Lowest)

        {_table}
        """
    )
    return


@app.cell
def _(mo, pd, tabs, team_data):
    mo.stop(tabs.value != "👥 By Team")

    # Time span overview
    def _fmt_date(d):
        return d.strftime('%Y-%m-%d') if pd.notna(d) else 'N/A'

    earliest_start = team_data['start_date'].min()
    latest_end = team_data['end_date'].max()

    _date_rows = "\n".join([
        f"| {r['name']} | {_fmt_date(r['start_date'])} | {_fmt_date(r['end_date'])} |"
        for _, r in team_data.iterrows()
    ])

    _time_table = f"""| Member | Start | End |
    |--------|-------|-----|
    {_date_rows}"""

    mo.md(
        f"""### Time Span

    **Team active period:** {_fmt_date(earliest_start)} → {_fmt_date(latest_end)}

    {_time_table}"""
    )
    return


@app.cell
def _(mo, tabs):
    mo.stop(tabs.value != "👥 By Team")

    team_question_map = {
        "How did your group decide on deadlines and divide tasks?": ("task_division", "text"),
        "Overall, how would you describe the task-division process?": ("task_process", "categorical"),
        "When disagreements occurred, how were they handled?": ("disagreements", "categorical"),
        "Did working as a group improve the final outcome?": ("group_outcome", "categorical"),
        "What should be continued?": ("continue_doing", "text"),
        "What should the group stop doing?": ("stop_doing", "text"),
        "What should the group start doing?": ("start_doing", "text"),
    }

    team_question_selector = mo.ui.multiselect(
        options=list(team_question_map.keys()),
        label="Select questions to display",
        value=[list(team_question_map.keys())[0]]
    )
    team_question_selector
    return team_question_map, team_question_selector


@app.cell
def _(mo, pd, tabs, team_data, team_question_map, team_question_selector):
    mo.stop(tabs.value != "👥 By Team")

    def _render_team_questions(data, qmap, selected):
        def _render_one(label, col, qtype):
            _parts = [f"**{label}**", ""]
            _parts.append("| Member | Answer |")
            _parts.append("|--------|--------|")
            for _, _r in data.iterrows():
                _v = str(_r[col]) if pd.notna(_r[col]) else "–"
                _parts.append(f"| {_r['name']} | {_v} |")
            return "\n".join(_parts)

        _sections = []
        for _i, _q in enumerate(selected):
            if _i > 0:
                _sections.append(mo.md("---"))
            _col, _qtype = qmap[_q]
            _sections.append(mo.md(_render_one(_q, _col, _qtype)))
        return _sections

    _result = _render_team_questions(team_data, team_question_map, team_question_selector.value)
    mo.vstack(_result) if _result else mo.md("*Select one or more questions above to view answers.*")
    return


@app.cell
def _(mo, tabs):
    mo.stop(tabs.value != "📊 Distributions")

    mo.md("## 📊 Distributions")
    return


@app.cell
def _(alt, df, mo, tabs):
    mo.stop(tabs.value != "📊 Distributions")

    # Responses per student
    responses_per_student = df['name'].value_counts().reset_index()
    responses_per_student.columns = ['student', 'responses']

    chart1 = alt.Chart(responses_per_student).mark_bar().encode(
        x=alt.X('student:N', sort='-y', title='Student'),
        y=alt.Y('responses:Q', title='Number of Groups'),
        color=alt.Color('responses:Q', scale=alt.Scale(scheme='blues'))
    ).properties(
        title='How Many Groups Did Each Student Participate In?',
        width=500,
        height=300
    )

    mo.ui.altair_chart(chart1)
    return


@app.cell
def _(alt, df, mo, tabs):
    mo.stop(tabs.value != "📊 Distributions")

    # Team sizes
    team_sizes = df.groupby('team')['name'].nunique().reset_index()
    team_sizes.columns = ['team', 'members']

    chart2 = alt.Chart(team_sizes).mark_bar().encode(
        x=alt.X('team:N', sort='-y', title='Team'),
        y=alt.Y('members:Q', title='Number of Members'),
        color=alt.Color('members:Q', scale=alt.Scale(scheme='greens'))
    ).properties(
        title='Team Sizes (Unique Members)',
        width=500,
        height=300
    )

    mo.ui.altair_chart(chart2)
    return


@app.cell
def _(mo):
    score_toggle = mo.ui.switch(label="Show Final Score", value=False)
    avg_toggle = mo.ui.switch(label="Show average per student", value=True)
    return avg_toggle, score_toggle


@app.cell
def _(alt, avg_toggle, df, mo, score_toggle, tabs):
    mo.stop(tabs.value != "📊 Distributions")

    if avg_toggle.value:
        # Aggregate per student: average sub-scores across teams
        student_avg = df.groupby('name').agg(
            contribution_score=('contribution_score', 'mean'),
            dynamics_score=('dynamics_score', 'mean'),
            reflection_score=('reflection_score', 'mean')
        ).reset_index()
    else:
        student_avg = df.copy()

    if score_toggle.value:
        # Final score distribution
        student_avg['final_score'] = (
            0.5 * student_avg['contribution_score'] +
            0.3 * student_avg['dynamics_score'] +
            0.2 * student_avg['reflection_score']
        ).round(2)

        chart = alt.Chart(student_avg).mark_bar().encode(
            x=alt.X('final_score:Q', bin=alt.Bin(step=0.25), title='Final Score (1=Best, 4=Lowest)'),
            y=alt.Y('count()', title='Count'),
        ).properties(
            title="Distribution of Final Scores" + (" (per student)" if avg_toggle.value else " (all entries)"),
            width=300,
            height=200
        )
    else:
        # Sub-score distributions
        id_vars = ['name'] if avg_toggle.value else ['name', 'team']
        score_data = student_avg[id_vars + ['contribution_score', 'dynamics_score', 'reflection_score']].melt(
            id_vars=id_vars,
            var_name='category',
            value_name='score'
        )
        score_data['category'] = score_data['category'].str.replace('_score', '').str.title()

        if avg_toggle.value:
            chart = alt.Chart(score_data).mark_bar().encode(
                x=alt.X('score:Q', bin=alt.Bin(step=0.25), title='Score (1=Best, 4=Lowest)'),
                y=alt.Y('count()', title='Count'),
                color=alt.Color('category:N', title='Category'),
                column=alt.Column('category:N', title=None)
            ).properties(
                title="Distribution of Self-Assessment Scores (per student)",
                width=150,
                height=200
            )
        else:
            chart = alt.Chart(score_data).mark_bar().encode(
                x=alt.X('score:O', title='Score (1=Best, 4=Lowest)'),
                y=alt.Y('count()', title='Count'),
                color=alt.Color('category:N', title='Category'),
                column=alt.Column('category:N', title=None)
            ).properties(
                title="Distribution of Self-Assessment Scores (all entries)",
                width=150,
                height=200
            )

    mo.vstack([mo.hstack([score_toggle, avg_toggle]), mo.ui.altair_chart(chart)])

    return


if __name__ == "__main__":
    app.run()
