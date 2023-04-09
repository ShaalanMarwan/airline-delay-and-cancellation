{{ config(materilized="table") }}

select iata_code, airport, city, state, country, latitude, longitude
from {{ ref("airports_lookup") }}
