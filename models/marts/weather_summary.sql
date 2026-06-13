select
    city,
    count(*) as number_of_days,
    avg(temperature_max) as avg_temperature,
    max(temperature_max) as highest_temperature
from {{ ref('stg_weather_data') }}
group by city