from pathlib import Path
import pandas as pd
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket
from prefect_gcp import GcpCredentials


@task(retries=3,log_prints=True)
def extract_from_gcs(year: int) -> Path:
    """Download trip data from GCS"""
    gcs_path = f"{year}.parquet"
    gcs_block = GcsBucket.load("airline-dealy")
    gcs_block.get_directory(from_path=gcs_path, local_path=f"./data/parquet/")
    return Path(f"./data/parquet/{gcs_path}")



@task(log_prints=True)
def transform(path: Path) -> pd.DataFrame:   
    """_summary_

    Args:
        path (Path): _description_

    Returns:
        pd.DataFrame: _description_
    """
    df = pd.read_parquet(path)

    return df


@task(log_prints=True)
def write_bq(df: pd.DataFrame) -> None:
    """Write DataFrame to BiqQuery"""

    gcp_credentials_block = GcpCredentials.load("zoom-gcp-cred")

    df.to_gbq(
        destination_table="us_airline_delay.usa_flights_delay",
        project_id="data-engineering-camp-376112",
        credentials=gcp_credentials_block.get_credentials_from_service_account(),
        chunksize=500_000,
        if_exists="append",
    )


@flow()
def etl_gcs_to_bq(year: int) -> None:
    """Main ETL flow to load data into Big Query"""
    # color = "green"
    # year = 2020
    # month = 1

    path = extract_from_gcs(year)
    df = transform(path)
    write_bq(df)


@flow()
def etl_to_bq_parent_flow(
    year: int = 2021
):
    # here
    etl_gcs_to_bq(year)



    
if __name__ == "__main__":
    years = [2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
    # etl_local_to_gcs(2018, "", "csv")
    # years = [2011, ]
    for year in years:
        etl_to_bq_parent_flow(year)