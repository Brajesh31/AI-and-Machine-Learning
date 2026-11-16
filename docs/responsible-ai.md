# 🩺 Responsible AI and Healthcare Use

Two notebooks in this repository contain healthcare-related prediction exercises. Their purpose is educational. They are not clinical tools and must not be used for patient diagnosis, treatment, triage, screening, insurance eligibility, employment, or other high-impact decisions.

## Why educational metrics are not clinical evidence

A model can achieve a high test score and still fail in practice because:
- Training data does not represent the intended population.
- Labels are inaccurate, incomplete, or defined differently from clinical outcomes.
- Measurements are taken at different points in the care process.
- Missing data patterns differ between sites.
- False positives and false negatives have unequal consequences.
- The model is poorly calibrated.
- Clinical workflows change after deployment.
- Data leakage inflates apparent performance.

## Target labels require domain context

The liver notebook references a `Report_curable` target. That column name does not establish a medical definition of curability or treatment outcome. Only the original dataset documentation and qualified domain experts can explain what the label represents.

The diabetes notebook uses a dataset target for diabetic/non-diabetic classification. Its source, cohort, data collection method, and representativeness must be established before conclusions are drawn.

## Bias and fairness

Review performance across relevant subgroups only when lawful, ethically sourced, sufficiently sized data is available. Do not infer protected characteristics from proxies. Report uncertainty and sample sizes, and avoid presenting subgroup metrics as reliable when the sample is small.

## Privacy

Never commit identifiable health records, private medical data, patient names, dates of birth, contact information, or record identifiers. Respect the dataset licence and access conditions. De-identification does not eliminate all re-identification risk.

## Human oversight

A future clinical tool would require independent clinical validation, governance, privacy and security review, robust monitoring, domain expert oversight, and applicable legal/regulatory assessment. These notebooks provide none of those safeguards.

## Responsible communication

Describe outputs as model predictions on a particular dataset, not as medical facts. State the target definition, population, split strategy, metrics, and limitations whenever reporting results.
