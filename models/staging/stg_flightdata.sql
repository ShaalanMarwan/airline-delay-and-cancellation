{{ config(materialized="view") }}


-- select * from us_airline_delay.flights_delay
select
    -- identifiers 
    cast(fl_date as date) as fl_date,
    cast(op_carrier as string) as op_carrier,
    cast(op_carrier_fl_num as integer) as op_carrier_fl_num,
    cast(origin as string) as origin,
    cast(dest as string) as dest,
    cast(crs_dep_time as integer) as crs_dep_time,
    cast(dep_time as float) as dep_time,
    cast(dep_delay as float) as dep_delay,
    cast(taxi_out as float) as taxi_out,
    cast(wheels_off as float) as wheels_off,
    cast(wheels_on as float) as wheels_on,
    cast(taxi_in as float) as taxi_in,
    cast(crs_arr_time as integer) as crs_arr_time,
    cast(arr_time as float) as arr_time,
    cast(arr_delay as float) as arr_delay,
    cast(cancelled as float) as cancelled,
    cast(cancellation_code as string) as cancellation_code,
    cast(diverted as float) as diverted,
    cast(crs_elapsed_time as float) as crs_elapsed_time,
    cast(actual_elapsed_time as float) as actual_elapsed_time,
    cast(air_time as float) as air_time,
    cast(distance as float) as distance,
    cast(carrier_delay as float) as carrier_delay,
    cast(weather_delay as float) as weather_delay,
    cast(nas_delay as float) as nas_delay,
    cast(security_delay as float) as security_delay

from
    {{ source("staging", "flights_delay") }}
    -- from 'flights_delay'
    
