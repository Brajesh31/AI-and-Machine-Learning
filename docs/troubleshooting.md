# 🧯 Notebook Troubleshooting

## CSV file not found

Confirm the exact filename and start Jupyter from the repository root. The repository does not include the CSV files referenced by the notebooks. Obtain authorized copies from their original sources and document their provenance.

## ModuleNotFoundError

Activate the intended virtual environment and install the missing dependency. Confirm Jupyter uses the same Python interpreter where the package was installed.

## Kernel not found

Register the environment as a Jupyter kernel if necessary:

```bash
python -m pip install ipykernel
python -m ipykernel install --user --name ai-ml-notebooks --display-name "AI and ML Notebooks"
```

Restart Jupyter and select the named kernel.

## Notebook produces different results

Restart the kernel and run every cell in order. Check package versions, dataset version, random seeds, train/test split, and preprocessing steps.

## Unexpectedly high test accuracy

Investigate data leakage, duplicate rows, target leakage, preprocessing performed before splitting, and repeated use of the test set for model selection.

## NaN or infinity errors

Inspect raw columns, invalid zero values, logarithmic transformations, division operations, and imputation order. Do not replace missing values blindly without checking feature meaning.

## GridSearchCV is slow

Inspect the size of the parameter grid, number of folds, estimator complexity, dataset size, and parallel worker setting. Record any reductions because they change the search procedure.

## Warnings

Review convergence, dtype, feature-name, and deprecation warnings. Do not hide warnings just to make output look clean.
