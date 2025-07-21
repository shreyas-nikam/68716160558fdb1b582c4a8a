id: 68716160558fdb1b582c4a8a_documentation
summary: First lab of Module 4 Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# Developing a Key Risk Indicator (KRI) Monitoring Application with Streamlit

## 1. Understanding the QuLab Application and Operational Risk Management
Duration: 00:05:00

Welcome to this codelab! In this guide, you will delve into the development and functionalities of **QuLab**, a Streamlit application designed for Key Risk Indicator (KRI) management in the domain of operational risk. This application provides a hands-on platform to understand, simulate, analyze, and visualize KRIs, which are crucial for proactive risk management.

Operational risk is the risk of loss resulting from inadequate or failed internal processes, people and systems or from external events. KRIs are metrics used by organizations to provide an early signal of increasing risk exposure in various operational areas. By monitoring KRIs, organizations can identify potential issues before they escalate into significant losses.

<aside class="positive">
Understanding KRIs is fundamental for any developer or risk professional working in finance, compliance, or any industry where operational stability is critical. This application will show you how to build a practical tool for this purpose.
</aside>

**Why is this application important?**

*   **Proactive Risk Identification**: KRIs act as an early warning system, helping to identify emerging risks.
*   **Data-Driven Decisions**: The application facilitates the simulation and analysis of KRI data, enabling informed decision-making.
*   **Operational Efficiency**: By highlighting areas of concern, it helps prioritize risk mitigation efforts, improving overall operational efficiency.
*   **Regulatory Compliance**: Many industries, especially financial services, have regulatory requirements around operational risk management, making KRI monitoring essential.

**Concepts Explained in this Codelab:**

*   **Key Risk Indicators (KRIs)**: Metrics that provide insight into an organization's risk exposure.
*   **Thresholds (Amber & Red)**: Predefined levels that trigger alerts when KRI values exceed them, indicating increasing risk.
*   **Synthetic Data Generation**: Creating artificial data that mimics real-world scenarios for testing and simulation.
*   **Time-Series Analysis**: Tracking KRI trends over time to identify patterns and deviations.
*   **Aggregated Risk View**: Consolidating KRI statuses across different dimensions (e.g., business units) for a holistic overview.

**Application Architecture Overview:**

The QuLab application is built using Streamlit, a powerful Python library for creating interactive web applications. Its modular design separates concerns into a main application file (`app.py`) and distinct page modules (`application_pages/*.py`).

The main `app.py` handles the overall structure, navigation, and initial context. It uses Streamlit's `st.sidebar.selectbox` to allow users to navigate between different functionalities, each implemented in its dedicated Python file within the `application_pages` directory.

The application's functionalities are logically divided into four main pages:

*   **KRI Configuration & Data Generation (`page1.py`)**: For setting up KRIs and simulating data.
*   **KRI Trend Analysis (`page2.py`)**: For visualizing individual KRI trends against defined thresholds.
*   **Aggregated KRI Status (`page3.py`)**: For a consolidated view of KRI statuses across different units or categories.
*   **KRI Data Fields Reference (`page4.py`)**: A static reference for standard KRI attributes.

```mermaid
graph TD
    A[app.py - Main Streamlit Application] --> B{Sidebar Navigation Selection};
    B -- "KRI Configuration & Data Generation" --> C[application_pages/page1.py];
    B -- "KRI Trend Analysis" --> D[application_pages/page2.py];
    B -- "Aggregated KRI Status" --> E[application_pages/page3.py];
    B -- "KRI Data Fields Reference" --> F[application_pages/page4.py];

    C -- Generates Synthetic KRI Data --> G[Data Frame in Session State (Conceptual)];
    G -- "Used by subsequent pages for analysis (Currently, pages 2 & 3 use sample data, but could be integrated)" --> D;
    G -- "Used by subsequent pages for analysis" --> E;

    D -- Calculates KRI Values & Status --> G;
    E -- Aggregates KRI Status --> H[Aggregated Views];
    F -- Displays Static KRI Reference Data --> I[Informational View];
```

This modular approach makes the application scalable and easier to maintain. Each page focuses on a specific aspect of KRI management, providing a clear user experience and a robust backend structure for developers.

## 2. Setting Up the Environment and Running the Application
Duration: 00:03:00

Before diving into the code, let's ensure you have the necessary environment set up to run the Streamlit application.

**Prerequisites:**

