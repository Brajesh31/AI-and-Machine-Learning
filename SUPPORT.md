# 🧭 Support Guide

This guide helps learners resolve common notebook and environment problems and prepare useful reports when something fails.

## Start here

- [README](README.md): project overview and setup.
- [Notebook catalogue](docs/notebook-catalogue.md): notebook-specific context.
- [Datasets](docs/datasets.md): required CSV files and provenance.
- [Installation](docs/installation.md): Python environment.
- [Troubleshooting](docs/troubleshooting.md): common errors.
- [Reproducibility](docs/reproducibility.md): versions and execution.

## Choose the right channel

| Need | Recommended route |
|---|---|
| Notebook execution failure | Bug report with notebook and cell details |
| Missing dataset | Check dataset guide and source terms |
| Methodology concern | Issue describing the leakage or evaluation question |
| Documentation correction | Focused issue or pull request |
| Feature proposal | Issue describing the learning objective |
| Security concern | Private reporting under SECURITY.md |

## Information to include

- Notebook filename.
- Python and Jupyter versions.
- Operating system.
- Relevant package versions.
- Dataset source and version, if public.
- Cell number or command.
- Complete sanitized traceback.
- Expected and observed behaviour.
- Whether the notebook was run from a clean kernel.

## Privacy

Never upload patient records, private datasets, credentials, or identifiable health information. Use synthetic examples and redact sensitive output.

## Support boundaries

This is an educational notebook repository. It does not provide clinical advice, a production inference service, or guaranteed response times.
