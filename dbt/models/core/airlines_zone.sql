{{ config(materilized="table") }}

select iata_code, airline
from {{ ref("airlines_lookup") }}
