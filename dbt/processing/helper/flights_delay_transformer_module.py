import pandas as pd
import numpy as np


def flights_delay_transformer(dataset: pd.DataFrame) -> pd.DataFrame:

    dataset['CANCELLATION_CODE'] = dataset['CANCELLATION_CODE'].apply(str)
    dataset['CANCELLATION_CODE'].fillna()

    dataset['FL_DATE'] = dataset['FL_DATE'].apply(pd.Timestamp)

    dataset['ORIGIN'] = dataset['ORIGIN'].apply(str)
    dataset['OP_CARRIER'] = dataset['OP_CARRIER'].apply(str)
    dataset['DEST'] = dataset['DEST'].apply(str)

    dataset['TAXI_OUT'] = dataset['TAXI_OUT'].apply(float)
    dataset = dataset.drop('Unnamed: 27', axis=1)

    return dataset