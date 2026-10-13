# Architecture

This repository is a collection of independent Jupyter notebooks rather than a deployed application. Each notebook generally loads tabular data, performs preprocessing and exploratory analysis, trains one or more scikit-learn models, and evaluates results.

There is no shared runtime API, database, or service layer. Keep notebook-specific assumptions documented near the relevant workflow and avoid treating healthcare examples as production clinical systems.
