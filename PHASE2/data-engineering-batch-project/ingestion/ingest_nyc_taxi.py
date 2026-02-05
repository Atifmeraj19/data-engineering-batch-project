import pandas as pd
import boto3
from io import BytesIO

# MinIO configuration
MINIO_ENDPOINT = "http://localhost:9000"
MINIO_ACCESS_KEY = "minioadmin"
MINIO_SECRET_KEY = "minioadmin"
BUCKET_NAME = "raw-zone"

CSV_KEY = "nyc_taxi/year=2018/month=01/taxi_trip_data.csv"
PARQUET_KEY = "nyc_taxi/year=2018/month=01/taxi_trip_data.parquet"

REQUIRED_COLUMNS = [
    "pickup_datetime",
    "dropoff_datetime",
    "trip_distance",
    "total_amount"
]


def main():
    print("Starting ingestion job...")

    df = pd.read_csv("../data/taxi_trip_data.csv")
    print(f"Loaded dataset with {len(df)} rows")

    # Validate schema
    missing_cols = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")

    df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"], errors="coerce")
    df_2018 = df[df["pickup_datetime"].dt.year == 2018]
    print(f"Rows after year filter: {len(df_2018)}")

    before = len(df_2018)
    df_2018 = df_2018.dropna(subset=REQUIRED_COLUMNS)
    after = len(df_2018)

    print(f"Dropped {before - after} invalid rows")
    print(f"Final valid rows: {after}")

    # Connect to MinIO
    s3 = boto3.client(
        "s3",
        endpoint_url=MINIO_ENDPOINT,
        aws_access_key_id=MINIO_ACCESS_KEY,
        aws_secret_access_key=MINIO_SECRET_KEY,
    )

    # Upload CSV
    csv_buffer = BytesIO()
    df_2018.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=CSV_KEY,
        Body=csv_buffer.getvalue(),
    )

    # Upload Parquet
    parquet_buffer = BytesIO()
    df_2018.to_parquet(parquet_buffer, index=False)
    parquet_buffer.seek(0)

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=PARQUET_KEY,
        Body=parquet_buffer.getvalue(),
    )

    print("CSV and Parquet successfully uploaded to MinIO.")


if __name__ == "__main__":
    main()
