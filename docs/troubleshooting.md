# Troubleshooting

## Import errors

Activate `.venv` and install the documented notebook dependencies.

## Missing files

Start Jupyter from the repository root and confirm that the notebook's relative data paths exist.

## Inconsistent results

Restart the kernel, run cells in order, check random seeds and package versions, and verify that preprocessing is fitted only on training data.

## Notebook warnings

Inspect warnings rather than hiding them. Feature-name, dtype, and convergence warnings can change the interpretation of results.
