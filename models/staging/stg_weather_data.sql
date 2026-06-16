select
    lower(split_part(filename, '_weather_', 1)) as city,
    value::date as weather_date,
    to_date(regexp_substr(filename, '\\d{4}-\\d{2}-\\d{2}')) as ingestion_date,
    raw_data:daily:temperature_2m_max[index]::float as temperature_max,
    raw_data:daily:temperature_2m_min[index]::float as temperature_min,
    raw_data:daily:precipitation_sum[index]::float as precipitation_sum,
    raw_data:daily:wind_speed_10m_max[index]::float as wind_speed_max
from WEATHER_PIPELINE_DB.RAW.RAW_WEATHER_JSON,
lateral flatten(input => raw_data:daily:time) f
