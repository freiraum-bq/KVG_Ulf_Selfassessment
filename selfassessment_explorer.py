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
    import base64
    import io

    return alt, base64, io, mo, pd


@app.cell
def _(mo):
    mo.md("""
    # 📊 Self-Assessment Questionnaire Explorer

    Explore the self-assessment responses from your team project.
    Students answered this questionnaire for **each group** they participated in.

    Use the tabs below to explore different aspects of the data.
    """)
    return


@app.cell(hide_code=True)
def _():
    # Generated the base64 string locally from the excel table & copy pasted here via "python3 -c "import base64; print(base64.b64encode(open('answers.xlsx', 'rb').read()).decode())""
    DataBase64 = """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"""
    return (DataBase64,)


@app.cell
def _(DataBase64, base64, io, pd):
    excel_bytes = base64.b64decode(DataBase64)
    df = pd.read_excel(io.BytesIO(excel_bytes))

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
        options=students,
        label="Select a student",
        value=students[0]
    )
    student_dropdown
    return (student_dropdown,)


@app.cell
def _(df, mo, pd, student_dropdown, tabs):
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
            _header = "| Category | " + " | ".join(teams) + " |"
            _sep = "|----------|" + "|".join(["------" for _ in teams]) + "|"
            _cat_labels = ['Contribution (50%)', 'Group Dynamics (30%)', 'Reflection (20%)']
            _rows = []
            for _cat, _key in zip(_cat_labels, _score_keys):
                _per_group = " | ".join(
                    str(int(r[_key])) if r[_key] is not None else "–"
                    for _, r in data.iterrows()
                )
                _rows.append(f"| {_cat} | {_per_group} |")

            _per_group_overall = " | ".join(
                f"{0.5 * r['contribution_score'] + 0.3 * r['dynamics_score'] + 0.2 * r['reflection_score']:.2f}"
                if all(r[k] is not None for k in _score_keys) else "–"
                for _, r in data.iterrows()
            )
            _rows.append(f"| **Overall** | {_per_group_overall} |")

            _per_group_period = " | ".join(
                f"{r['start_date'].strftime('%Y-%m-%d') if pd.notna(r['start_date']) else 'N/A'} → {r['end_date'].strftime('%Y-%m-%d') if pd.notna(r['end_date']) else 'N/A'}"
                for _, r in data.iterrows()
            )
            _rows.append(f"| Period | {_per_group_period} |")

            _per_group_active_days = " | ".join(
                str((r['end_date'] - r['start_date']).days) if pd.notna(r['start_date']) and pd.notna(r['end_date']) else "–"
                for _, r in data.iterrows()
            )
            _rows.append(f"| **Active Days** | {_per_group_active_days} |")
            return "\n        ".join([_header, _sep] + _rows)
        else:
            _overall = 0.5 * _avg_c + 0.3 * _avg_d + 0.2 * _avg_r
            _r = data.iloc[0]
            _start = _r['start_date'].strftime('%Y-%m-%d') if pd.notna(_r['start_date']) else 'N/A'
            _end = _r['end_date'].strftime('%Y-%m-%d') if pd.notna(_r['end_date']) else 'N/A'
            _active_days = str((_r['end_date'] - _r['start_date']).days) if pd.notna(_r['start_date']) and pd.notna(_r['end_date']) else '–'
            return f"""| Category | Score |
        |----------|-------|
        | Contribution (50%) | **{_avg_c:.2f}** |
        | Group Dynamics (30%) | **{_avg_d:.2f}** |
        | Reflection (20%) | **{_avg_r:.2f}** |
        | **Overall** | **{_overall:.2f}** |
        | **Period** | {_start} → {_end} |
        | **Active Days** | {_active_days} |"""

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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### See the answers of that student for each group they participated in.
    """)
    return


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

    def _calc_active_days(row):
        if pd.notna(row['start_date']) and pd.notna(row['end_date']):
            return str((row['end_date'] - row['start_date']).days)
        return '–'

    earliest_start = team_data['start_date'].min()
    latest_end = team_data['end_date'].max()

    _date_rows = "\n".join([
        f"| {r['name']} | {_fmt_date(r['start_date'])} | {_fmt_date(r['end_date'])} | {_calc_active_days(r)} |"
        for _, r in team_data.iterrows()
    ])

    _time_table = f"""| Member | Start | End | Active Days |
    |--------|-------|-----|-------------|
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
def _(active_days_group_dropdown, alt, df, mo, pd, tabs):
    mo.stop(tabs.value != "📊 Distributions")

    # Calculate active days per row
    _df = df.copy()
    _df['active_days'] = _df.apply(
        lambda r: (r['end_date'] - r['start_date']).days if pd.notna(r['start_date']) and pd.notna(r['end_date']) else None,
        axis=1
    )
    _df = _df.dropna(subset=['active_days'])

    _selected_group = active_days_group_dropdown.value

    _note = ""

    if _selected_group == "Average per group":
        # Filter out negative active days for the overview
        _df_positive = _df[_df['active_days'] >= 0]
        _excluded = _df[_df['active_days'] < 0]
        _chart_data = _df_positive.groupby('team').agg(
            active_days=('active_days', 'mean'),
            members=('name', lambda x: ', '.join(x))
        ).reset_index()
        _chart_data.columns = ['group', 'active_days', 'members']
        _chart_data['active_days'] = _chart_data['active_days'].round(1)
        _title = "Average Active Days per Group"

        if not _excluded.empty:
            _neg_groups = _excluded['team'].unique().tolist()
            _note = f"**Note:** *{len(_excluded)} entrie(s) with negative active days (likely incorrect dates) were excluded from this overview. Affected group(s): {', '.join(_neg_groups)}. Select a specific group to see all values.*"

        _chart = alt.Chart(_chart_data).mark_bar().encode(
            x=alt.X('group:N', sort='-y', title='Group'),
            y=alt.Y('active_days:Q', title='Avg Active Days'),
            color=alt.Color('active_days:Q', scale=alt.Scale(scheme='oranges'), legend=None),
            tooltip=[
                alt.Tooltip('group:N', title='Group'),
                alt.Tooltip('active_days:Q', title='Avg Active Days'),
                alt.Tooltip('members:N', title='Members'),
            ]
        ).properties(
            title=_title,
            width=500,
            height=300
        )
    else:
        # Active days per student for selected group (including negative values)
        _chart_data = _df[_df['team'] == _selected_group][['name', 'active_days']].copy()
        _chart_data.columns = ['student', 'active_days']
        _chart_data['active_days'] = _chart_data['active_days'].astype(int)
        _title = f"Active Days — {_selected_group}"

        _neg = _chart_data[_chart_data['active_days'] < 0]
        if not _neg.empty:
            _note = f"*Note: {len(_neg)} student(s) in this group have negative active days, which likely indicates incorrect start/end dates.*"

        _chart = alt.Chart(_chart_data).mark_bar().encode(
            x=alt.X('student:N', sort='-y', title='Student'),
            y=alt.Y('active_days:Q', title='Active Days'),
            color=alt.Color('active_days:Q', scale=alt.Scale(scheme='oranges'), legend=None),
            tooltip=[
                alt.Tooltip('student:N', title='Student'),
                alt.Tooltip('active_days:Q', title='Active Days'),
            ]
        ).properties(
            title=_title,
            width=500,
            height=300
        )

    _elements = [active_days_group_dropdown, mo.ui.altair_chart(_chart)]
    if _note:
        _elements.append(mo.md(_note))
    mo.vstack(_elements)
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
    return


@app.cell
def _():
    return


@app.cell
def _(df, mo, tabs):
    mo.stop(tabs.value != "📊 Distributions")

    active_days_group_options = ["Average per group"] + sorted(df['team'].unique().tolist())
    active_days_group_dropdown = mo.ui.dropdown(
        options=active_days_group_options,
        label="Filter by group",
        value="Average per group"
    )
    return (active_days_group_dropdown,)


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