*   Python 3.7+ installed.
*   `pip` (Python package installer).

**Installation Steps:**

1.  **Create a Virtual Environment (Recommended):**
    This helps manage dependencies for your project without conflicting with other Python projects.

    ```bash
    python -m venv venv
    ```

2.  **Activate the Virtual Environment:**

    *   On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    *   On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

3.  **Install Required Libraries:**
    The application uses `streamlit`, `pandas`, `numpy`, and `plotly`. You can install them using pip.

    ```bash
    pip install streamlit pandas numpy plotly
    ```

**Organizing the Files:**

Create the following directory structure and save the provided Python code snippets into their respective files:

```
your_project_directory/
├── app.py
└── application_pages/
    ├── __init__.py  (empty file to make it a package)
    ├── page1.py
    ├── page2.py
    ├── page3.py
    └── page4.py
```

Place the `app.py` content into `your_project_directory/app.py`.
Place the `page1.py` content into `your_project_directory/application_pages/page1.py`.
And so on for `page2.py`, `page3.py`, and `page4.py`.

**Running the Streamlit Application:**

Once all files are in place and your environment is set up, navigate to `your_project_directory` in your terminal and run the application:

```bash
streamlit run app.py
```

This command will open the application in your default web browser (usually at `http://localhost:8501`).

<aside class="positive">
Streamlit automatically reloads the application whenever you make changes to the Python files, making the development process very efficient.
</aside>

You should see the "QuLab" application with a sidebar for navigation.

## 3. KRI Configuration & Data Generation
Duration: 00:10:00

This is the first functional page of the QuLab application, handled by `application_pages/page1.py`. It's responsible for allowing users to configure parameters for synthetic KRI data generation and then simulate that data.

**Key Functionality:**

*   **Parameter Configuration**: Users can define the duration of the data, number of locations, base values for core operational metrics (trades, unreconciled items, staff), volatility, and trend factors.
*   **KRI Selection**: Users can select which Key Risk Indicators they want to monitor from a predefined list.
*   **Synthetic Data Generation**: Based on the configured parameters, the application generates time-series data for the selected KRIs and their underlying metrics.

Let's examine the core of this page: the `generate_synthetic_data` function.

```python
# application_pages/page1.py

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
            # Simulate metrics with base, volatility, and trend
            trades = base_values['trades'] * (1 + np.random.normal(0, volatility) + trend_factors['trades'] * (date - dates[0]).days)
            unreconciled = base_values['unreconciled'] * (1 + np.random.normal(0, volatility) + trend_factors['unreconciled'] * (date - dates[0]).days)
            staff = base_values['staff'] * (1 + np.random.normal(0, volatility) + trend_factors['staff'] * (date - dates[0]).days)

            # Ensure values are non-negative integers
            trades = max(0, int(trades))
            unreconciled = max(0, int(unreconciled))
            staff = max(0, int(staff))

            data.append({
                'Date': date,
                'Location': f'Location {location + 1}',
                'Volume of Trades per day': trades,
                'Number of unreconciled trades > 5 days': unreconciled,
                'Staff turnover': staff,
                'System outages': np.random.randint(0, 2), # Binary KRI
                'Number of Back Office Staff': staff * 5 # Derived metric
            })

    df = pd.DataFrame(data)
    return df

def run_page1():
    st.header("KRI Configuration & Data Generation")

    # Sidebar inputs for data generation parameters
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

    # KRI Selection for later use (though not directly used for generation in this page)
    st.sidebar.header("KRI Selection")
    kri_options = ['Number of unreconciled trades > 5 days', 'Staff turnover', 'System outages', 'Unreconciled items as % of volume', 'Volume per staff']
    selected_kris = st.sidebar.multiselect("Select KRIs", kri_options, default=['Number of unreconciled trades > 5 days', 'Staff turnover'])

    # Button to trigger data generation
    if st.sidebar.button("Run Simulation"):
        with st.spinner("Generating data..."):
            synthetic_df = generate_synthetic_data(duration, num_locations, base_values, volatility, trend_factors)
            st.dataframe(synthetic_df)
            # In a full application, you would store synthetic_df in st.session_state
            # for other pages to access it. For this demo, subsequent pages use sample data.
            st.session_state['synthetic_data'] = synthetic_df
            st.session_state['selected_kris'] = selected_kris
```

**Understanding `generate_synthetic_data`:**

