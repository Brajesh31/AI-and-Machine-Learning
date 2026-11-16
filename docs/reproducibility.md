# 🔁 Reproducibility Guide

A notebook is reproducible only when another person can obtain compatible data, packages, configuration, and execution steps and can understand the source of variation.

## Current repository state

The repository currently includes four notebooks and documentation. It includes `requirements.txt` and `requirements-dev.txt` with compatible version ranges, but not a fully locked environment or the CSV datasets referenced by the notebooks. Saved notebook outputs may be stale and should not be treated as a current experiment run.

## Recommended environment capture

Record:
- Python version.
- Jupyter and notebook version.
- pandas and NumPy versions.
- scikit-learn version.
- Statsmodels version.
- Matplotlib and Seaborn versions.
- Operating system and architecture.
- Dataset filename, version, source, and checksum.

After installing a stable environment, export a minimal dependency file for the libraries actually used. Do not blindly pin every transitive package as a direct dependency.

## Randomness

Where supported, define a fixed `random_state` for data splits, model estimators, and stochastic processes. Record the seed. Random seeds improve repeatability but do not guarantee identical results across different library versions or computational environments.

## Notebook execution

1. Activate the documented virtual environment.
2. Start Jupyter from the repository root.
3. Confirm the expected input dataset is present.
4. Restart the kernel.
5. Run all cells from top to bottom.
6. Check warnings and outputs.
7. Save the notebook only after reviewing output for sensitive information.

## Clean execution

A clean-kernel run is more meaningful than rerunning selected cells in an old session. Out-of-order execution can leave variables from earlier cells and produce misleading results.

## Data and split reproducibility

Record the exact split method, test size, stratification, grouping, chronological ordering, and seed. For time-dependent cryptocurrency observations, a chronological split may be more appropriate than random splitting.

## Future repository improvements

- Add a pinned environment after verifying imports.
- Add a dataset manifest and provenance record.
- Validate notebooks in CI with safe, available data or mocked inputs.
- Remove stale outputs when they create confusion or expose private information.
- Add experiment metadata and metric summaries.
