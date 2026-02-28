from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, count

# Create Spark session (local mode)
spark = SparkSession.builder \
    .appName("NYC Taxi Simple Batch") \
    .master("local[*]") \
    .getOrCreate()

print("Spark session created")

# ABSOLUTE path
input_path = r"D:\Software\data-engineering-batch-project\data\minio\raw-zone\nyc_taxi\year=2018\month=01\taxi_trip_data.parquet"

df = spark.read.parquet(input_path)
print("Data loaded into Spark")
print(f"Total records: {df.count()}")

# Simple aggregation
result = df.agg(
    count("*").alias("total_trips"),
    avg("trip_distance").alias("avg_trip_distance"),
    avg("total_amount").alias("avg_total_amount")
)

result.show()

# Output path (Curated Zone)
output_path = r"D:\Software\data-engineering-batch-project\data\curated\nyc_taxi_2018_summary"

result.write.mode("overwrite").parquet(output_path)

print("Batch aggregation completed")

spark.stop()
