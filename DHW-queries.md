CREATE TABLE `data-engineering-camp-376112.us_airline_delay.flights_delay_partitioned`
PARTITION BY FL_DATE
CLUSTER BY OP_CARRIER, ORIGIN, DEST
OPTIONS(
  expiration_timestamp=TIMESTAMP_ADD(CURRENT_TIMESTAMP(), INTERVAL 30 DAY),
  description='My partitioned and clustered table'
) AS
SELECT *
FROM `data-engineering-camp-376112.us_airline_delay.flights_delay`;


CREATE TABLE `data-engineering-camp-376112.us_airline_delay.flights_delay_clustered`
PARTITION BY FL_DATE
CLUSTER BY OP_CARRIER
OPTIONS(
  expiration_timestamp=TIMESTAMP_ADD(CURRENT_TIMESTAMP(), INTERVAL 30 DAY),
  description='My partitioned and clustered table'
) AS
SELECT *
FROM `data-engineering-camp-376112.us_airline_delay.flights_delay_partitioned`;
