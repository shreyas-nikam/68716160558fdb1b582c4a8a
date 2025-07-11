import pytest
import pandas as pd
from definition_81adebace4b149788201eb51c0bf769d import calculate_kpis

def test_calculate_kpis_empty_dataframe():
    df = pd.DataFrame()
    result = calculate_kpis(df)
    assert isinstance(result, pd.DataFrame)
    assert result.equals(df)


def test_calculate_kpis_basic_data():
    data = {'Volume of Trades': [100, 200], 
            'Number of unreconciled trades': [10, 20], 
            'Number of Back Office Staff': [5, 10],
            'Number of unreconciled trades > 5 days': [1,2],
            'Staff turnover': [3,4],
            'System outages': [5,6]}
    df = pd.DataFrame(data)
    result = calculate_kpis(df.copy())
    assert 'Unreconciled items as % of volume' in result.columns
    assert 'Volume per staff' in result.columns
    assert result['Unreconciled items as % of volume'][0] == 10.0
    assert result['Volume per staff'][0] == 20.0

def test_calculate_kpis_zero_volume():
    data = {'Volume of Trades': [0, 200], 
            'Number of unreconciled trades': [10, 20], 
            'Number of Back Office Staff': [5, 10],
            'Number of unreconciled trades > 5 days': [1,2],
            'Staff turnover': [3,4],
            'System outages': [5,6]}
    df = pd.DataFrame(data)
    result = calculate_kpis(df.copy())
    assert 'Unreconciled items as % of volume' in result.columns
    assert result['Unreconciled items as % of volume'][0] == 0.0

def test_calculate_kpis_zero_staff():
    data = {'Volume of Trades': [100, 200], 
            'Number of unreconciled trades': [10, 20], 
            'Number of Back Office Staff': [0, 0],
            'Number of unreconciled trades > 5 days': [1,2],
            'Staff turnover': [3,4],
            'System outages': [5,6]}
    df = pd.DataFrame(data)
    result = calculate_kpis(df.copy())
    assert 'Volume per staff' in result.columns
    assert result['Volume per staff'][0] == float('inf')
    assert result['Volume per staff'][1] == float('inf')

def test_calculate_kpis_missing_columns():
    data = {'Volume of Trades': [100, 200], 
            'Number of unreconciled trades': [10, 20]}
    df = pd.DataFrame(data)
    with pytest.raises(KeyError):
        calculate_kpis(df.copy())
