# Data Engineering Batch Project – Setup & Run Guide

This repository contains the Phase 2 (Development) and Phase 3 (Finalization)
implementation of a batch-processing data engineering pipeline.

After cloning/downloading the repository, some runtime folders must be created
locally before executing the pipeline.

--------------------------------------------------
STEP 1: CLONE / DOWNLOAD REPOSITORY
--------------------------------------------------

git clone <repository-url>
cd data-engineering-batch-project

--------------------------------------------------
STEP 2: CREATE REQUIRED LOCAL FOLDERS
--------------------------------------------------

Create the following folders inside the project root:

mkdir data
mkdir data/minio
mkdir data/postgres
mkdir data/curated
mkdir screenshots

Place the dataset file in:

data/taxi_trip_data.csv

--------------------------------------------------
STEP 3: START INFRASTRUCTURE SERVICES
--------------------------------------------------

docker compose up -d

--------------------------------------------------
STEP 4: OPEN MINIO CONSOLE
--------------------------------------------------

Open browser:
http://localhost:9001

Login:
Username: minioadmin
Password: minioadmin

Create buckets:
raw-zone
curated-zone

--------------------------------------------------
STEP 5: RUN DATA INGESTION
--------------------------------------------------

cd ingestion
python ingest_nyc_taxi.py

--------------------------------------------------
STEP 6: RUN BATCH AGGREGATION
--------------------------------------------------

cd ingestion
python batch_aggregation_pandas.py

--------------------------------------------------
STEP 7: UPLOAD CURATED OUTPUT TO MINIO
--------------------------------------------------

Upload file from:

data/curated/nyc_taxi_2018_summary/summary.parquet

Upload location in MinIO:

curated-zone/nyc_taxi/year=2018/quarterly_summary/summary.parquet

--------------------------------------------------
STEP 8: SERVING LAYER (DESIGN)
--------------------------------------------------

PostgreSQL schema file:

docker/postgres_schema.sql

--------------------------------------------------
STEP 9: AIRFLOW ORCHESTRATION
--------------------------------------------------

Airflow DAG file:

airflow/dags/nyc_taxi_batch_dag.py
