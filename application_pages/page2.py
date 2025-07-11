
import streamlit as st
import pandas as pd
import plotly.express as px

def calculate_kpis(dataframe):
    """Computes KRI values from the input DataFrame."""

    if dataframe.empty:
        return dataframe

    try:
        dataframe['Unreconciled items as % of volume'] = (dataframe['Number of unreconciled trades > 5 days'] / dataframe['Volume of Trades per day']) * 100
        dataframe['Unreconciled items as % of volume'] = dataframe['Unreconciled items as % of volume'].fillna(0)
        dataframe['Unreconciled items as % of volume'] = dataframe['Unreconciled items as % of volume'].replace([float('inf'), float('nan')], 0)
        dataframe['Volume per staff'] = dataframe['Volume of Trades per day'] / dataframe['Number of Back Office Staff']
        dataframe['Volume per staff'] = dataframe['Volume per staff'].replace(0, float('inf'))

    except KeyError as e:
        raise KeyError(e)
    except ZeroDivisionError:
        pass

    return dataframe

def assign_kri_status(dataframe, kri_name, amber_threshold, red_threshold):
    """Assign KRI status based on thresholds."""
    if dataframe.empty:
        dataframe['kri_value_status'] = []
        return dataframe

    dataframe['kri_value_status'] = dataframe[kri_name].apply(
        lambda x: 'Green' if x <= amber_threshold else ('Amber' if x <= red_threshold else 'Red')
    )
    return dataframe


def run_page2():
    st.header("KRI Trend Analysis")

    # Sample Data (replace with actual data loading or generation)
    data = {
        'Date': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05']),
        'Location': ['Location 1'] * 5,
        'Number of unreconciled trades > 5 days': [50, 60, 70, 80, 90],
        'Staff turnover': [2, 3, 2, 4, 5],
        'Volume of Trades per day': [1000, 1200, 1500, 1800, 2000],
        'Number of Back Office Staff': [10, 11, 12, 13, 14]
    }
    df = pd.DataFrame(data)

    # Calculate KPIs
    df = calculate_kpis(df)

    # KRI Selection
    kri_options = ['Number of unreconciled trades > 5 days', 'Staff turnover', 'Unreconciled items as % of volume', 'Volume per staff']
    selected_kri = st.selectbox("Select KRI", kri_options, index=0)

    # Thresholds
    amber_threshold = st.number_input("Amber Threshold", value=70)
    red_threshold = st.number_input("Red Threshold", value=85)

    # Assign KRI Status
    df = assign_kri_status(df, selected_kri, amber_threshold, red_threshold)

    # Plotting
    fig = px.line(df, x="Date", y=selected_kri, color="Location", title=f"{selected_kri} Trend")
    fig.add_hline(y=amber_threshold, line=dict(color="orange"), annotation_text="Amber Threshold")
    fig.add_hline(y=red_threshold, line=dict(color="red"), annotation_text="Red Threshold")
    st.plotly_chart(fig, use_container_width=True)
