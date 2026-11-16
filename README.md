# 🤖 AI and Machine Learning

<p align="center">
  <strong>A collection of hands-on Jupyter notebooks exploring data preprocessing, regression, healthcare classification, and ensemble learning.</strong>
</p>

<p align="center">
  <a href="https://github.com/Brajesh31/AI-and-Machine-Learning">Repository</a> ·
  <a href="docs/README.md">Documentation</a> ·
  <a href="CONTRIBUTING.md">Contributing</a> ·
  <a href="ROADMAP.md">Roadmap</a>
</p>

> [!IMPORTANT]
> The healthcare notebooks are educational experiments. They are not clinically validated, must not be used for diagnosis, treatment, screening, insurance, or other high-impact decisions, and should not be interpreted as medical advice. The repository does not include the referenced CSV datasets. See [data/README.md](data/README.md) for the exact expected filenames.

---

## 📚 Table of Contents

1. [🌟 Project Overview](#-project-overview)
2. [🎯 Learning Objectives](#-learning-objectives)
3. [🗂️ Notebook Catalogue](#️-notebook-catalogue)
4. [🧪 Workflow and Methodology](#-workflow-and-methodology)
5. [🧰 Technology Stack](#-technology-stack)
6. [🗂️ Repository Structure](#️-repository-structure)
7. [📊 Dataset Requirements](#-dataset-requirements)
8. [🖥️ Environment Requirements](#️-environment-requirements)
9. [🚀 Installation](#-installation)
10. [▶️ Run the Notebooks](#️-run-the-notebooks)
11. [📏 Model Evaluation](#-model-evaluation)
12. [⚠️ Reproducibility and Data Leakage](#️-reproducibility-and-data-leakage)
13. [🩺 Healthcare and Responsible AI Notice](#-healthcare-and-responsible-ai-notice)
14. [🔐 Data Privacy and Security](#-data-privacy-and-security)
15. [🧯 Troubleshooting](#-troubleshooting)
16. [🤝 Contributing](#-contributing)
17. [🗺️ Roadmap](#️-roadmap)
18. [📖 Documentation](#-documentation)
19. [📄 License](#-license)

---

## 🌟 Project Overview

This repository contains four independent Jupyter notebooks developed as practical exercises in data analysis and machine learning. The examples cover the progression from raw tabular data to preprocessing, model fitting, prediction, and performance evaluation.

The notebooks are educational artifacts, not a single packaged application. Each notebook has its own dataset assumptions, preprocessing steps, model choices, and execution flow. There is no shared Python package, API service, database, hosted model, or command-line application in the current repository.

### What is included

- A regression-oriented preprocessing workflow using OLS regression.
- A liver-disease classification notebook comparing several supervised learning methods.
- A diabetes classification example using Gaussian and Bernoulli Naive Bayes.
- A cryptocurrency-feature classification example using Random Forest and GridSearchCV.

### What is not included

- The source CSV datasets referenced by the notebooks.
- A fully locked environment file. `requirements.txt` currently provides compatible version ranges.
- A unified training pipeline or reusable model package.
- A deployed inference API or web interface.
- A model registry, experiment tracker, or saved production model.
- Clinical validation or authorization for medical use.

## 🎯 Learning Objectives

Working through these notebooks can help you learn how to:

1. Inspect tabular data with Pandas.
2. Identify missing values, duplicate records, unusual values, and outliers.
3. Prepare numerical and categorical features.
4. Apply encoding and scaling transformations.
5. Split data into training and testing subsets.
6. Fit regression and classification estimators.
7. Compare model behaviour using evaluation metrics.
8. Tune selected hyperparameters with cross-validation.
9. Interpret the limitations of small educational experiments.
10. Build more reproducible and responsible machine-learning workflows.

## 🗂️ Notebook Catalogue

The repository contains these four notebooks. Open each notebook in GitHub or launch it locally through Jupyter.

### 1. Mini Project: Data Preprocessing and Regression Model

**File:** [Mini Project - Data Preprocessing & Regression Model.ipynb](Mini%20Project%20-%20Data%20Preprocessing%20%26%20Regression%20Model.ipynb)

This notebook focuses on preparing tabular data for regression. Its stated workflow includes missing-value handling, duplicate checks, IQR-based outlier treatment, categorical encoding, transformation, feature engineering, train/test splitting, and Ordinary Least Squares regression using Statsmodels.

**Topics covered**
- Numerical and categorical missing-value treatment.
- Duplicate inspection.
- Boxplots and interquartile-range reasoning.
- One-hot encoding.
- Standardization and normalization.
- Feature transformation and engineering.
- OLS regression and residual-oriented evaluation.
- R², mean absolute error, and mean squared error.

**Dataset requirement:** `LoansData (1).csv`, not included in this repository.

### 2. Liver Disease Prediction

**File:** [Liver Disease Prediction (KNN, Decision Tree, Naive Bayes).ipynb](Liver%20Disease%20Prediction%20%28KNN%20%2C%20Desicion%20Tree%20%2C%20Naive%20Bayes%29.ipynb)

This notebook loads `liver_cirrhosis.csv` and contains K-Nearest Neighbors, Decision Tree, Logistic Regression, and Support Vector Machine classification workflows. The filename mentions Naive Bayes, but the current notebook does not implement a Naive Bayes estimator. The binary `Report_curable` target is an educational label derived from the dataset's Stage field, not a medical determination.

The notebook uses a target field called `Report_curable` in its evaluation examples. That label should be treated as a dataset-specific target, not as an authoritative medical determination.

**Topics covered**
- Tabular medical-data preparation.
- Train/test splitting.
- Standard scaling for distance-based models.
- KNN and Decision Tree classification.
- Model comparison and classification reports.
- Accuracy, precision, recall, and F1-score.

**Dataset requirement:** `liver_cirrhosis.csv`, not committed in this repository.

### 3. Mini Project: Naive Bayes on Healthcare Dataset

**File:** [Mini project (Naive Bayes Healthcare dataset).ipynb](Mini%20project%20%28Naive%20Bayes%20Healthcare%20dataset%29.ipynb)

This notebook loads `diabetes.csv` and compares Gaussian Naive Bayes with Bernoulli Naive Bayes. It engineers glucose, BMI, and age categories, applies dummy encoding, filters insulin values using an IQR rule, and transforms insulin and skin-thickness features. The current code does not implement the zero-to-missing replacement, median imputation, or scaling previously described in this README.

**Topics covered**
- Glucose, BMI, and age-derived categories.
- One-hot/dummy encoding.
- IQR-based filtering of insulin values.
- Log transformation of insulin.
- Square-root transformation of skin thickness.
- GaussianNB and BernoulliNB comparison.
- GaussianNB and BernoulliNB.
- Train and test accuracy comparison.

**Dataset requirement:** `diabetes.csv`, not committed in this repository.

### 4. Mini Project: Random Forest Classification

**File:** [Mini project (Random Forest).ipynb](Mini%20project%20%28Random%20Forest%29.ipynb)

This notebook loads `Cryptocurrency_FeaturedData.csv` and trains a Random Forest classifier. It also sets up a parameter search using GridSearchCV with a five-fold cross-validation strategy and accuracy scoring. The current notebook searches Random Forest hyperparameters with GridSearchCV, then evaluates the selected best estimator. It does not implement the KNN and Decision Tree comparisons mentioned in older descriptions.

**Topics covered**
- Data inspection and preprocessing.
- Random Forest classification.
- GridSearchCV.
- Number of estimators, tree depth, split size, leaf size, and feature selection.
- Cross-validation.
- Accuracy-based model selection.

**Dataset requirement:** `Cryptocurrency_FeaturedData.csv`, not committed in this repository.

> [!NOTE]
> Dataset names and model methods above are based on notebook code and repository documentation. They do not imply that the notebooks have been executed successfully in the current environment or that any reported model is validated.

## 🧪 Workflow and Methodology

Most notebooks follow a similar conceptual lifecycle:

```text
Raw tabular dataset
        |
        v
Data inspection and understanding
        |
        v
Missing value / duplicate checks
        |
        v
Feature preparation and transformation
        |
        v
Train / test split
        |
        v
Model fitting and tuning
        |
        v
Predictions on held-out data
        |
        v
Metrics and interpretation
```

The exact order differs by notebook. A robust future version should place splitting before any transformation whose parameters are learned from data, then fit those transformations using training data only.

## 🧰 Technology Stack

| Tool or library | Purpose |
|---|---|
| Python | Notebook programming language |
| Jupyter Notebook | Interactive execution environment |
| Pandas | Tabular data loading and manipulation |
| NumPy | Numeric operations and arrays |
| Matplotlib | Plotting and visualization |
| Seaborn | Statistical visual exploration |
| Scikit-learn | Preprocessing, estimators, splitting, tuning, and metrics |
| Statsmodels | OLS regression modelling and statistical summaries |

The actual installed versions are not pinned in the current repository. Create a separate environment and record versions when reproducing results.

## 🗂️ Repository Structure

```text
AI-and-Machine-Learning/
├── *.ipynb                         Four machine-learning notebooks
├── data/
│   └── README.md                   Dataset manifest and placement guide
├── scripts/
│   └── validate_notebooks.py       Notebook structure and syntax validator
├── tests/
│   └── test_repository.py          Repository integrity tests
├── docs/                           Technical documentation and guides
├── .github/
│   ├── ISSUE_TEMPLATE/             Bug and feature request templates
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/ci.yml            Static checks and tests
├── requirements.txt                Runtime dependencies
├── requirements-dev.txt            Development dependencies
├── pytest.ini
├── .editorconfig
├── .gitattributes
├── .gitignore
├── CITATION.cff
├── CODEOWNERS
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── GOVERNANCE.md
├── LICENSE
├── MAINTAINERS.md
├── README.md
├── ROADMAP.md
├── SECURITY.md
└── SUPPORT.md
```

## 📊 Dataset Requirements

The notebooks refer to local CSV files that are not present in the repository tree. Before running a notebook, obtain the relevant dataset from an authorized source and place it where the notebook's relative path expects it, or deliberately update the path in a separate code change.

See [docs/datasets.md](docs/datasets.md) for the expected filenames, provenance requirements, and data-handling guidance.

Do not assume a dataset is included just because a notebook contains `pd.read_csv(...)`.

## 🖥️ Environment Requirements

- Python 3.9 or newer is a practical starting point; actual compatibility depends on library versions.
- Jupyter Notebook or JupyterLab.
- pandas, NumPy, Matplotlib, Seaborn, scikit-learn, and Statsmodels for workflows that import them.
- Enough memory for the selected dataset and model search.
- Access to the source datasets under their applicable terms.

## 🚀 Installation

Create an isolated Python environment:

**Windows PowerShell**
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install jupyter pandas numpy matplotlib seaborn scikit-learn statsmodels
```

The dependency manifest defines compatible version ranges, not a fully locked historical environment. See [docs/reproducibility.md](docs/reproducibility.md).

## ▶️ Run the Notebooks

From the repository root:

```bash
jupyter notebook
```

Then open the notebook you want to study. Alternatively:

```bash
jupyter notebook "Mini project (Naive Bayes Healthcare dataset).ipynb"
```

For reliable execution:
1. Confirm the required CSV is available.
2. Select the correct Python kernel.
3. Restart the kernel.
4. Run cells from top to bottom.
5. Record any warnings or errors.
6. Confirm that results are produced from the current data and code.

## 📏 Model Evaluation

Classification notebooks use metrics including accuracy, precision, recall, F1-score, and classification reports. The regression notebook imports R², mean squared error, and mean absolute error.

Do not compare models using accuracy alone, particularly when the target classes are imbalanced or the cost of false positives and false negatives differs.

For detailed definitions and interpretation, see [docs/evaluation.md](docs/evaluation.md).

## ⚠️ Reproducibility and Data Leakage

Machine-learning results are only meaningful when the data split and preprocessing procedure are sound.

Important checks:
- Split before fitting imputers, scalers, encoders, or feature transformations.
- Fit transformations on training data only.
- Apply the fitted transformation to the test data.
- Use a fixed random seed where supported.
- Use stratification for classification when appropriate.
- Keep test data out of hyperparameter selection.
- Record the dataset source, version, feature definitions, and target.
- Report class counts and confusion matrices where relevant.

The existing notebooks are educational and may not consistently follow all of these practices. Review their cells before interpreting the results as robust estimates.

## 🩺 Healthcare and Responsible AI Notice

The liver and diabetes notebooks use healthcare-related datasets and labels. They are not clinical decision-support systems.

A model trained on a public or educational dataset can be affected by:
- Sampling and selection bias.
- Missing or inaccurate measurements.
- Population differences.
- Class imbalance.
- Label-definition errors.
- Data leakage.
- Outdated or unrepresentative data.
- Poor calibration and threshold choices.

Do not use these notebooks to diagnose, treat, triage, screen, or make decisions about individuals. Do not share identifiable health information. Any real-world clinical use would require extensive independent validation, domain expertise, privacy safeguards, governance, and applicable regulatory review.

## 🔐 Data Privacy and Security

- Never commit personal health information or identifiable records.
- Do not commit API keys, tokens, passwords, or private dataset credentials.
- Review notebook outputs before pushing changes.
- Remove machine-specific absolute paths.
- Confirm dataset licences and redistribution terms.
- Treat downloaded datasets and notebook code as untrusted until reviewed.
- Keep private data out of logs, screenshots, and issue reports.

## 🧯 Troubleshooting

| Problem | What to check |
|---|---|
| CSV file not found | Confirm the dataset filename and notebook working directory |
| Import error | Activate the intended environment and install the missing package |
| Kernel not listed | Register or select the virtual environment kernel |
| Results differ | Restart kernel, check random seeds, data version, and package versions |
| Unexpectedly high test scores | Investigate data leakage, duplicates, target leakage, and split strategy |
| NaN or infinity errors | Inspect transformations and input ranges |
| Grid search is slow | Review the parameter grid, dataset size, and parallel workers |
| Notebook opens but fails | Run cells in order and inspect the first exception |

## 🤝 Contributing

Contributions that improve methodology, clarity, reproducibility, responsible data handling, and documentation are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before changing a notebook.

## 🗺️ Roadmap

See [ROADMAP.md](ROADMAP.md) for proposed improvements, including environment pinning, dataset documentation, notebook validation, leakage prevention, and responsible model evaluation.

## 📖 Documentation

| Document | Description |
|---|---|
| [Documentation index](docs/README.md) | All technical guides |
| [Notebook catalogue](docs/notebook-catalogue.md) | Notebook purpose and model inventory |
| [Datasets](docs/datasets.md) | CSV requirements, provenance, and privacy |
| [Methodology](docs/methodology.md) | Preprocessing and modelling lifecycle |
| [Evaluation](docs/evaluation.md) | Classification and regression metrics |
| [Reproducibility](docs/reproducibility.md) | Environments, versions, seeds, and validation |
| [Responsible AI](docs/responsible-ai.md) | Healthcare, bias, and appropriate use |
| [Installation](docs/installation.md) | Python setup |
| [Development](docs/development.md) | Notebook editing and review |
| [Troubleshooting](docs/troubleshooting.md) | Common notebook problems |
| [FAQ](docs/faq.md) | Common questions |
| [Deployment](docs/deployment.md) | Current deployment boundary |
| [Contributing](CONTRIBUTING.md) | Contribution workflow |
| [Security](SECURITY.md) | Security reporting |
| [Code of Conduct](CODE_OF_CONDUCT.md) | Community expectations |
| [Support](SUPPORT.md) | Help and reporting |
| [Maintainers](MAINTAINERS.md) | Repository maintenance |
| [Governance](GOVERNANCE.md) | Decision process |
| [Changelog](CHANGELOG.md) | Verified changes |

## 📄 License

The repository is distributed under the MIT License. See [LICENSE](LICENSE) for the full text.

---

**Maintained by Brajesh Kumar** · [GitHub](https://github.com/Brajesh31)

Last updated: 2026-11-16 01:59 UTC


## 🧪 Local Validation

Install the notebook environment:

```bash
python -m pip install -r requirements.txt
```

Install development and validation tools:

```bash
python -m pip install -r requirements-dev.txt
```

Validate notebook structure and Python cell syntax without executing the experiments:

```bash
python scripts/validate_notebooks.py
```

Run the repository checks:

```bash
python -m pytest
```

The CI workflow performs structural and static syntax checks. It does not run model training because the required CSV datasets are not distributed with this repository.
