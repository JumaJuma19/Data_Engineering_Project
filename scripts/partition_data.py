import pandas as pd
import os

df = pd.read_parquet(r"C:\Users\user\Desktop\Data_eng_Project _file\team_6.parquet")

print("Total rows:", len(df))

# Drop rows with missing year or month
df = df.dropna(subset=["year", "month"])
df["year"]  = df["year"].astype(int)
df["month"] = df["month"].astype(int)

output_path = r"C:\Users\user\Desktop\Data_eng_Project _file\partitioned_data"

df.to_parquet(
    output_path,
    partition_cols=["year", "month"],
    engine="pyarrow",
    index=False
)

print("Partitioning complete. Output:", output_path)
 
