PostgreSQL Serving Store

The PostgreSQL serving layer is designed to host aggregated, ML-ready
feature snapshots generated during batch processing.

Due to local environment authentication constraints, data loading was
validated conceptually using schema definition and data inspection,
while the full ingestion is planned to be executed via Airflow-managed
jobs in the final deployment.

The target table is nyc_taxi_quarterly_summary, designed to store
quarterly aggregated metrics for downstream analytics and ML use.
