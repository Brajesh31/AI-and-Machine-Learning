# 🔐 Security Policy

This repository contains Jupyter notebooks for educational data analysis and machine learning. Notebooks may execute arbitrary Python code, read local files, access the network, and display saved outputs. Review notebooks before running them.

## 📚 Table of Contents

- [Scope](#-scope)
- [Reporting a vulnerability](#-reporting-a-vulnerability)
- [Safe notebook execution](#-safe-notebook-execution)
- [Sensitive data](#-sensitive-data)
- [Dataset safety](#-dataset-safety)
- [Dependency security](#-dependency-security)
- [Notebook outputs and metadata](#-notebook-outputs-and-metadata)
- [Incident response](#-incident-response)

## 🎯 Scope

This policy applies to notebooks, documentation, configuration, dependencies, datasets added to the repository, and GitHub Actions workflows.

The repository does not currently expose an API or production model-serving service.

## 🚨 Reporting a vulnerability

Use GitHub's private vulnerability reporting feature when available:

https://github.com/Brajesh31/AI-and-Machine-Learning/security/advisories/new

If private reporting is not enabled, contact the repository owner privately through GitHub. Do not publish exploit details, private records, or access tokens in a public issue.

A useful report includes the affected file, commit, environment, reproduction steps, impact, and sanitized evidence.

## 🧪 Safe notebook execution

- Inspect code cells before executing an unfamiliar notebook.
- Run notebooks in an isolated virtual environment.
- Avoid executing notebooks from untrusted sources with access to sensitive local files.
- Review shell commands, file operations, downloads, and network calls.
- Do not use production credentials in educational notebooks.

## 🔒 Sensitive data

Never commit:
- Identifiable patient or health records.
- Personal names, contact information, or account identifiers.
- Passwords, tokens, API keys, and private credentials.
- Restricted datasets or private exports.
- Notebook outputs containing confidential data.

If a secret is exposed, revoke it at the issuing service. Removing it from the latest commit does not make it safe.

## 📊 Dataset safety

Verify data provenance, licence, permitted use, and redistribution terms. Treat downloaded archives and data files as untrusted inputs. Avoid running untrusted serialized model files such as pickle or joblib artifacts.

## 📦 Dependency security

Use isolated environments. Review package sources and advisories before installing or upgrading dependencies. The repository does not currently pin exact Python dependency versions.

## 🧾 Notebook outputs and metadata

Review saved outputs, cell metadata, execution history, and embedded images before committing. Clear output that exposes private information or makes stale results appear current.

## 🚑 Incident response

Maintainers should contain the exposure, revoke credentials where applicable, remove sensitive data from active files, assess repository history and access, and communicate remediation appropriately.
