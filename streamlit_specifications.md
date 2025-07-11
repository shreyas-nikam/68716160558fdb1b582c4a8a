### Streamlit Application Requirements Specification

This document outlines the requirements for developing an interactive Streamlit application based on the provided Jupyter Notebook content and user requirements. It serves as a blueprint, detailing the application's purpose, user interface components, and the integration of core functionalities with relevant code snippets.

---

### 1. Application Overview

**Purpose and Objectives:**
The primary purpose of this Streamlit application is to provide an interactive simulator for a Key Risk Indicator (KRI) framework. It enables users to define, monitor, and analyze KRIs across different simulated business units, demonstrating their utility as early warning tools for operational risk management.

The key objectives and learning outcomes for users are:
- To understand the role and characteristics of effective Key Risk Indicators (KRIs), as described in the PRMIA Operational Risk Manager Handbook [1].
- To learn how to select, define, and monitor KRIs, including setting thresholds for `Amber` and `Red` alerts.
- To analyze the interdependencies between different KRIs and their impact on the overall risk profile.
- To explore the differences and uses of `Top Down` versus `Bottom Up` KRI approaches.

**Key Features:**
- **KRI Configuration**: Allows users to select predefined KRIs and set custom `Amber` and `Red` alert thresholds.
- **Synthetic Data Generation**: Simulates time-series data for selected KRIs across multiple business locations, including underlying operational metrics.
- **Interactive Dashboards**: Visualizes KRI trends over time, highlighting threshold breaches, and examines relationships between compounded KRIs.
- **Aggregated KRI View**: Provides a consolidated view of KRI statuses (Green, Amber, Red) across business units, using an aggregated comparison.
- **KRI Data Fields Exploration**: An interactive table displaying descriptions of standard KRI data fields.

---

### 2. User Interface Requirements

**Layout and Navigation Structure:**
The application will follow a clean, intuitive layout, leveraging Streamlit's sidebar for user inputs and the main area for displaying results and visualizations.
- **Sidebar**: Will house all configuration parameters and controls for data generation and KRI settings.
- **Main Content Area**: Will be organized into multiple sections or tabs to present different aspects of the KRI analysis (e.g., "KRI Configuration & Data Generation", "KRI Trend Analysis", "Aggregated KRI Status", "KRI Data Fields Reference").

**Input Widgets and Controls:**
Users will interact with the application through various widgets:
- **KRI Selection**: A `st.multiselect` widget in the sidebar for users to select which KRIs they wish to simulate and analyze (e.g., 'Number of unreconciled trades > 5 days', 'Staff turnover', 'System outages', 'Unreconciled items as % of volume', 'Volume per staff').
- **Synthetic Data Generation Parameters**: Located in the sidebar.
    - **Duration**: `st.slider` or `st.number_input` for the number of days to simulate (e.g., default: 30 days, range: 1-365).
    - **Number of Locations**: `st.slider` or `st.number_input` for the number of business locations (e.g., default: 2, range: 1-5).
    - **Base Values**: `st.number_input` widgets for initial values of key metrics (`trades`, `unreconciled`, `staff`).
    - **Volatility**: `st.slider` or `st.number_input` for data randomness (e.g., default: 0.1, range: 0.0-0.5).
    - **Trend Factors**: `st.number_input` widgets for linear trend factors (`trades`, `unreconciled`, `staff`).
- **KRI Thresholds**: Dynamic `st.number_input` widgets will appear in the sidebar for each selected KRI, allowing users to set custom `Amber` and `Red` thresholds.
- **Action Button**: A `st.button` to trigger data generation and analysis once parameters are set (e.g., "Run Simulation"). Alternatively, the application can update automatically on input changes.

**Visualization Components:**
- **Raw Data Table**: `st.dataframe` to display the generated synthetic data and calculated KPIs.
- **Individual KRI Trend Plots**: `st.line_chart` (or interactive libraries like Altair/Plotly) for each selected KRI, showing its value over time with horizontal lines representing the `Amber` and `Red` thresholds.
- **Relationship Plot**: `st.scatter_chart` (or interactive libraries) to visualize the relationship between compounded KRIs, such as 'Unreconciled items per staff' versus 'Volume per staff'.
- **Aggregated KRI Status Chart**: A `st.bar_chart` or `st.dataframe` with conditional formatting (or a Plotly/Seaborn heatmap rendered as an image) displaying the count of 'Green', 'Amber', and 'Red' statuses for aggregated KRIs across locations/metrics.

**Interactive Elements and Feedback Mechanisms:**
- All input widgets will be interactive, allowing users to dynamically change parameters.
- Charts will support interactivity where the environment allows (e.g., zooming, panning, tooltips on data points).
- Clear titles, labeled axes, and legends will be provided for all visualizations, adhering to color-blind friendly palettes and font size $\ge$ 12 pt.
- Loading spinners (`st.spinner`) or progress bars (`st.progress`) will be used to indicate ongoing data generation or computation.
- Error messages will be displayed using `st.error` for invalid inputs or calculation issues.

