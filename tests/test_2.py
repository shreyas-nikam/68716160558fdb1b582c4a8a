import pytest
import pandas as pd
from definition_d189378a329a4090a8a1b8d16abf5363 import assign_kri_status


def test_assign_kri_status_basic():
    data = {'kri_value': [10, 20, 30, 40]}
    df = pd.DataFrame(data)
    result_df = assign_kri_status(df.copy(), 'kri_value', 15, 35)
    assert 'kri_value_status' in result_df.columns
    assert list(result_df['kri_value_status']) == ['Green', 'Amber', 'Amber', 'Red']


def test_assign_kri_status_edge_cases():
    data = {'kri_value': [15, 35]}
    df = pd.DataFrame(data)
    result_df = assign_kri_status(df.copy(), 'kri_value', 15, 35)
    assert list(result_df['kri_value_status']) == ['Green', 'Amber']
    
    result_df2 = assign_kri_status(df.copy(), 'kri_value', 14, 34)
    assert list(result_df2['kri_value_status']) == ['Amber', 'Red']


def test_assign_kri_status_empty_dataframe():
    df = pd.DataFrame()
    result_df = assign_kri_status(df.copy(), 'kri_value', 15, 35)
    assert 'kri_value_status' in result_df.columns
    assert len(result_df) == 0

def test_assign_kri_status_different_thresholds():
    data = {'kri_value': [5, 15, 25, 35, 45]}
    df = pd.DataFrame(data)
    result_df = assign_kri_status(df.copy(), 'kri_value', 10, 20)
    assert list(result_df['kri_value_status']) == ['Green', 'Amber', 'Red', 'Red', 'Red']

def test_assign_kri_status_negative_values():
    data = {'kri_value': [-10, -5, 0, 5]}
    df = pd.DataFrame(data)
    result_df = assign_kri_status(df.copy(), 'kri_value', 0, 5)
    assert list(result_df['kri_value_status']) == ['Green', 'Green', 'Green', 'Amber']
