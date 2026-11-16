# 🗄️ Data Storage and Database Scope

The current repository does not define a database. Data is loaded from local CSV files and stored in memory as Pandas DataFrames and NumPy arrays during notebook execution.

## Current data lifecycle

1. The learner obtains the required dataset from an authorized source.
2. A notebook reads the CSV using Pandas.
3. DataFrame objects hold loaded and transformed data.
4. Train/test arrays are created for modelling.
5. Estimators and metrics exist in the active kernel.
6. State disappears when the kernel is shut down unless the notebook output or an explicit file save is retained.

## No persistence service

There is no SQL database, document database, object store, data warehouse, or model registry in the repository.

## Data safety

Do not commit private or restricted datasets. Follow the source licence and record provenance. Healthcare datasets and notebook outputs require special care because de-identification does not eliminate all privacy risk.

## Future storage changes

A future data layer would require a justified use case, documented schema, access control, retention policy, backup and deletion procedures, and security review. It should not be introduced simply to run the current notebooks.
