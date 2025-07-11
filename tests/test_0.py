import pytest
import pandas as pd
from definition_eb185c8f1565415aac4cf72322aff4b3 import generate_synthetic_data

@pytest.mark.parametrize("duration, num_locations, base_values, volatility, trend_factors, expected_columns", [
    (5, 2, {'trades': 100, 'unreconciled': 5, 'staff': 10}, 0.1, {'trades': 0.01, 'unreconciled': -0.01, 'staff': 0.0}, ['Date', 'Location', 'Volume of Trades per day', 'Number of unreconciled trades > 5 days', 'Staff turnover', 'System outages', 'Number of Back Office Staff']),
    (1, 1, {'trades': 50, 'unreconciled': 2, 'staff': 5}, 0.05, {'trades': 0.0, 'unreconciled': 0.0, 'staff': 0.0}, ['Date', 'Location', 'Volume of Trades per day', 'Number of unreconciled trades > 5 days', 'Staff turnover', 'System outages', 'Number of Back Office Staff']),
    (3, 3, {'trades': 200, 'unreconciled': 10, 'staff': 20}, 0.2, {'trades': -0.02, 'unreconciled': 0.02, 'staff': 0.0}, ['Date', 'Location', 'Volume of Trades per day', 'Number of unreconciled trades > 5 days', 'Staff turnover', 'System outages', 'Number of Back Office Staff'])
])
def test_generate_synthetic_data_valid_input(duration, num_locations, base_values, volatility, trend_factors, expected_columns):
    df = generate_synthetic_data(duration, num_locations, base_values, volatility, trend_factors)
    assert isinstance(df, pd.DataFrame)
    assert set(expected_columns).issubset(df.columns)
    assert len(df) == duration * num_locations

def test_generate_synthetic_data_zero_duration():
    df = generate_synthetic_data(0, 1, {'trades': 100, 'unreconciled': 5, 'staff': 10}, 0.1, {'trades': 0.01, 'unreconciled': -0.01, 'staff': 0.0})
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 0

def test_generate_synthetic_data_negative_duration():
    with pytest.raises(ValueError):
        generate_synthetic_data(-1, 1, {'trades': 100, 'unreconciled': 5, 'staff': 10}, 0.1, {'trades': 0.01, 'unreconciled': -0.01, 'staff': 0.0})

def test_generate_synthetic_data_invalid_base_values_type():
     with pytest.raises(TypeError):
         generate_synthetic_data(5, 2, ['incorrect'], 0.1, {'trades': 0.01, 'unreconciled': -0.01, 'staff': 0.0})
