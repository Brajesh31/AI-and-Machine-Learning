# 📦 Installation Guide

## Requirements

- Python 3.9 or newer as a practical baseline.
- Jupyter Notebook or JupyterLab.
- Access to the CSV files required by the notebook you intend to run.
- A terminal for environment setup.

The repository includes compatible dependency ranges in `requirements.txt` and development tools in `requirements-dev.txt`. These ranges are not a fully locked environment. Record the installed versions when publishing results.

## Create a virtual environment

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

### macOS or Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

## Install common dependencies

```bash
python -m pip install -r requirements.txt
```

These are a practical shared set based on notebook imports and project descriptions. A notebook may need additional packages depending on all cells and data-specific operations.

## Start Jupyter

From the repository root:

```bash
jupyter notebook
```

Select the virtual environment's Python kernel. Confirm the notebook's CSV files exist in the expected working directory before running cells.

## Confirm versions

```bash
python --version
python -m pip show pandas numpy scikit-learn statsmodels
```

Record versions when sharing results or reporting a problem.
