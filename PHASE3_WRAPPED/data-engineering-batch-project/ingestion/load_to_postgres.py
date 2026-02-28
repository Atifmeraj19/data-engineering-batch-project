import pandas as pd
from sqlalchemy import create_engine

print("Starting load to Postgres")

# Load curated Parquet
parquet_path = r"D:\Software\data-engineering-batch-project\data\curated\nyc_taxi_2018_summary\summary.parquet"
df = pd.read_parquet(parquet_path)

print("Loaded curated data:")
print(df)

# Postgres connection
engine = create_engine(
    "postgresql+psycopg2://taxi_user:taxi_pass@localhost:5432/taxi_db"
)

# Load into Postgres
table_name = "nyc_taxi_quarterly_summary"

df.to_sql(
    table_name,
    engine,
    if_exists="replace",
    index=False
)

print("Data successfully loaded into Postgres table:", table_name)
