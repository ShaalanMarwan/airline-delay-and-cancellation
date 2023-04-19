{{ config(materilized="table", sort='timestamp') }}


with
    flights_data as (select * from {{ ref("stg_flightdata") }}),

    airlines_zone as (select * from {{ ref("airlines_zone") }}),

    airports_zone as (select * from {{ ref("airports_zone") }})

-- select
--     flights_data.fl_date,
--     flights_data.op_carrier,
--     flights_data.op_carrier_fl_num,
--     flights_data.origin,
--     flights_data.dest,
--     flights_data.crs_dep_time,
--     flights_data.dep_time,
--     flights_data.dep_delay,
--     flights_data.taxi_out,
--     flights_data.wheels_off,
--     flights_data.wheels_on,
--     flights_data.taxi_in,
--     flights_data.crs_arr_time,
--     flights_data.arr_time,
--     flights_data.arr_delay,
--     flights_data.cancelled,
--     flights_data.cancellation_code_description,
--     flights_data.diverted,
--     flights_data.crs_elapsed_time,
--     flights_data.actual_elapsed_time,
--     flights_data.air_time,
--     flights_data.distance,
--     flights_data.carrier_delay,
--     flights_data.weather_delay,
--     flights_data.nas_delay,
--     flights_data.security_delay
--     airports_zone."AIRPORT",
--     airports_zone."CITY",
--     airports_zone."STATE",
--     airports_zone."COUNTRY",
--     airports_zone."LATITUDE",
--     airports_zone."LONGITUDE",
--     airlines_zone."AIRLINE"
-- from flights_data
-- left join airports_zone on flights_data.origin = airports_zone."IATA_CODE"
-- left join airlines_zone on flights_data.op_carrier = airlines_zone."IATA_CODE"

SELECT
    flights_data.fl_date,
    flights_data.op_carrier,
    flights_data.op_carrier_fl_num,
    flights_data.origin,
    flights_data.dest,
    flights_data.crs_dep_time,
    flights_data.dep_time,
    flights_data.dep_delay,
    flights_data.taxi_out,
    flights_data.wheels_off,
    flights_data.wheels_on,
    flights_data.taxi_in,
    flights_data.crs_arr_time,
    flights_data.arr_time,
    flights_data.arr_delay,
    flights_data.cancelled,
    flights_data.cancellation_code_description,
    flights_data.diverted,
    flights_data.crs_elapsed_time,
    flights_data.actual_elapsed_time,
    flights_data.air_time,
    flights_data.distance,
    flights_data.carrier_delay,
    flights_data.weather_delay,
    flights_data.nas_delay,
    flights_data.security_delay,
    airports_zone.AIRPORT,
    airports_zone.CITY,
    airports_zone.STATE,
    airports_zone.COUNTRY,
    airports_zone.LATITUDE,
    airports_zone.LONGITUDE,
    airlines_zone.AIRLINE
FROM flights_data
LEFT JOIN airports_zone ON flights_data.origin = airports_zone.IATA_CODE
LEFT JOIN airlines_zone ON flights_data.op_carrier = airlines_zone.IATA_CODE
