# ❓ Frequently Asked Questions

## Are the datasets included?

No. The repository contains four notebooks. The CSV files referenced in code, including `liver_cirrhosis.csv`, `diabetes.csv`, and `Cryptocurrency_FeaturedData.csv`, are not in the current repository tree.

## Is this a production ML platform?

No. It is a set of independent educational notebooks.

## Do I need Node.js or npm?

No. The project uses Python and Jupyter. Create a Python virtual environment and install the notebook dependencies.

## Why does a notebook say a file is missing?

The CSV must be obtained separately from an authorized source and placed at the path used by the notebook. Start Jupyter from the repository root.

## Are the healthcare predictions reliable medical advice?

No. They are educational model outputs and have not been established as clinically valid.

## Why do model results change?

Data version, package version, random seed, split, execution order, and preprocessing can all affect results.

## Can I deploy the trained models?

The notebooks do not provide production-ready inference code. A deployment would require an extracted, tested preprocessing pipeline, versioned data/model, input validation, monitoring, privacy, and access controls.

## Is there a pinned requirements file?

Not currently. The installation guide lists common dependencies, but exact versions are not locked.
