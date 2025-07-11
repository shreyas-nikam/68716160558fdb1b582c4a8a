import pandas as pd
import numpy as np

def generate_synthetic_data(duration, num_locations, base_values, volatility, trend_factors):
    """Generates synthetic time-series data for operational metrics."""

    if duration < 0:
        raise ValueError("Duration must be non-negative.")
    if not isinstance(base_values, dict):
        raise TypeError("Base values must be a dictionary.")

    dates = pd.date_range(start='2023-01-01', periods=duration)
    data = []

    for location in range(num_locations):
        for date in dates:
            trades = base_values['trades'] * (1 + np.random.normal(0, volatility) + trend_factors['trades'] * (date - dates[0]).days)
            unreconciled = base_values['unreconciled'] * (1 + np.random.normal(0, volatility) + trend_factors['unreconciled'] * (date - dates[0]).days)
            staff = base_values['staff'] * (1 + np.random.normal(0, volatility) + trend_factors['staff'] * (date - dates[0]).days)

            trades = max(0, int(trades))
            unreconciled = max(0, int(unreconciled))
            staff = max(0, int(staff))

            data.append({
                'Date': date,
                'Location': f'Location {location + 1}',
                'Volume of Trades per day': trades,
                'Number of unreconciled trades > 5 days': unreconciled,
                'Staff turnover': staff,
                'System outages': np.random.randint(0, 2),
                'Number of Back Office Staff': staff * 5 
            })

    df = pd.DataFrame(data)
    return df

import pandas as pd

def calculate_kpis(dataframe):
    """Computes KRI values from the input DataFrame."""

    if dataframe.empty:
        return dataframe

    try:
        dataframe['Unreconciled items as % of volume'] = (dataframe['Number of unreconciled trades'] / dataframe['Volume of Trades']) * 100
        dataframe['Unreconciled items as % of volume'] = dataframe['Unreconciled items as % of volume'].fillna(0)
        dataframe['Unreconciled items as % of volume'] = dataframe['Unreconciled items as % of volume'].replace([float('inf'), float('nan')], 0)
        dataframe['Volume per staff'] = dataframe['Volume of Trades'] / dataframe['Number of Back Office Staff']
        dataframe['Volume per staff'] = dataframe['Volume per staff'].replace(0, float('inf'))

    except KeyError as e:
        raise KeyError(e)
    except ZeroDivisionError:
        pass

    return dataframe

import pandas as pd

def assign_kri_status(dataframe, kri_name, amber_threshold, red_threshold):
    """Assign KRI status based on thresholds."""
    if dataframe.empty:
        dataframe['kri_value_status'] = []
        return dataframe
    
    dataframe['kri_value_status'] = dataframe[kri_name].apply(
        lambda x: 'Green' if x <= amber_threshold else ('Amber' if x <= red_threshold else 'Red')
    )
    return dataframe

import pandas as pd

def aggregate_kri_status(dataframe, kri_list):
    """Aggregates KRI statuses for visualization."""
    if not kri_list:
        return None

    df = dataframe.copy()
    result = pd.DataFrame()

    for kri in kri_list:
        if kri not in df.columns:
            raise KeyError(f"KRI column '{kri}' not found in dataframe.")

        # Check if KRI status column contains string values
        if not all(isinstance(x, str) for x in df[kri]):
            raise TypeError(f"KRI column '{kri}' must contain string values.")

        status_counts = df[kri].value_counts().to_dict()
        for status in ['Green', 'Amber', 'Red']:
            count = status_counts.get(status, 0)
            result[f'{kri}_{status}'] = [count]

    return result