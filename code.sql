-- Create weather_records table
CREATE TABLE IF NOT EXISTS weather_records (
    id            SERIAL PRIMARY KEY,
    station_id    VARCHAR(50),
    state         VARCHAR(100),
    city          VARCHAR(100),
    station_name  VARCHAR(200),
    timestamp     BIGINT,
    datetime      TIMESTAMP,
    at_c          FLOAT,
    rh_percent    FLOAT,
    ws_m_s        FLOAT,
    wd_deg        FLOAT,
    rf_mm         FLOAT,
    tot_rf_mm     FLOAT,
    sr_w_mt2      FLOAT,
    bp_mmhg       FLOAT,
    vws_m_s       FLOAT,
    pollutant     VARCHAR(50),
    value         FLOAT,
    station       VARCHAR(200),
    day           INTEGER,
    hour          INTEGER,
    year          INTEGER,
    month         INTEGER
);

-- Indexes for performance
CREATE INDEX idx_year_month ON weather_records (year, month);
CREATE INDEX idx_city       ON weather_records (city);
CREATE INDEX idx_pollutant  ON weather_records (pollutant);

-- Count total rows
SELECT COUNT(*) AS total_rows FROM weather_records;

-- Average temperature by city
SELECT city, ROUND(AVG(at_c)::numeric, 2) AS avg_temp_c
FROM weather_records
WHERE at_c IS NOT NULL
GROUP BY city
ORDER BY avg_temp_c DESC;

-- Most common pollutants
SELECT pollutant, COUNT(*) AS occurrences
FROM weather_records
WHERE pollutant IS NOT NULL
GROUP BY pollutant
ORDER BY occurrences DESC;