---

### 3. Additional Requirements

**Real-time Updates and Responsiveness:**
The Streamlit application will leverage its reactive nature to update visualizations and results in near real-time as users adjust input parameters in the sidebar. This ensures an immediate feedback loop for exploratory analysis.

**Annotation and Tooltip Specifications:**
- **Inline Help Text**: Each input widget in the sidebar will include concise `help` text to describe its purpose and expected input format (`st.sidebar.slider(..., help='This parameter controls...')`).
- **Chart Annotations**: Key thresholds (`Amber`, `Red`) will be clearly annotated on trend plots.
- **Interactive Tooltips**: For interactive charts (e.g., Plotly, Altair), tooltips will be enabled to display precise data values upon hovering, enhancing data exploration.

---

### 4. Notebook Content and Code Requirements

This section details the integration of the provided Jupyter Notebook's core logic and functions into the Streamlit application.

**4.1. Core Libraries**
The application will use `pandas` for data manipulation and `numpy` for numerical operations. Plotting libraries such as `plotly.express` or `altair` are recommended for interactive visualizations, with `matplotlib.pyplot` or `seaborn` as potential static fallbacks.

```python
import pandas as pd
import numpy as np
# Potentially import plotly.express as px or altair as alt for visualizations
```

**4.2. Synthetic Data Generation**
This module simulates time-series operational data based on user-defined parameters.

**Description:**
The `generate_synthetic_data` function creates a DataFrame mimicking metrics relevant to operational risk over a specified duration and for multiple locations. This synthetic data is crucial for prototyping KRI models and conducting scenario analysis without sensitive live data.

**Function from Jupyter Notebook:**
```python
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
```

**Streamlit Usage:**
- Inputs (`duration`, `num_locations`, `base_values`, `volatility`, `trend_factors`) will be gathered from `st.sidebar` widgets.
- The `generate_synthetic_data` function will be called to create the `synthetic_df`.
- The raw `synthetic_df` can be displayed using `st.dataframe` in the main content area.

**4.3. KRI Calculation**
This module computes Key Performance Indicators (KPIs) that serve as KRIs from the generated synthetic data.

**Description:**
This section computes two critical KPIs:
1.  **Unreconciled items as % of volume**: Measures operational inefficiency and potential financial risk.
    $$\text{Unreconciled items as % of volume} = \frac{\text{Number of unreconciled trades}}{\text{Volume of Trades}} \times 100$$
2.  **Volume per staff**: Assesses the efficiency of back-office staff.
    $$\text{Volume per staff} = \frac{\text{Volume of Trades}}{\text{Number of Back Office Staff}}$$

**Function from Jupyter Notebook:**
```python
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
```

**Streamlit Usage:**
- The `calculate_kpis` function will be applied to the `synthetic_df` to produce `kpis_df`.
- The `kpis_df` will be used as the primary data source for KRI status assignment and visualizations.

**4.4. KRI Status Assignment**
This module assigns a risk status (Green, Amber, or Red) to each KRI based on predefined thresholds.

**Description:**
Assigning a status transforms raw KRI values into actionable risk signals, facilitating prompt identification and exception management. The status is determined as follows:
- `Green` if `KRI Value $\le$ Amber Threshold`
- `Amber` if `Amber Threshold < KRI Value $\le$ Red Threshold`
- `Red` if `KRI Value $>$ Red Threshold`

**Function from Jupyter Notebook:**
```python
def assign_kri_status(dataframe, kri_name, amber_threshold, red_threshold):
    """Assign KRI status based on thresholds."""
    if dataframe.empty:
        dataframe['kri_value_status'] = []
        return dataframe

    dataframe['kri_value_status'] = dataframe[kri_name].apply(
        lambda x: 'Green' if x <= amber_threshold else ('Amber' if x <= red_threshold else 'Red')
    )
    return dataframe
```

**Streamlit Usage:**
- This function will be called iteratively for each KRI selected by the user, applying the user-defined `amber_threshold` and `red_threshold` for that specific KRI.
- The resulting dataframe with the `kri_value_status` column will be used for trend plots (showing status zones) and for aggregation.

**4.5. Aggregating KRI Statuses for Visualization**
This module aggregates KRI statuses to provide a consolidated organizational risk view.

**Description:**
Aggregating KRI statuses helps in holistic risk assessment and prioritization of mitigation efforts by summarizing the counts of 'Green', 'Amber', and 'Red' statuses across selected KRIs or business units.

