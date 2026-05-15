import pandas as pd

df = pd.read_parquet(r"C:\Users\user\Desktop\Data_eng_Project _file\team_6.parquet")

print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nData types:\n", df.dtypes)
print("\nNull counts:\n", df.isnull().sum())
print("\nFirst 5 rows:\n", df.head())
