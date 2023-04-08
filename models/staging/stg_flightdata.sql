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
    cast(dep_time as numeric) as dep_time,
    cast(dep_delay as numeric) as dep_delay,
    cast(taxi_out as numeric) as taxi_out,
    cast(wheels_off as numeric) as wheels_off,
    cast(wheels_on as numeric) as wheels_on,
    cast(taxi_in as numeric) as taxi_in,
    cast(crs_arr_time as integer) as crs_arr_time,
    cast(arr_time as numeric) as arr_time,
    cast(arr_delay as numeric) as arr_delay,
    cast(cancelled as numeric) as cancelled,
    {{ get_cancellation_type_description("cancellation_code") }}
    as cancellation_code_description,
    cast(diverted as numeric) as diverted,
    cast(crs_elapsed_time as numeric) as crs_elapsed_time,
    cast(actual_elapsed_time as numeric) as actual_elapsed_time,
    cast(air_time as numeric) as air_time,
    cast(distance as numeric) as distance,
    cast(carrier_delay as numeric) as carrier_delay,
    cast(weather_delay as numeric) as weather_delay,
    cast(nas_delay as numeric) as nas_delay,
    cast(security_delay as numeric) as security_delay

from {{ source("staging", "flights_delay") }}
-- from 'flights_delay'
{% if var("is_test_run", default=true) %} limit 100 {% endif %}
