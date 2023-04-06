import pandas as pd
import numpy as np
import pytest

from flights_delay_transformer import flights_delay_transformer


@pytest.fixture
def sample_dataset():
    # Create a sample dataset with some missing values and incorrect types
    return pd.DataFrame({
        'FL_DATE': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04'],
        'ORIGIN': ['LHR', 'LGW', 'STN', np.nan],
        'DEST': ['JFK', 'LAX', np.nan, 'SFO'],
        'OP_CARRIER': [123, 'AA', 'DL', 'UA'],
        'TAXI_OUT': ['10.5', '20.0', '30.0', ''],
        'CANCELLATION_CODE': ['A', 'B', np.nan, np.nan],
        'Unnamed: 27': [1, 2, 3, 4]
    })


def test_flights_delay_transformer(sample_dataset):
    # Apply the transformation to the sample dataset
    transformed_dataset = flights_delay_transformer(sample_dataset)

    # Check that the transformed dataset has the expected data types and values
    assert isinstance(transformed_dataset['FL_DATE'][0], pd.Timestamp)
    assert transformed_dataset['ORIGIN'].dtype == 'object'
    assert transformed_dataset['OP_CARRIER'].dtype == 'object'
    assert transformed_dataset['DEST'].dtype == 'object'
    assert transformed_dataset['TAXI_OUT'].dtype == 'float64'
    assert 'Unnamed: 27' not in transformed_dataset.columns
    assert transformed_dataset['CANCELLATION_CODE'].isnull().all()

# import pandas as pd
# import numpy as np
# import pytest

# from flights_delay_transformer import flights_delay_transformer


# def test_flights_delay_transformer():

#     # create test dataset
#     df = pd.DataFrame({
#         'CANCELLATION_CODE': ['A', np.nan, 'B'],
#         'FL_DATE': ['2022-01-01', '2022-01-02', '2022-01-03'],
#         'ORIGIN': ['JFK', 'LAX', 'ORD'],
#         'OP_CARRIER': ['AA', 'DL', 'UA'],
#         'DEST': ['LAX', 'JFK', 'SFO'],
#         'TAXI_OUT': ['10.5', '15.2', '20.0'],
#         'Unnamed: 27': [''],
#     })

#     # expected output
#     expected = pd.DataFrame({
#         'CANCELLATION_CODE': ['A', 'nan', 'B'],
#         'FL_DATE': [pd.Timestamp('2022-01-01'), pd.Timestamp('2022-01-02'), pd.Timestamp('2022-01-03')],
#         'ORIGIN': ['JFK', 'LAX', 'ORD'],
#         'OP_CARRIER': ['AA', 'DL', 'UA'],
#         'DEST': ['LAX', 'JFK', 'SFO'],
#         'TAXI_OUT': [10.5, 15.2, 20.0],
#     })

#     # apply transformer function
#     result = flights_delay_transformer(df)

#     # check if result matches expected output
#     pd.testing.assert_frame_equal(result, expected)