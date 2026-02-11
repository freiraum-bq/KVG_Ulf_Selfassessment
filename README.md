# 📊 Self-Assessment Questionnaire Explorer

A [Marimo](https://marimo.io) notebook for exploring self-assessment responses of the KVG Bus project.
Also see https://sustainabilitymethods.org/index.php/Marimo_Notebooks
It is recommended to use the package manager UV: https://sustainabilitymethods.org/index.php/UV_as_Package_Manager 


## Run interactive marimo notebook

To run the noteboook, simply click this link: https://freiraum-bq.github.io/KVG_Ulf_Selfassessment/ (link in the "about" section)

## Features

- **By Student** — View scores, active days, and text responses per student across all their groups
- **By Team** — View aggregated team scores, time spans, and qualitative answers
- **Distributions** — Interactive charts for group participation, team sizes, score distributions, and active days

## Data

The assessment data (`answers.xlsx`) is embedded directly in the notebook as a Base64-encoded string, since Marimo notebooks cannot reliably access external files when deployed for external users.

## Dependencies
No dependencies when you want to run it in your browser. 
Running it locally:

- Python ≥ 3.13
- marimo
- pandas
- openpyxl
- altair