This function simulates time-series data for key operational metrics. For each day and location, it calculates values based on:

1.  **Base Value**: A starting point for the metric.
2.  **Volatility**: Random noise (normally distributed) introduced to simulate day-to-day fluctuations. This is represented by $N(0, \sigma)$, where $\sigma$ is the `volatility` parameter.
3.  **Trend Factor**: A linear trend applied over time to simulate growth or decline. For a metric $M$, the formula approximately follows:
    $$M_t = M_0 \times (1 + N(0, \sigma) + \text{TrendFactor} \times t)$$
    where $M_0$ is the base value, $\sigma$ is volatility, and $t$ is the number of days from the start.

Metrics generated include:
*   `Volume of Trades per day`
*   `Number of unreconciled trades > 5 days`
*   `Staff turnover`
*   `System outages` (binary 0 or 1)
*   `Number of Back Office Staff` (derived from `Staff turnover` as `staff * 5`)

**Streamlit Components Used:**

*   `st.header()`: To display the page title.
*   `st.sidebar.slider()`: For numerical input ranges like duration, number of locations, and volatility.
*   `st.sidebar.number_input()`: For specific numerical inputs like base values and trend factors.
*   `st.sidebar.multiselect()`: For selecting multiple KRIs from a list.
*   `st.sidebar.button()`: To trigger the data generation process.
*   `st.spinner()`: To show a loading animation while data is being generated.
*   `st.dataframe()`: To display the generated Pandas DataFrame in a scrollable table.
*   `st.session_state`: Although commented in the provided code, this is the standard Streamlit way to pass data between pages. We've added it to show how it *should* be done.

<aside class="negative">
In the provided `app.py`, `page2.py` and `page3.py` use their own sample data. To make the application fully dynamic and utilize the data generated in `page1.py`, you would need to implement `st.session_state` to pass `synthetic_df` to the subsequent pages.
</aside>

## 4. KRI Trend Analysis
Duration: 00:12:00

This page, powered by `application_pages/page2.py`, is dedicated to visualizing the trends of individual KRIs over time and assessing their status against predefined thresholds.

**Key Functionality:**

*   **KPI Calculation**: Computes derived KRIs like "Unreconciled items as % of volume" and "Volume per staff" from the raw operational metrics.
*   **Threshold Assignment**: Assigns a status (Green, Amber, Red) to each KRI value based on user-defined thresholds.
*   **Interactive Trend Visualization**: Uses Plotly Express to display KRI trends, clearly marking Amber and Red threshold lines.

Let's look at the core functions within `page2.py`.

