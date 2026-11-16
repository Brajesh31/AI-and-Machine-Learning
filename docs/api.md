# 🔌 API Scope

This repository does not currently expose a web API, REST endpoint, GraphQL endpoint, or network inference service.

The notebooks are interactive research artifacts executed in a Jupyter kernel. They load CSV files, transform data, fit estimators, and print or plot results in notebook cells.

## Current interfaces

- Notebook cells are the main user interface.
- Local filesystem paths are used to load input data.
- Python objects hold models and intermediate data during a kernel session.
- Notebook outputs display metrics, tables, and visualizations.

## What is not implemented

There is no authentication layer, HTTP server, request schema, API versioning, rate limiting, model-serving process, or hosted prediction endpoint.

## Future API work

Before exposing a model, extract the fitted preprocessing and estimator pipeline, define and validate an input schema, version the model and data, add tests and monitoring, and conduct privacy and security review. Healthcare predictions require additional domain validation and governance.
