# 🧪 Testing and Validation Guide

This repository is a collection of Jupyter notebooks. It does not currently expose a Python package or application with a conventional unit-test suite. Validation is therefore split into notebook-file checks, notebook execution, data checks, and experiment review.

## 1. What CI currently checks

The GitHub Actions workflow at `.github/workflows/ci.yml`:
- Finds Jupyter notebooks in the repository root.
- Parses each notebook as nbformat version 4.
- Runs nbformat structural validation.
- Fails when no root-level notebooks are found or a notebook is malformed.

This is a structural check only. It does not execute notebook cells, download datasets, verify model accuracy, or prove that a model is suitable for any real-world decision.

## 2. Validate notebook structure locally

Create an isolated Python environment, then install the validator:

```bash
python -m pip install nbformat
python - <<'PY'
from pathlib import Path
import nbformat

notebooks = sorted(Path(".").glob("*.ipynb"))
if not notebooks:
    raise SystemExit("No root-level notebooks found")

for path in notebooks:
    notebook = nbformat.read(path, as_version=4)
    nbformat.validate(notebook)
    print(f"VALID: {path}")
PY
```

## 3. Execute a notebook

Only execute a notebook after obtaining its required dataset from a legitimate source and confirming that its licence permits the intended use.

```bash
python -m pip install jupyter nbconvert
jupyter nbconvert --to notebook --execute \
  --inplace "path/to/notebook.ipynb"
```

Run from the repository root unless the notebook explicitly documents another working directory. Execution may fail until the missing CSV files and compatible dependencies are supplied.

Do not overwrite the only copy of a notebook when testing substantial changes. Work on a separate branch or temporary copy.

## 4. Data validation checklist

Before model fitting, inspect:
- Dataset row and column counts.
- Column names and data types.
- Missing-value counts and percentages.
- Duplicate records.
- Target distribution and class balance.
- Impossible values and domain constraints.
- Potential target leakage and identifier columns.
- Dataset provenance, licence, collection date, and version.

Check that the target column exists and has the expected values. Never silently rename or drop columns just to make a cell execute.

## 5. Machine-learning validation checklist

- Split the data before fitting learned preprocessing steps.
- Fit imputers, scalers, encoders, and feature selectors on training data only.
- Use a validation strategy appropriate to the data, including stratification or time-aware splitting where justified.
- Keep the final test set out of hyperparameter selection.
- Compare against a simple baseline.
- Report class-wise metrics for classification.
- Inspect confusion matrices and error patterns.
- Record random seeds, parameters, and package versions.
- Check for leakage, imbalance, and overfitting.

## 6. Reproducibility record

For every meaningful experiment, record:

| Field | What to record |
|---|---|
| Notebook | Exact notebook filename and revision |
| Dataset | Source, licence, version, and checksum where practical |
| Target | Target column and task definition |
| Split | Method, proportions, seed, and stratification |
| Preprocessing | Imputation, encoding, scaling, feature selection |
| Model | Estimator and complete relevant parameters |
| Validation | Cross-validation strategy and folds |
| Metrics | Metric names, values, and evaluation split |
| Environment | Python and key library versions |
| Limitations | Missing data, known bias, and execution constraints |

## 7. Current limitations

- The repository does not include the CSV datasets referenced by the notebooks.
- A pinned dependency manifest is not currently provided.
- CI validates notebook structure but does not execute the experiments.
- No claim is made that all notebooks have been freshly executed.
- No model-performance threshold is defined as a release gate.

These limitations should be addressed with real dataset provenance and repeatable experiments, not fabricated test results.
