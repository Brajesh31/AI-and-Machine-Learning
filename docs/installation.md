# Installation

Use Python 3.9 or newer and an isolated environment:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

Run Jupyter from the repository root so relative data paths resolve:

```powershell
jupyter notebook
```