```python
# application_pages/page2.py

import streamlit as st
import pandas as pd
import plotly.express as px

def calculate_kpis(dataframe):
    """Computes KRI values from the input DataFrame."""

    if dataframe.empty:
        return dataframe

    try:
        # Calculate 'Unreconciled items as % of volume'
        dataframe['Unreconciled items as % of volume'] = (dataframe['Number of unreconciled trades > 5 days'] / dataframe['Volume of Trades per day']) * 100
        dataframe['Unreconciled items as % of volume'] = dataframe['Unreconciled items as % of volume'].fillna(0)
        dataframe['Unreconciled items as % of volume'] = dataframe['Unreconciled items as % of volume'].replace([float('inf'), float('nan')], 0)

        # Calculate 'Volume per staff'
        dataframe['Volume per staff'] = dataframe['Volume of Trades per day'] / dataframe['Number of Back Office Staff']
        # Handle division by zero for Volume per staff, treating 0 staff as infinite volume per staff (or very high risk)
        dataframe['Volume per staff'] = dataframe['Volume per staff'].replace(0, float('inf'))

    except KeyError as e:
        raise KeyError(e)
    except ZeroDivisionError:
        # This catch block might not be fully effective if NaN/inf are generated,
        # but the .replace() handles it better.
        pass

    return dataframe

def assign_kri_status(dataframe, kri_name, amber_threshold, red_threshold):
    """Assign KRI status based on thresholds."""
    if dataframe.empty:
        dataframe['kri_value_status'] = [] # Ensure column exists even if empty
        return dataframe

    # Apply threshold logic: Green <= Amber, Amber <= Red, Red > Red
    dataframe['kri_value_status'] = dataframe[kri_name].apply(
        lambda x: 'Green' if x <= amber_threshold else ('Amber' if x <= red_threshold else 'Red')
    )
    return dataframe


def run_page2():
    st.header("KRI Trend Analysis")

    # Sample Data (In a real app, this would come from st.session_state from page1)
    # Using st.session_state.get() to try and retrieve data from page1 if available
    df = st.session_state.get('synthetic_data', pd.DataFrame({
        'Date': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05']),
        'Location': ['Location 1'] * 5,
        'Number of unreconciled trades > 5 days': [50, 60, 70, 80, 90],
        'Staff turnover': [2, 3, 2, 4, 5],
        'Volume of Trades per day': [1000, 1050, 1100, 1150, 1200], # Added for KPI calculation
        'Number of Back Office Staff': [50, 52, 55, 58, 60] # Added for KPI calculation
    }))


    # If no data is available after trying session state, display a warning and return.
    if df.empty or 'Volume of Trades per day' not in df.columns: # Check for necessary columns
        st.warning("Please generate data first in 'KRI Configuration & Data Generation' page, or ensure the sample data includes required columns.")
        return

    # Calculate KPIs
    df = calculate_kpis(df)

    # KRI Selection (options now include calculated KPIs)
    kri_options = ['Number of unreconciled trades > 5 days', 'Staff turnover', 'System outages'] # Base KRIs from page1
    if 'Unreconciled items as % of volume' in df.columns:
        kri_options.append('Unreconciled items as % of volume')
    if 'Volume per staff' in df.columns:
        kri_options.append('Volume per staff')

    selected_kri = st.selectbox("Select KRI", kri_options, index=0 if kri_options else None)

    if selected_kri is None:
        st.warning("No KRIs available to select.")
        return

    # Thresholds - provide reasonable defaults based on KRI
    default_amber = 70
    default_red = 85
    if selected_kri == 'Staff turnover':
        default_amber = 3
        default_red = 4
    elif selected_kri == 'Unreconciled items as % of volume':
        default_amber = 7.0
        default_red = 8.5
    elif selected_kri == 'Volume per staff': # Assuming higher volume per staff is good, so thresholds are inverse
        default_amber = 120 # Below this is amber
        default_red = 110 # Below this is red (lower value, worse performance)
        st.info("For 'Volume per staff', lower values indicate higher risk.")
        # Adjust assign_kri_status logic slightly for inverse KRI, or manage thresholds appropriately.
        # For simplicity, current logic assumes higher value = higher risk.
        # If Volume per staff is *inverse*, the logic should be:
        # 'Green' if x >= amber_threshold else ('Amber' if x >= red_threshold else 'Red')
        # However, for this codelab, we'll stick to the original logic and
        # let the user set thresholds assuming a direct relationship or adjust them inversely.


    amber_threshold = st.number_input("Amber Threshold", value=float(default_amber), key=f"{selected_kri}_amber")
    red_threshold = st.number_input("Red Threshold", value=float(default_red), key=f"{selected_kri}_red")

    # Assign KRI Status
    df = assign_kri_status(df, selected_kri, amber_threshold, red_threshold)

    # Plotting
    if not df.empty:
        fig = px.line(df, x="Date", y=selected_kri, color="Location", title=f"{selected_kri} Trend")
        fig.add_hline(y=amber_threshold, line_dash="dot", line_color="orange", annotation_text="Amber Threshold", annotation_position="top left")
        fig.add_hline(y=red_threshold, line_dash="dot", line_color="red", annotation_text="Red Threshold", annotation_position="top left")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No data available to display KRI trends.")

```

**Understanding `calculate_kpis`:**

This function computes two common derived KRIs:

*   `Unreconciled items as % of volume`: This KRI measures the efficiency of reconciliation processes.
    $$ \text{Unreconciled % of Volume} = \frac{\text{Number of unreconciled trades > 5 days}}{\text{Volume of Trades per day}} \times 100 $$
    It includes error handling for division by zero and `NaN`/`inf` values, replacing them with `0`.
*   `Volume per staff`: This KRI assesses staff productivity.
    $$ \text{Volume per Staff} = \frac{\text{Volume of Trades per day}}{\text{Number of Back Office Staff}} $$
    It handles zero in `Number of Back Office Staff` by replacing it with `inf`, implying extreme inefficiency or an issue.

**Understanding `assign_kri_status`:**

This function categorizes KRI values into 'Green', 'Amber', or 'Red' based on the provided thresholds:

*   **Green**: KRI value $\le$ Amber Threshold
*   **Amber**: Amber Threshold $<$ KRI value $\le$ Red Threshold
*   **Red**: KRI value $>$ Red Threshold

**Streamlit Components Used:**

*   `st.selectbox()`: To allow users to choose which KRI to visualize.
*   `st.number_input()`: For defining the Amber and Red alert thresholds.
*   `st.plotly_chart()`: To display the interactive line chart generated by Plotly Express. `use_container_width=True` makes the chart responsive.
*   `fig.add_hline()`: Plotly feature to add horizontal lines for thresholds.

<aside class="positive">
Plotly Express is an excellent choice for creating interactive visualizations in Streamlit. Its high-level API makes it easy to generate complex charts with minimal code, and the interactivity allows for detailed data exploration.
</aside>

## 5. Aggregated KRI Status
Duration: 00:08:00

The third page, implemented in `application_pages/page3.py`, provides an aggregated view of KRI statuses across different dimensions (e.g., locations, departments). This is crucial for management to get a high-level overview of risk exposure without delving into individual KRI trends.

**Key Functionality:**

*   **Status Aggregation**: Counts the occurrences of 'Green', 'Amber', and 'Red' statuses for selected KRIs.
*   **Consolidated View**: Presents these counts in a table format.
*   **Visual Summary**: Displays a stacked bar chart to visually represent the aggregated KRI statuses, allowing for quick comparison of risk levels across different KRIs.

Let's examine the `aggregate_kri_status` function.

```python
# application_pages/page3.py

import streamlit as st
import pandas as pd
import plotly.express as px

def aggregate_kri_status(dataframe, kri_status_list):
    """Aggregates KRI statuses for visualization."""
    if not kri_status_list:
        return pd.DataFrame() # Return empty if no KRIs selected

    df = dataframe.copy()
    result_data = [] # To build the result DataFrame

    # Assuming dataframe contains columns like 'KRI1_status', 'KRI2_status'
    # The current sample data in run_page3() aligns with this.
    # If using generated data from page1, you'd first need to calculate KRI values
    # and then assign 'kri_value_status' for each relevant KRI based on thresholds.

    # Example: If your dataframe from page1 had 'Unreconciled items as % of volume' and you want to aggregate its status
    # You would first need a 'Unreconciled items as % of volume_status' column for each row.
    # This function expects columns like 'KRI_status'.

    # For the current implementation, we iterate directly on the *selected_kri_statuses* which are expected to be column names
    # like 'KRI1_status'.
    for kri_status_col in kri_status_list:
        if kri_status_col not in df.columns:
            st.warning(f"KRI status column '{kri_status_col}' not found in data.")
            continue # Skip if column doesn't exist

        status_counts = df[kri_status_col].value_counts().to_dict()
        row_data = {'KRI': kri_status_col.replace('_status', '')} # Clean name for display
        for status in ['Green', 'Amber', 'Red']:
            row_data[status] = status_counts.get(status, 0)
        result_data.append(row_data)

    if not result_data:
        return pd.DataFrame()

    return pd.DataFrame(result_data)


def run_page3():
    st.header("Aggregated KRI Status")

    # Sample Data (In a real app, this would be computed KRI statuses from generated data)
    # This sample data structure directly provides KRI_status columns, which is what aggregate_kri_status expects.
    # To use data from page1:
    # 1. Retrieve st.session_state['synthetic_data']
    # 2. For each KRI, calculate its value (if derived) and then use assign_kri_status() to add '_status' column
    #    E.g., df['KRI1_status'] = assign_kri_status(df.copy(), 'KRI1', amber_thr, red_thr)['kri_value_status']
    # 3. Pass this processed DataFrame to aggregate_kri_status.

    data = {
        'Location': ['Location 1', 'Location 2', 'Location 1', 'Location 2', 'Location 1', 'Location 2'],
        'KRI1_status': ['Green', 'Amber', 'Red', 'Green', 'Amber', 'Green'], # e.g., Unreconciled trades
        'KRI2_status': ['Amber', 'Red', 'Green', 'Amber', 'Red', 'Green'], # e.g., Staff turnover
        'KRI3_status': ['Green', 'Green', 'Amber', 'Green', 'Green', 'Green'] # e.g., System outages
    }
    df = pd.DataFrame(data)


    # KRI Status Columns Selection (only show columns ending with _status)
    kri_status_options = [col for col in df.columns if col.endswith('_status')]
    selected_kri_statuses = st.multiselect("Select KRI Statuses", kri_status_options, default=kri_status_options)

    # Aggregate KRI Status
    if selected_kri_statuses:
        aggregated_df = aggregate_kri_status(df, selected_kri_statuses)

        if not aggregated_df.empty:
            # Display Aggregated Data
            st.subheader("Aggregated KRI Status Counts")
            st.dataframe(aggregated_df)

            # Reshape the DataFrame for Plotly Express stacked bar chart
            # We want columns: KRI, Status (Green/Amber/Red), Count
            reshaped_df = aggregated_df.melt(id_vars=['KRI'], var_name='Status', value_name='Count')

            # Ensure order of colors for statuses
            color_map = {'Green': 'green', 'Amber': 'orange', 'Red': 'red'}
            status_order = ['Green', 'Amber', 'Red']
            reshaped_df['Status'] = pd.Categorical(reshaped_df['Status'], categories=status_order, ordered=True)
            reshaped_df = reshaped_df.sort_values('Status')

            # Create bar chart
            fig = px.bar(reshaped_df, x='KRI', y='Count', color='Status',
                         title='Aggregated KRI Status',
                         color_discrete_map=color_map)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("No data to display in the bar chart after aggregation. Check your KRI status selections.")
    else:
        st.warning("Please select at least one KRI Status to aggregate.")

```