**Function from Jupyter Notebook:**
```python
def aggregate_kri_status(dataframe, kri_list):
    """Aggregates KRI statuses for visualization."""
    if not kri_list:
        return None

    df = dataframe.copy()
    result = pd.DataFrame()

    for kri in kri_list:
        if kri not in df.columns:
            raise KeyError(f"KRI column '{kri}' not found in dataframe.")

        # Ensure that the KRI column contains status strings before counting
        # (This implies assign_kri_status has already been applied)
        if not all(isinstance(x, str) for x in df[kri]):
            # Assuming 'kri_value_status' is the column after assignment
            # The notebook's example aggregates on KRI name itself after it has been assigned status
            # We need to adapt this for the streamlit context to use the assigned status column.
            # For the purpose of this spec, assume kri_list refers to columns *with* status
            # Or, we'll re-assign status for aggregation purposes in Streamlit.
            # The current function as is from the notebook takes kri_list as column names
            # and expects those columns to contain string statuses.
            # A pragmatic approach for Streamlit would be to iterate through selected KRIs,
            # apply assign_kri_status for each, then aggregate the *resulting status columns*.
            # Let's adjust this for clarity: The aggregated_status_df will summarize the counts of 'Green', 'Amber', 'Red'
            # for the *status column* associated with each KRI, not the raw KRI value column.
            # The example notebook usage for `aggregate_kri_status` passes `kpis_df` and `kri_list_to_aggregate`
            # which are raw KRI names. This means `assign_kri_status` needs to be run *before* this aggregate function,
            # and the `kri_list` passed here should be the *status* columns (e.g., 'Unreconciled items as % of volume_status').

            # For consistency with the notebook's example usage where `assign_kri_status` directly modifies
            # the original DataFrame's column to 'kri_value_status',
            # the `aggregate_kri_status` function expects the *status column name* in `kri_list`.
            # Let's assume `kri_list` will contain the names of the *status columns* that were created.
            pass # The original notebook code directly checked `df[kri]` for string values.
                 # This implies `df[kri]` should be the status column itself for the aggregation to work as written.

        status_counts = df[kri].value_counts().to_dict()
        for status in ['Green', 'Amber', 'Red']:
            count = status_counts.get(status, 0)
            result[f'{kri}_{status}'] = [count]

    return result
```

**Streamlit Usage:**
- After applying `assign_kri_status` to create status columns for relevant KRIs, the `aggregate_kri_status` function will be used.
- The `kri_list` for this function will contain the names of the status columns (e.g., 'Unreconciled items as % of volume_status', 'Volume per staff_status').
- The `aggregated_status_df` will be used to generate a bar chart or heatmap visualization using `st.bar_chart` or other plotting libraries.

**4.6. KRI Data Fields Exploration**
This section provides a reference table for understanding common KRI data fields.

**Description:**
A static table outlining various attributes, descriptions, and uses of KRI data fields, as presented in the PRMIA Handbook.

**Content from Jupyter Notebook (Markdown Table):**
A pandas DataFrame will be created from this content in the Streamlit application.

| Attribute             | Description                                                                                             | Use                                                                                        |
| :-------------------- | :------------------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------- |
| Measures/Description  | Number, value, duration, percent, rating, issue, etc. associated with KRI                               | Describes data attributes and determines what data might be aggregated                     |
| KRI Construction      | Methodology for computation of KRI from source data where KRI is a derived calculation or a linked/compound KRI | Details the construction and data sources used for each KRI                                |
| Reported by           | Business area or function reporting the data                                                            | Clarifies workflow, provides audit trail by reporter                                       |
| Reported for          | Relevant org unit(s)/entity(ies)                                                                        | Explains dependencies and allows for reporting cuts of risk profile by management area, risk, product, process |
| Risk Category(ies)    | Relevant category(ies) of risk                                                                          | Allows for causal analysis of business/top risk drivers                                    |
| Relevant Product(s)   | Applicable product(s) the KRI is used for                                                               | -                                                                                          |
| Relevant Process(es)  | Applicable process(es) that the KRI is linked to                                                        | -                                                                                          |
| Reporting Frequency   | Daily, weekly, monthly, etc.                                                                            | Workflow for monitoring                                                                    |
| Reporting Period      | Data cut off (e.g., month end)                                                                          | Allows trending analysis to be performed                                                   |
| Submission Date       | Reporting submission deadline                                                                           | For review, committees, etc.                                                               |
| Causal Event Category | KRI linkage to a business risk or operational risk cause                                                | Allows for causal analysis of business/top risk drivers                                    |
| Data Thresholds       | KRI tolerances, red and amber levels                                                                    | Defines risk appetite and drives action/mitigation                                         |
| Comment Field         | Mandatory for any breaches                                                                              | Explains data/breaches                                                                     |
| KRI Priority          | Risk level/importance                                                                                   | Highlights data/issues for relevant management level                                       |
| Threshold Breach Path | Escalation workflow                                                                                     | -                                                                                          |

**Streamlit Usage:**
- This table will be converted into a pandas DataFrame and displayed using `st.dataframe` in a dedicated section (e.g., a "Reference" tab).

**References:**
[1] Chapter 5: Risk Information, PRMIA Operational Risk Manager Handbook, https://www.e-education.psu.edu/earth107/sites/www.e-education.psu.edu.earth107/files/Unit2/Mod4/Module4LabWorksheet_Rev-12-16-24.pdf.