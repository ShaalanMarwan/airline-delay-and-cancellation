
# Analytics of Airline Delays of US Airports
- [Analytics of Airline Delays of US Airports](#analytics-of-airline-delays-of-us-airports)
  - [Preface](#preface)
  - [Introduction](#introduction)
  - [Dataset Description](#dataset-description)
- [Setup](#setup)
- [Goals](#goals)


## Preface 
Air travel has become an integral part of our lives, whether it's for business or leisure. However, airline delays and cancellations are an unfortunate reality that passengers often face. These issues can cause significant inconvenience, financial loss, and frustration for travelers. Therefore, airlines and airports need to be proactive in addressing these issues and providing the necessary information and support to their customers.

## Introduction
The Airline delays and cancellations in USA between 2009 and 2018 datasets contain 28 columns and for the process we should clean the data and implement the following:


- Extract the data 
- Exploring the data to have better knowledge about the columns 
- Clean the data (depend on your way of implementation Like Delete NaN rows , find Mean of number etc)
- find the right types of the data
- Terraform setup (IaC) with database schema(optional)
- Data ingestion :
  - Batch/Workflow orchestration (Airflow, Prefect, etc)
  - Steam (Kafka , Pulsar)
- Data warehouse: Tables are partitioned and clustered 
- Transformations: (dbt, spark, etc)
- Dashboard : Google dashboard or Metabase


***

## Dataset Description

https://cloud.getdbt.com/accounts/148444/runs/138771363/docs/#!/overview

There are two types of data in the dataset - zipped csv files.

```python
    Index(['FL_DATE', 'OP_CARRIER', 'OP_CARRIER_FL_NUM', 'ORIGIN', 'DEST',
       'CRS_DEP_TIME', 'DEP_TIME', 'DEP_DELAY', 'TAXI_OUT', 'WHEELS_OFF',
       'WHEELS_ON', 'TAXI_IN', 'CRS_ARR_TIME', 'ARR_TIME', 'ARR_DELAY',
       'CANCELLED', 'CANCELLATION_CODE', 'DIVERTED', 'CRS_ELAPSED_TIME',
       'ACTUAL_ELAPSED_TIME', 'AIR_TIME', 'DISTANCE', 'CARRIER_DELAY',
       'WEATHER_DELAY', 'NAS_DELAY', 'SECURITY_DELAY', 'LATE_AIRCRAFT_DELAY',
       'Unnamed: 27'],


'FL_DATE': The flight date.

'OP_CARRIER': The airline carrier code.
'OP_CARRIER_FL_NUM': The flight number for that airline carrier.

'ORIGIN': The airport code for the origin airport.

'DEST': The airport code for the destination airport.

'CRS_DEP_TIME': The scheduled departure time.

'DEP_TIME': The actual departure time.
'DEP_DELAY': The difference in minutes between the scheduled and actual departure time.

'TAXI_OUT': The amount of time in minutes it took for the plane to taxi from the gate to the runway.
'WHEELS_OFF': The actual time when the plane left the gate.
'CRS_ELAPSED_TIME': The scheduled flight time in minutes.
'ACTUAL_ELAPSED_TIME': The actual flight time in minutes.
'AIR_TIME': The amount of time in minutes that the plane was in the air.

'DISTANCE': The distance between the origin and destination airports in miles.

'CARRIER_DELAY': The amount of time in minutes that the delay was due to the airline.
'WEATHER_DELAY': The amount of time in minutes that the delay was due to weather.
'NAS_DELAY': The amount of time in minutes that the delay was due to the National Airspace System.
'SECURITY_DELAY': The amount of time in minutes that the delay was due to security issues.
'LATE_AIRCRAFT_DELAY': The amount of time in minutes that the delay was due to a previous flight using the same aircraft arriving late.
```

***
# Setup
```
.Repo
├── config.yml
├── code
│   ├── data-EDA.ipynb
│   └── on-simplicity-in-technology.markdown
├── data
│   ├── csv 
│   │    ├── 2009.csv
│   │    ├── 2010.csv
│   │    ├── 2011.csv
│   │    ├── 2012.csv
│   │    ├── 2013.csv
│   │    ├── 2014.csv
│   │    ├── 2015.csv
│   │    ├── 2016.csv
│   │    ├── 2017.csv
│   │    ├── 2018.csv
│   └── post.html
│   └── header.html
├── terraform
│   ├── main.tf
│   └── terraform.tfstate
│   └── variables.tf
└── readme.md

```

***
# Goals 
1- Reading Data 

2- Terraform Setup 

3- Prefect flow

4- DBT 

5- Spark or Kafka 

