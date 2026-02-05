# Run Instructions – NYC Taxi Batch Pipeline

## Start Infrastructure
cd data-engineering-batch-project
docker compose up -d

## Open MinIO
URL: http://localhost:9001
Username: minioadmin
Password: minioadmin

Create buckets:
- raw-zone
- curated-zone

## Run Ingestion
cd ingestion
python ingest_nyc_taxi.py

## Run Batch Aggregation
cd ingestion
python batch_aggregation_pandas.py

## Upload Curated Output to MinIO
Upload file:
data/curated/nyc_taxi_2018_summary/summary.parquet

Target path in MinIO:
curated-zone/nyc_taxi/year=2018/quarterly_summary/summary.parquet

Schema file:
docker/postgres_schema.sql

DAG file:
airflow/dags/nyc_taxi_batch_dag.py
