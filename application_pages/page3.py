
import streamlit as st
import pandas as pd
import plotly.express as px

def aggregate_kri_status(dataframe, kri_list):
    """Aggregates KRI statuses for visualization."""
    if not kri_list:
        return None

    df = dataframe.copy()
    result = pd.DataFrame()

    for kri in kri_list:
        if kri not in df.columns:
            raise KeyError(f"KRI column '{kri}' not found in dataframe.")

        status_counts = df[kri].value_counts().to_dict()
        for status in ['Green', 'Amber', 'Red']:
            count = status_counts.get(status, 0)
            result[f'{kri}_{status}'] = [count]

    return result

def run_page3():
    st.header("Aggregated KRI Status")

    # Sample Data (replace with actual data loading or generation)
    data = {'Location': ['Location 1', 'Location 2', 'Location 1', 'Location 2'],
            'KRI1_status': ['Green', 'Amber', 'Red', 'Green'],
            'KRI2_status': ['Amber', 'Red', 'Green', 'Amber']}
    df = pd.DataFrame(data)

    # KRI Status Columns Selection
    kri_status_options = [col for col in df.columns if col.endswith('_status')]
    selected_kri_statuses = st.multiselect("Select KRI Statuses", kri_status_options, default=kri_status_options)

    # Aggregate KRI Status
    if selected_kri_statuses:
        aggregated_df = aggregate_kri_status(df, selected_kri_statuses)

        # Display Aggregated Data
        st.dataframe(aggregated_df)

        # Create bar chart
        if aggregated_df is not None:
            # Reshape the DataFrame for Plotly Express
            reshaped_df = pd.DataFrame()
            for kri_status in selected_kri_statuses:
                for status in ['Green', 'Amber', 'Red']:
                    count_column = f'{kri_status}_{status}'
                    if count_column in aggregated_df.columns:
                        reshaped_df = pd.concat([reshaped_df, pd.DataFrame({'KRI': [kri_status], 'Status': [status], 'Count': aggregated_df[count_column].values})], ignore_index=True)

            if not reshaped_df.empty:
                fig = px.bar(reshaped_df, x='KRI', y='Count', color='Status', title='Aggregated KRI Status')
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.warning("No data to display in the bar chart.")
    else:
        st.warning("Please select at least one KRI Status to aggregate.")
