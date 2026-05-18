import pandas as pd
import psycopg2
import os

try:
    conn = psycopg2.connect(
        database="weather_db",
        user="postgres",
        password="Binmussa@@21",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    print("CONNECTED SUCCESSFULLY")
except Exception as e:
    print(f"CONNECTION FAILED: {e}")
    exit(1)

base_path = r"C:\Users\user\Desktop\Data_eng_Project _file\partitioned_data"

for root, dirs, files in os.walk(base_path):
    for file in files:
        if file.endswith(".parquet"):
            file_path = os.path.join(root, file)
            print(f"LOADING: {file_path}")
            try:
                df = pd.read_parquet(file_path)
                parts = root.split(os.sep)
                year  = int(parts[-2].split("=")[1])
                month = int(parts[-1].split("=")[1])
                df["year"]  = year
                df["month"] = month
                data = list(df.itertuples(index=False, name=None))
                cursor.executemany("""
                    INSERT INTO weather_records (
                        station_id, state, city, station_name,
                        timestamp, datetime, at_c, rh_percent,
                        ws_m_s, wd_deg, rf_mm, tot_rf_mm,
                        sr_w_mt2, bp_mmhg, vws_m_s,
                        pollutant, value, station,
                        day, hour, year, month
                    )
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """, data)
                conn.commit()
                print(f"INSERTED: {file} ({len(data)} rows)")
            except Exception as e:
                print(f"FAILED: {file} - {e}")
                conn.rollback()

cursor.close()
conn.close()
print("ALL DONE")
