from pathlib import Path
from prefect import flow, task
from prefect.tasks import task_input_hash
from prefect_gcp.cloud_storage import GcsBucket
from datetime import timedelta
import pyarrow.csv as pv
import pyarrow.parquet as pq
import pyarrow as pa

# https://www.kaggle.com/datasets/yuanyuwendymu/airline-delay-and-cancellation-data-2009-2018 dataset path

import sys
import pandas as pd
import numpy as np
import pathlib

# sys.path.insert(0,'/Users/yousif/Programming/data-engineering-course/airline-delay-and-cancellation/processing/helper')

# from flights_delay_transformer_module import flights_delay_transformer
# @task()


flights_delay_schema = pa.schema(
    [


        ('FL_DATE', pa.timestamp('s')),
        ('OP_CARRIER', pa.string()),
        ('OP_CARRIER_FL_NUM', pa.int64()),
        ('ORIGIN', pa.string()),
        ('DEST', pa.string()),
        ('CRS_DEP_TIME', pa.int64()),
        ('DEP_TIME', pa.float64()),
        ('DEP_DELAY', pa.float64()),
        ('TAXI_OUT', pa.float64()),
        ('WHEELS_OFF', pa.float64()),
        ('WHEELS_ON', pa.float64()),
        ('TAXI_IN', pa.float64()),
        ('CRS_ARR_TIME', pa.int64()),
        ('ARR_TIME', pa.float64()),
        ('ARR_DELAY', pa.float64()),
        ('CANCELLED', pa.int64()),
        ('CANCELLATION_CODE', pa.string()),
        ('DIVERTED', pa.float64()),
        ('CRS_ELAPSED_TIME', pa.float64()),
        ('ACTUAL_ELAPSED_TIME', pa.float64()),
        ('AIR_TIME', pa.float64()),
        ('DISTANCE', pa.float64()),
        ('CARRIER_DELAY', pa.float64()),
        ('WEATHER_DELAY', pa.float64()),
        ('NAS_DELAY', pa.float64()),
        ('SECURITY_DELAY', pa.float64()),
        ('LATE_AIRCRAFT_DELAY', pa.float64()),
        # ('Unnamed: 27', pa.float64())

    ])
    



@task(retries=3, log_prints=True, cache_key_fn=task_input_hash,refresh_cache=True, cache_expiration=timedelta(days=1))
def clean_airline_data(datasetPath: str) -> pd.DataFrame:
    
    try:
        table = pv.read_csv(datasetPath)
        
        print(table)
        table = table.remove_column(27)
        print(table.schema.names)
        
        table.cast(flights_delay_schema)
        
        
        pq.write_table(table, datasetPath.replace('.csv', '.parquet'))
    except:
        pass
    # pq.write_table(table, datasetPath.replace('./data/csv/*.csv', './data/parquet/*.parquet'))




@task(log_prints=True)
def write_gcs(path: Path) -> None:
    
    gcp_cloud_storage_bucket_block = GcsBucket.load("airline-dealy")
    gcp_cloud_storage_bucket_block.upload_from_path(from_path=path, to_path=path)
    return


@flow()
def etl_local_to_gcs(year: int, fileName: str, dir: str) -> None:
    "The main ETL"
    
    
    dataset_file = f"{fileName}{year}.csv"
    # for local files
    datasetPath = f"./data/{dir}"
    # "../../../data/"

    clean_airline_data(f"{datasetPath}/{dataset_file}")
    
    path = Path(f"data/parquet/{year}.parquet")
    
    write_gcs(path)
    

    # for url path
    # df = fetch(datasetPath)


def flights_delay_transformer(dataset: pd.DataFrame) -> pd.DataFrame:
    """_summary_

    Args:
        dataset (pd.DataFrame): _description_

    Returns:
        pd.DataFrame: _description_
    """

    dataset['CANCELLATION_CODE'] = dataset['CANCELLATION_CODE'].apply(str)
    dataset['CANCELLATION_CODE'].fillna(value=np.nan)

    dataset['FL_DATE'] = dataset['FL_DATE'].apply(pd.Timestamp)

    dataset['ORIGIN'] = dataset['ORIGIN'].apply(str)
    dataset['OP_CARRIER'] = dataset['OP_CARRIER'].apply(str)
    dataset['DEST'] = dataset['DEST'].apply(str)

    dataset['TAXI_OUT'] = dataset['TAXI_OUT'].apply(float)
    dataset = dataset.drop('Unnamed: 27', axis=1)

    return dataset


if __name__ == "__main__":
    years = [2009,2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
    # years = [2012]
    # etl_local_to_gcs(2018, "", "csv")
    # years = [2011, ]
    for year in years:
        etl_local_to_gcs(year, "", "csv")
