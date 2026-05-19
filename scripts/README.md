# Data Engineering Project — Team 6

## Project Overview
End-to-end ETL pipeline for a large-scale weather and air quality dataset (~4.6M rows) stored in Parquet format, loaded into PostgreSQL.

## Technologies
- Python, Pandas, PyArrow
- PostgreSQL
- Git

## Team Members

| Name    | Student ID | Role                              |
|---------|------------|-----------------------------------|
| Juma    | zda24b021  | Dataset exploration, ETL pipeline |
| Ali     | zda24b023  | Database schema, SQL queries      |
| Ibrahim | zda24b035  | Data partitioning, documentation  |

## How to Run

1. Install dependencies:
   ```
   pip install pandas psycopg2 pyarrow
   ```
2. Create the table: run `code.sql` in PostgreSQL
3. Partition the data: `python scripts/partition_data.py`
4. Load into DB: `python scripts/load_data.py`
