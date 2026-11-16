# 🗺️ AI and Machine Learning Roadmap

This roadmap distinguishes implemented repository improvements from work that still depends on external datasets or a deeper experiment redesign. It is not a delivery commitment.

## ✅ Completed repository foundations

- [x] Add runtime and development dependency manifests.
- [x] Add a dataset manifest and local placement guidance.
- [x] Add notebook JSON and Python-cell syntax validation.
- [x] Add repository integrity tests and CI.
- [x] Document notebook architecture, methodology, evaluation, and responsible use.
- [x] Correct the regression notebook's inline package-install command.
- [x] Correct the diabetes BMI category ordering.
- [x] Use Logistic Regression for the liver notebook's binary classification section.
- [x] Use the cross-validated best estimator for Random Forest evaluation.
- [x] Remove unnecessary hourly README timestamp commits.

## Priority 1: Dataset provenance and availability

- [ ] Verify the official source, version, licence, and redistribution rights for every dataset.
- [ ] Add data dictionaries for each target and feature.
- [ ] Decide whether any source dataset can legally be redistributed.
- [ ] Add checksums and dataset version metadata where practical.
- [ ] Run each notebook against its correct, authorized source dataset.

## Priority 2: Methodology and leakage review

- [ ] Move learned preprocessing and feature selection inside training-only pipelines.
- [ ] Audit target leakage in all notebooks.
- [ ] Use stratified validation for classification where appropriate.
- [ ] Use chronological or walk-forward splits for time-dependent cryptocurrency data.
- [ ] Add meaningful baselines and class-level metrics.
- [ ] Add residual analysis for regression.

## Priority 3: Reproducible experiment results

- [ ] Validate dependency ranges in a clean environment and produce a fully locked environment.
- [ ] Execute each notebook from a clean kernel with documented datasets.
- [ ] Record verified metrics, parameters, random seeds, and environment versions.
- [ ] Remove or refresh stale notebook outputs after reproducible execution.

## Priority 4: Responsible AI and maintenance

- [ ] Review healthcare target definitions with qualified domain expertise before making any real-world claims.
- [ ] Add bias and subgroup analysis only where data governance and sample sizes support it.
- [ ] Keep model cards synchronized with verified experiment runs.
- [ ] Review dependency and workflow security periodically.

## Scope boundary

The repository remains a notebook-based educational project. A web API, database, production model-serving stack, or model registry should only be introduced if a real use case justifies the added complexity.
