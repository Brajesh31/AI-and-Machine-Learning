# 🧑‍💻 Notebook Development Guide

## Before editing

Identify the notebook, the question it explores, the target variable, the data source, and the intended model. Read all relevant cells, including preprocessing and evaluation, before changing a single cell.

## Notebook hygiene

- Use descriptive markdown headings.
- Keep imports grouped and avoid repeated conflicting imports.
- Explain transformations and why they are used.
- Avoid machine-specific absolute paths.
- Use reproducible random seeds where appropriate.
- Keep a clean execution order.
- Clear sensitive or confusing outputs before committing.
- Avoid storing private datasets or credentials in notebook metadata and outputs.

## Leakage prevention

Split data before fitting preprocessing. Fit imputers, scalers, encoders, selectors, and outlier thresholds on training data only. Prefer a scikit-learn Pipeline/ColumnTransformer where practical.

## Model development

Keep baseline and candidate models distinct. Document feature sets, target, parameters, validation method, and metrics. Do not tune on the final test data.

## Healthcare-related work

Do not frame educational predictions as medical recommendations. Include the responsible-use limitations in any report or presentation that uses these notebooks.

## Review before commit

- [ ] Notebook restarts and runs from top to bottom.
- [ ] Required dataset provenance is documented.
- [ ] No private data or credentials are present.
- [ ] No absolute local paths remain.
- [ ] Data split and preprocessing are leakage-aware.
- [ ] Metrics match the task.
- [ ] Results and limitations are explained.
- [ ] Documentation is updated.
