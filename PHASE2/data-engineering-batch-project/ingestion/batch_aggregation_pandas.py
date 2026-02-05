import pandas as pd
from pathlib import Path

print("Starting batch aggregation using Pandas (CSV source)")

input_path = r"D:\Software\data-engineering-batch-project\data\taxi_trip_data.csv"

df = pd.read_csv(input_path)
print(f"Loaded {len(df)} rows")

# Parse datetime and filter year 2018
df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"], errors="coerce")
df_2018 = df[df["pickup_datetime"].dt.year == 2018]

print(f"2018 records: {len(df_2018)}")

total_trips = len(df_2018)
avg_trip_distance = df_2018["trip_distance"].mean()
avg_total_amount = df_2018["total_amount"].mean()

summary_df = pd.DataFrame([{
    "total_trips": total_trips,
    "avg_trip_distance": avg_trip_distance,
    "avg_total_amount": avg_total_amount
}])

print(summary_df)

# Write to Curated Zone
output_dir = Path(r"D:\Software\data-engineering-batch-project\data\curated\nyc_taxi_2018_summary")
output_dir.mkdir(parents=True, exist_ok=True)

output_path = output_dir / "summary.parquet"
summary_df.to_parquet(output_path, index=False)

print("Batch aggregation completed and written to Curated Zone")