**Understanding `aggregate_kri_status`:**

This function takes a DataFrame and a list of KRI status columns (e.g., `['KRI1_status', 'KRI2_status']`). For each selected status column, it counts how many times 'Green', 'Amber', and 'Red' appear.

The output DataFrame `aggregated_df` will have rows for each selected KRI and columns for 'Green', 'Amber', and 'Red' counts.

**Streamlit Components Used:**

*   `st.multiselect()`: To allow users to choose which KRI statuses to include in the aggregation.
*   `st.dataframe()`: To display the raw aggregated counts.
*   `st.plotly_chart()`: To display the stacked bar chart. `px.bar` is used, and the DataFrame is `melt`ed to a long format suitable for stacking.
    *   The `color_discrete_map` and explicit `pd.Categorical` ordering ensure that the bars are colored consistently (Green, Amber, Red) and stacked in a meaningful order.

<aside class="positive">
Aggregated views like this are incredibly valuable for high-level oversight. They allow stakeholders to quickly grasp the overall risk posture and identify areas that require immediate attention without getting lost in the details of individual trends.
</aside>

## 6. KRI Data Fields Reference
Duration: 00:05:00

The final page, handled by `application_pages/page4.py`, serves as a comprehensive reference guide for standard KRI data fields. While not interactive in terms of data processing, it's an essential resource for understanding the metadata and context surrounding Key Risk Indicators.

**Key Functionality:**

*   **Static Data Display**: Presents a pre-defined table containing attributes related to KRI definitions.
*   **Detailed Descriptions**: Each attribute comes with a `Description` and a `Use` explanation, clarifying its purpose and importance in KRI management.

Let's look at the `run_page4` function.

```python
# application_pages/page4.py

import streamlit as st
import pandas as pd

def run_page4():
    st.header("KRI Data Fields Reference")

    data = {
        'Attribute': ['Measures/Description', 'KRI Construction', 'Reported by', 'Reported for', 'Risk Category(ies)',
                      'Relevant Product(s)', 'Relevant Process(es)', 'Reporting Frequency', 'Reporting Period',
                      'Submission Date', 'Causal Event Category', 'Data Thresholds', 'Comment Field', 'KRI Priority',
                      'Threshold Breach Path'],
        'Description': [
            'Number, value, duration, percent, rating, issue, etc. associated with KRI',
            'Methodology for computation of KRI from source data where KRI is a derived calculation or a linked/compound KRI',
            'Business area or function reporting the data',
            'Relevant org unit(s)/entity(ies)',
            'Relevant category(ies) of risk',
            'Applicable product(s) the KRI is used for',
            'Applicable process(es) that the KRI is linked to',
            'Daily, weekly, monthly, etc.',
            'Data cut off (e.g., month end)',
            'Reporting submission deadline',
            'KRI linkage to a business risk or operational risk cause',
            'KRI tolerances, red and amber levels',
            'Mandatory for any breaches',
            'Risk level/importance',
            'Escalation workflow'
        ],
        'Use': [
            'Describes data attributes and determines what data might be aggregated',
            'Details the construction and data sources used for each KRI',
            'Clarifies workflow, provides audit trail by reporter',
            'Explains dependencies and allows for reporting cuts of risk profile by management area, risk, product, process',
            'Allows for causal analysis of business/top risk drivers',
            '-',
            '-',
            'Workflow for monitoring',
            'Allows trending analysis to be performed',
            'For review, committees, etc.',
            'Allows for causal analysis of business/top risk drivers',
            'Defines risk appetite and drives action/mitigation',
            'Explains data/breaches',
            'Highlights data/issues for relevant management level',
            '-'
        ]
    }

    df = pd.DataFrame(data)
    st.dataframe(df)

```

