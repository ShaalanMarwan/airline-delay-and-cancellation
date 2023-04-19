{#
    This macro returns the description of the cancellation_code
#}

{% macro get_cancellation_type_description(cancellation_code) -%}

    case {{ cancellation_code }}
        when 'A' then 'Carrier'
        when 'B' then 'Weather'
        when 'C' then 'No charge'
        when 'D' then 'Security'
        when 'nan' then null
        when null then null
    end

{%- endmacro %}