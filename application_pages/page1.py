
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

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

def run_page1():
    st.header("KRI Configuration & Data Generation")

    # Sidebar inputs
    st.sidebar.header("Data Generation Parameters")
    duration = st.sidebar.slider("Duration (days)", 1, 365, 30)
    num_locations = st.sidebar.slider("Number of Locations", 1, 5, 2)

    st.sidebar.subheader("Base Values")
    base_trades = st.sidebar.number_input("Base Trades", value=1000)
    base_unreconciled = st.sidebar.number_input("Base Unreconciled", value=50)
    base_staff = st.sidebar.number_input("Base Staff", value=10)
    base_values = {'trades': base_trades, 'unreconciled': base_unreconciled, 'staff': base_staff}

    st.sidebar.subheader("Volatility")
    volatility = st.sidebar.slider("Volatility", 0.0, 0.5, 0.1)

    st.sidebar.subheader("Trend Factors")
    trend_trades = st.sidebar.number_input("Trend Trades", value=0.01)
    trend_unreconciled = st.sidebar.number_input("Trend Unreconciled", value=-0.005)
    trend_staff = st.sidebar.number_input("Trend Staff", value=0.001)
    trend_factors = {'trades': trend_trades, 'unreconciled': trend_unreconciled, 'staff': trend_staff}

    # KRI Selection
    st.sidebar.header("KRI Selection")
    kri_options = ['Number of unreconciled trades > 5 days', 'Staff turnover', 'System outages', 'Unreconciled items as % of volume', 'Volume per staff']
    selected_kris = st.sidebar.multiselect("Select KRIs", kri_options, default=['Number of unreconciled trades > 5 days', 'Staff turnover'])

    # Generate data
    if st.sidebar.button("Run Simulation"):
        with st.spinner("Generating data..."):
            synthetic_df = generate_synthetic_data(duration, num_locations, base_values, volatility, trend_factors)
            st.dataframe(synthetic_df)
