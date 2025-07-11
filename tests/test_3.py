import pytest
import pandas as pd
from definition_2dd2b5906f1d45da880aa130712c24e1 import aggregate_kri_status

@pytest.fixture
def sample_dataframe():
    data = {'Location': ['A', 'A', 'B', 'B'],
            'KRI1_Status': ['Green', 'Amber', 'Red', 'Green'],
            'KRI2_Status': ['Red', 'Green', 'Amber', 'Amber']}
    return pd.DataFrame(data)

def test_aggregate_kri_status_empty_kri_list(sample_dataframe):
    result = aggregate_kri_status(sample_dataframe, [])
    assert result is None # Or whatever the expected behavior is for an empty list

def test_aggregate_kri_status_single_kri(sample_dataframe):
    result = aggregate_kri_status(sample_dataframe.copy(), ['KRI1_Status'])
    assert isinstance(result, pd.DataFrame)
    assert 'KRI1_Status_Green' in result.columns
    assert 'KRI1_Status_Amber' in result.columns
    assert 'KRI1_Status_Red' in result.columns
    assert result['KRI1_Status_Green'].sum() == 2
    assert result['KRI1_Status_Amber'].sum() == 1
    assert result['KRI1_Status_Red'].sum() == 1

def test_aggregate_kri_status_multiple_kris(sample_dataframe):
    result = aggregate_kri_status(sample_dataframe.copy(), ['KRI1_Status', 'KRI2_Status'])
    assert isinstance(result, pd.DataFrame)
    assert 'KRI1_Status_Green' in result.columns
    assert 'KRI1_Status_Amber' in result.columns
    assert 'KRI1_Status_Red' in result.columns
    assert 'KRI2_Status_Green' in result.columns
    assert 'KRI2_Status_Amber' in result.columns
    assert 'KRI2_Status_Red' in result.columns
    assert result['KRI1_Status_Green'].sum() == 2
    assert result['KRI1_Status_Amber'].sum() == 1
    assert result['KRI1_Status_Red'].sum() == 1
    assert result['KRI2_Status_Green'].sum() == 1
    assert result['KRI2_Status_Amber'].sum() == 2
    assert result['KRI2_Status_Red'].sum() == 1

def test_aggregate_kri_status_missing_kri_column(sample_dataframe):
    with pytest.raises(KeyError):
        aggregate_kri_status(sample_dataframe, ['KRI3_Status'])

def test_aggregate_kri_status_non_string_status(sample_dataframe):
    # Create dataframe with non-string KRI statuses
    data = {'Location': ['A', 'A'],
            'KRI1_Status': [1, 2]}
    df = pd.DataFrame(data)

    with pytest.raises(TypeError):
        aggregate_kri_status(df, ['KRI1_Status'])