**Understanding the Data Fields:**

This page presents a tabular breakdown of various attributes commonly associated with Key Risk Indicators. These attributes help define, categorize, and manage KRIs effectively within an organization. For instance:

*   **KRI Construction**: Explains how a KRI is calculated, especially important for derived or compound KRIs.
*   **Data Thresholds**: Highlights the critical Amber and Red levels that define acceptable risk appetites.
*   **Causal Event Category**: Links a KRI to the underlying business or operational risk event it is designed to signal. This is crucial for root cause analysis.
*   **Threshold Breach Path**: Defines the escalation workflow when a KRI breaches its thresholds.

**Streamlit Components Used:**

*   `st.dataframe()`: Used to display the Pandas DataFrame containing the KRI data fields and their descriptions in an easy-to-read table format.

This reference page is highly valuable for developers and risk professionals alike, ensuring a common understanding of KRI terminology and best practices in their design and implementation.

## 7. Further Exploration and Enhancements
Duration: 00:05:00

You have now explored all the functionalities of the QuLab Streamlit application. This provides a solid foundation for understanding KRI management and building interactive data applications.

Here are some ideas for further exploration and enhancements to the application:

1.  **Integrate Data Flow with `st.session_state`**:
    *   Currently, `page2.py` and `page3.py` use sample data. Modify them to utilize the `synthetic_df` generated in `page1.py` by storing and retrieving it using `st.session_state`.
    *   **Hint**: In `page1.py`, after `synthetic_df` is generated, add `st.session_state['synthetic_data'] = synthetic_df`. In `page2.py` and `page3.py`, retrieve it with `df = st.session_state.get('synthetic_data', default_sample_data)`.
    *   You will also need to add logic in `page2.py` and `page3.py` to calculate the `_status` columns based on the KRI selections and thresholds chosen in `page1.py` or `page2.py`.

2.  **Save and Load Configurations/Data**:
    *   Implement functionality to save the generated synthetic data (e.g., to a CSV file) and load it back later. Streamlit's `st.download_button` and `st.file_uploader` can be useful here.
    *   Allow users to save and load KRI threshold configurations.

3.  **Real-time Data Simulation**:
    *   Instead of generating all data at once, simulate data point by point over a period, perhaps using `st.empty()` and `time.sleep()` to create a "live" feel.

4.  **Advanced KRI Calculations**:
    *   Introduce more complex KRI calculations, such as those involving moving averages, standard deviations, or weighted averages of multiple underlying metrics.
    *   Implement **Compounded KRIs** where a single KRI is a function of multiple other KRIs.

5.  **User Authentication/Multi-tenancy**:
    *   For a production-ready application, consider adding user authentication and potentially allowing different users/departments to manage their own sets of KRIs and data.

6.  **Alerting Mechanism**:
    *   Beyond visualization, implement a simple alerting system. This could be as simple as displaying prominent messages when thresholds are breached, or more complex like integrating with email/SMS notifications (though this would require external services).

7.  **More Sophisticated Visualizations**:
    *   Explore other Plotly chart types (e.g., heatmaps for risk matrices, scatter plots for correlation analysis between KRIs) or integrate with other visualization libraries.

8.  **Error Handling and Edge Cases**:
    *   Improve robust error handling, especially for user inputs and data calculations (e.g., what if a user enters a Red threshold lower than Amber?).

9.  **Deployment**:
    *   Deploy the application to Streamlit Community Cloud or other cloud platforms like Heroku, AWS, or Azure, to make it accessible online.

By implementing these enhancements, you can transform this foundational KRI application into a more powerful and production-ready tool for operational risk management. Happy coding!
