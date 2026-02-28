from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Dummy task functions
def monthly_ingestion():
    print("Monthly ingestion task executed")

def quarterly_batch_processing():
    print("Quarterly batch processing task executed")

# Define DAG
with DAG(
    dag_id="nyc_taxi_batch_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["batch", "nyc_taxi"]
) as dag:

    ingestion_task = PythonOperator(
        task_id="monthly_ingestion",
        python_callable=monthly_ingestion
    )

    batch_task = PythonOperator(
        task_id="quarterly_batch_processing",
        python_callable=quarterly_batch_processing
    )

    ingestion_task >> batch_task
