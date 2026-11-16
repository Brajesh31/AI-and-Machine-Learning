# 🏗️ Repository Architecture

This project is an educational collection of four independent Jupyter notebooks. It is not a deployed application or a shared machine-learning package.

## Repository layers

```text
Repository
├── *.ipynb                 Four independent experiments
├── data/README.md          Dataset manifest and safe placement guidance
├── scripts/                Static notebook validation utility
├── tests/                  Repository integrity tests
├── docs/                   Technical and responsible-use documentation
├── .github/workflows/      Continuous integration
├── requirements.txt        Runtime dependency ranges
└── requirements-dev.txt    Runtime plus developer validation tools
```

## Notebook lifecycle

Each notebook reads a local CSV, inspects and transforms tabular data, creates features, fits estimators, and displays evaluation output. The exact pipeline is notebook-specific. Shared application services, a database, model-serving API, experiment tracker, and deployment environment are not implemented.

## Supporting code

- `scripts/validate_notebooks.py` checks notebook JSON and parses code cells for Python syntax without executing them.
- `tests/test_repository.py` checks the expected notebook count, notebook format, dataset manifest, and documentation index.
- `.github/workflows/ci.yml` runs static validation and repository tests on pushes and pull requests.

## Data boundary

CSV datasets are intentionally external until their provenance and redistribution permissions are confirmed. Their expected filenames are listed in [data/README.md](../data/README.md). Notebook execution and model training remain dependent on obtaining those files.

## Design constraints

Do not introduce an API or database merely to make the repository look like an application. Keep the project notebook-first unless a concrete reusable workflow justifies extracting shared modules. Healthcare notebooks must remain clearly labelled as educational examples.
