{#
    This macro returns the description of the cancellation_code
#}

{% macro get_cancellation_type_description(cancellation_code) -%}

    case {{ cancellation_code }}
        when 'A' then 'Carrier'
        when 'B' then 'Cash'
        when 'C' then 'No charge'
        when 'D' then 'Dispute'
        when 'nan' then 'Unknown'
        when null then 'Unknown'
    end

{%- endmacro %}