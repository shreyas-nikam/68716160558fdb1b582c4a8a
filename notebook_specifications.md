
### Technical Specification for Jupyter Notebook: Key Risk Indicator (KRI) Framework Simulator

---

**1. Notebook Overview**

This Jupyter Notebook provides an interactive and educational simulation environment for a Key Risk Indicator (KRI) framework. It allows users to define, monitor, and analyze KRIs across different simulated business units, demonstrating their role as early warning tools in operational risk management. The application is designed for risk analysts, operational managers, and students interested in practical KRI implementation and analysis.

#### Learning Goals
- Understand the fundamental role and characteristics of effective Key Risk Indicators (KRIs) in managing operational risk, drawing insights from the PRMIA Operational Risk Manager Handbook [1].
- Learn the practical steps involved in selecting, defining, and continuously monitoring KRIs, including the establishment of thresholds.
- Gain hands-on experience in setting and interpreting `Amber` and `Red` alert thresholds for KRIs to facilitate proactive exception management.
- Analyze the interdependencies between various KRIs and their collective impact on an organization's overall risk profile.
- Explore the differences and uses of `Top-Down` versus `Bottom-Up` KRI approaches in a realistic context [1].
- Comprehend the key insights regarding KRIs and their application, as detailed in the provided document and supporting data.

#### Expected Outcomes
Upon successful interaction with the notebook, users will be able to:
- Configure a simulated KRI framework by selecting from predefined KRIs and customizing their respective thresholds.
- Generate and interpret synthetic time-series data for selected KRIs across multiple simulated business locations.
- Visualize KRI trends over time, clearly showing breaches against defined thresholds using interactive plots.
- Identify and analyze relationships between different KRIs, such as efficiency metrics and risk indicators, through correlation plots.
- Understand the aggregated status (Green, Amber, Red) of multiple KRIs across different business units using consolidated visual displays.
- Explore and understand the purpose and description of various `KRI Data Fields` as described in the PRMIA handbook via an interactive table.
- Appreciate the importance of quantitative KRIs for objective monitoring and their role in driving `Exception Management`.
- Illustrate the utility of `Interdependent KRIs` by enabling comparative analysis of efficiency and risk across different business locations.

---

**2. Mathematical and Theoretical Foundations**

This section details the core concepts, definitions, real-world applications, and the mathematical formulas underpinning the Key Risk Indicator (KRI) framework simulation.

#### 2.1 Key Risk Indicators (KRIs) Defined
A Key Risk Indicator (KRI) is formally defined as a metric utilized to monitor risk exposures at a particular instance or over a specified period. It serves as a vital early warning tool, aiding in the monitoring and mitigation of potential risk exposures [1]. Effective KRIs are characterized by their relevance, quantifiability, consistency, efficiency, and auditability [1]. They are crucial for proactively identifying emerging risks and enabling timely management intervention.

#### 2.2 KRI Status Determination
The status of a KRI is determined by comparing its `KRI Value` against predefined `Amber` and `Red` `Thresholds`. These thresholds are set to align with the organization's risk appetite and serve as triggers for management action [1].

The KRI status is categorized as follows:
-   **`Green`**: Denotes that the KRI value is within an acceptable range, indicating a low-risk scenario.
    $$ \text{Status} = \text{Green} \quad \text{if} \quad \text{KRI Value} \le \text{Amber Threshold} $$
-   **`Amber`**: Indicates that the KRI value has entered a cautionary zone, suggesting a moderate risk exposure that warrants close monitoring or minor corrective actions.
    $$ \text{Status} = \text{Amber} \quad \text{if} \quad \text{Amber Threshold} < \text{KRI Value} \le \text{Red Threshold} $$
-   **`Red`**: Signifies that the KRI value has exceeded the highest risk tolerance, indicating a critical risk exposure that requires immediate attention and significant mitigation efforts.
    $$ \text{Status} = \text{Red} \quad \text{if} \quad \text{KRI Value} > \text{Red Threshold} $$

#### 2.3 Compound KRI Calculations
Certain KRIs are composite metrics, derived from the relationship between multiple underlying data points. These `Interdependent KRIs` offer a more comprehensive perspective on operational efficiency and risk, facilitating comparative analysis across different business units or locations [1].

##### Unreconciled items as % of volume
This KRI quantifies the proportion of unreconciled trades relative to the total volume of trades. It is a critical indicator of processing efficiency and potential operational risk, where a higher percentage signals increased backlog, potential errors, or financial losses.
$$ \text{Unreconciled items as % of volume} = \frac{\text{Number of unreconciled trades}}{\text{Volume of Trades}} \times 100 $$

##### Volume per staff (Efficiency Metric)
This metric evaluates the operational efficiency of a business unit by measuring the volume of work, such as trades, processed per staff member. It serves as an important efficiency KRI, often correlated with risk indicators to assess the balance between operational output and associated risks.
$$ \text{Volume per staff} = \frac{\text{Volume of Trades}}{\text{Number of Back Office Staff}} $$

#### 2.4 Top-Down vs. Bottom-Up KRI Approaches
The framework for KRI selection and implementation can adopt two primary approaches [1]:
-   **`Top-Down`**: In this approach, KRIs are typically defined at a strategic level by senior management or the board. The focus is on material external and internal loss exposures and overarching strategic and regulatory objectives. These KRIs are usually fewer, highly aggregated, and reported less frequently (e.g., monthly or quarterly). Their primary utility lies in understanding and managing changes in the broader business environment, particularly during periods of stress [1].
-   **`Bottom-Up`**: This approach involves the identification of KRIs by local operational risk teams or line management. These KRIs are directly linked to internal loss events at the specific legal entity, country, business, or product level. They are often informed by key controls or weaknesses identified through risk assessments and audit reports. `Bottom-Up` KRIs are more granular, numerous, and reported more frequently (e.g., daily or weekly). Their main purpose is to manage and monitor daily operational risks and assess the quality and capacity of specific processes [1].

This simulation will primarily demonstrate aspects of a `Bottom-Up` approach, showcasing how specific KRIs are monitored at a detailed level and contribute to an understanding of risk at individual business unit levels.

#### 2.5 KRI Data Fields
A comprehensive set of `KRI Data Fields` is essential for the consistent definition, collection, analysis, and reporting of KRI data. These fields ensure data integrity, auditability, and provide the necessary context for effective risk management decisions [1]. Key fields include: `Measures/Description`, `KRI Construction`, `Reported by`, `Reported for`, `Risk Category(ies)`, `Relevant Product(s)`, `Relevant Process(es)`, `Reporting Frequency`, `Reporting Period`, `Submission Date`, `Causal Event Category`, `Data Thresholds`, `Comment Field`, `KRI Priority`, and `Threshold Breach Path`. An interactive table will allow users to explore these definitions and their practical applications.

---

**3. Code Requirements**

This section outlines the technical specifications for implementing the Key Risk Indicator (KRI) Framework Simulator in a Jupyter Notebook, detailing the required libraries, input/output structures, core algorithms, and visualization components. No actual Python code will be provided.

#### 3.1 Expected Libraries
The notebook will utilize widely adopted, open-source Python libraries available on PyPI, selected for their efficiency in data handling, numerical computation, and high-quality visualization capabilities.

-   **`pandas`**: Essential for efficient data structuring, manipulation, and analysis of time-series data and tabular KRI reports.
-   **`numpy`**: Provides fundamental numerical operations, particularly useful for generating synthetic data and complex mathematical calculations.
-   **`matplotlib.pyplot`**: A foundational library for creating static plots, used as a fallback for visualizations.
-   **`seaborn`**: Built on Matplotlib, it offers a high-level interface for drawing attractive and informative statistical graphics, supporting color-blind friendly palettes.
-   **`plotly.express` / `plotly.graph_objects`**: The primary library for generating interactive visualizations, including trend plots, scatter plots, and heatmaps, enhancing user engagement and data exploration.
-   **`ipywidgets`**: Facilitates the creation of interactive user interface controls (e.g., sliders, dropdowns, text inputs) directly within the notebook environment, enabling dynamic scenario analysis.

#### 3.2 Input/Output Expectations

##### 3.2.1 Input
The simulation will rely on dynamically generated synthetic data based on user inputs, supplemented by an optional lightweight sample dataset.

-   **User-defined parameters (via `ipywidgets`):**
    -   **Simulation Duration**: Numeric input for the number of periods (e.g., days, weeks, months) to simulate.
    -   **Number of Business Locations**: Integer input (e.g., 2 for 'Location A', 'Location B').
    -   **Base Values for Metrics**: Numeric inputs for starting values of underlying metrics such as `Volume of Trades`, `Number of unreconciled trades`, and `Number of Back Office Staff`.
    -   **Volatility Factors**: Numeric inputs to control the randomness and fluctuation in the generated time-series data.
    -   **Trend Factors**: Optional numeric inputs to introduce a linear or seasonal trend to the underlying metrics over time.
    -   **KRI Selection**: Multi-select dropdown or checkboxes to choose from predefined KRIs: `Number of unreconciled trades > 5 days`, `Staff turnover`, `System outages`, `Unreconciled items as % of volume`, `Volume per staff`.
    -   **Threshold Configuration**: Numeric inputs for `Amber` and `Red` thresholds for each selected KRI, configurable per location or globally. Default values will be provided based on the handbook's examples or reasonable assumptions.

-   **Optional Sample Data**: A lightweight (≤ 5 MB) CSV file containing pre-generated synthetic data will be provided. This allows the notebook to run out-of-the-box, even if the user skips interactive parameter input for data generation. The notebook will include validation steps to:
    -   Confirm expected column names and data types.
    -   Assert uniqueness of primary keys.
    -   Verify no missing values in critical data fields, logging summary statistics for numeric columns.

##### 3.2.2 Output
The notebook will generate and display comprehensive outputs derived from the simulation.

-   **Generated Dataframes**: Pandas DataFrames containing the simulated time-series data for both underlying metrics and calculated KRIs.
-   **KRI Status Reports**: Tabular summaries displaying the calculated KRI values alongside their determined `Green`, `Amber`, or `Red` statuses for selected periods or the most recent period.
-   **Visualizations**: All plots and charts as detailed in section 3.4.
-   **Summary Statistics**: Descriptive statistics for all generated data and calculated KRI values (e.g., mean, median, standard deviation, min, max).

#### 3.3 Algorithms and Functions (High-Level Description)

The core logic of the notebook will be structured into distinct, modular functions to ensure clarity and maintainability.

1.  **`generate_synthetic_data(duration, num_locations, base_values, volatility, trend_factors)`**:
    *   **Purpose**: To simulate time-series data for the fundamental operational metrics over a specified period across multiple business locations.
    *   **Logic**:
        *   Initialize data series for each location and metric with the provided `base_values`.
        *   Apply random fluctuations (e.g., using a normal or Poisson distribution) to simulate day-to-day variability.
        *   Incorporate optional `trend_factors` to model growth, seasonality, or decline over the simulation period.
        *   Ensure data realism by constraining values (e.g., non-negative counts, integer staff numbers).
        *   Generate data for fields such as `Date`, `Location`, `Volume of Trades per day`, `Number of unreconciled trades > 5 days`, `Staff turnover`, `System outages`, and `Number of Back Office Staff`.
        *   Return a pandas DataFrame containing the simulated data.

2.  **`calculate_kpis(dataframe)`**:
    *   **Purpose**: To compute all specified Key Risk Indicators, including compound ones, from the generated underlying data.
    *   **Logic**:
        *   Calculate `Unreconciled items as % of volume` using the formula: $ \frac{\text{Number of unreconciled trades}}{\text{Volume of Trades}} \times 100 $. Implement robust error handling for division by zero.
        *   Compute `Volume per staff` (Efficiency Metric) using the formula: $ \frac{\text{Volume of Trades}}{\text{Number of Back Office Staff}} $. Include handling for zero staff.
        *   Directly include `Number of unreconciled trades > 5 days`, `Staff turnover`, and `System outages` as core KRIs.
        *   Append new columns for each calculated KRI to the input DataFrame.
        *   Return the DataFrame augmented with KRI values.

3.  **`assign_kri_status(dataframe, kri_name, amber_threshold, red_threshold)`**:
    *   **Purpose**: To categorize the calculated KRI values into `Green`, `Amber`, or `Red` statuses based on user-defined thresholds.
    *   **Logic**:
        *   Apply the KRI status determination rules (as defined in Section 2.2) to each KRI value for the given `kri_name`.
        *   Create a new column in the DataFrame, populating it with the assigned status for the specified KRI.
        *   Return the DataFrame with the added status column.

4.  **`aggregate_kri_status(dataframe, kri_list)`**:
    *   **Purpose**: To provide an aggregated overview of KRI statuses across different dimensions, such as locations or overall portfolio.
    *   **Logic**:
        *   Count the occurrences of `Green`, `Amber`, and `Red` statuses for each selected KRI across all locations or within a specified time window.
        *   Optionally, implement a rule-based system to derive a composite risk status for each location or the entire portfolio (e.g., if any KRI is `Red`, the overall status is `Red`).
        *   Return a summarized DataFrame suitable for heatmap or bar chart visualization.

#### 3.4 Visualization Requirements

The notebook will generate several types of plots and tables, adhering to strict aesthetic and usability guidelines to ensure clarity, accessibility, and interactivity. Visualizations will adopt a color-blind-friendly palette, maintain a font size of at least $12$ pt, and feature clear titles, labeled axes, and legends.

1.  **Trend Plot (Line Chart with Thresholds)**
    *   **Purpose**: To visually track the time-series performance of individual KRIs and highlight instances where KRI values breach predefined `Amber` and `Red` thresholds.
    *   **Inputs**: User-selected KRI, associated `Amber` and `Red` thresholds, and the simulated time-series data.
    *   **Output**: A line chart displaying the KRI value over time, segmented by location. Horizontal lines will clearly mark the `Amber` and `Red` thresholds. Areas representing breaches (i.e., KRI values exceeding thresholds) will be visually emphasized using distinct colors or shaded regions.
    *   **Interactivity**: Enable hover-over functionality to display exact KRI values and dates, along with zoom and pan capabilities for detailed inspection.
    *   **Fallback**: A static PNG image of the plot will be saved and displayed if interactive rendering is not supported.

2.  **Relationship Plot (Scatter Plot)**
    *   **Purpose**: To explore and visualize the correlation or relationship between two user-selected KRIs, such as `Unreconciled items per staff` versus `Volume per staff`.
    *   **Inputs**: Two user-selected KRIs and the simulated data.
    *   **Output**: A scatter plot where each point represents a data instance (e.g., a specific day for a particular location). Points can be distinctively color-coded based on the business location or a derived KRI status for enhanced insight.
    *   **Interactivity**: Provide hover-over details for individual data points, as well as zoom and pan functionalities.
    *   **Fallback**: A static PNG image of the plot will be saved and displayed.

3.  **Aggregated KRI Comparison (Heatmap or Bar Chart)**
    *   **Purpose**: To present a consolidated view of the status (`Green`, `Amber`, `Red`) of multiple KRIs across different business units or aggregated over a defined time period.
    *   **Inputs**: A list of selected KRIs, the simulated data, and a specified aggregation period (e.g., latest daily status, weekly average status).
    *   **Output (Heatmap Option)**: A matrix where rows represent KRIs and columns represent business locations (or vice versa). Each cell will be colored according to the KRI's status (`Green`, `Amber`, `Red`) for that specific KRI in that location.
    *   **Output (Bar Chart Option)**: Bar charts illustrating the count or proportion of `Green`, `Amber`, and `Red` statuses for each KRI, or a summary of statuses per location.
    *   **Interactivity**: Enable hover-over functionality to reveal precise status details or underlying values.
    *   **Fallback**: A static PNG image of the plot will be saved and displayed.

4.  **KRI Data Fields Exploration (Interactive Table)**
    *   **Purpose**: To allow users to interactively explore the comprehensive definitions and practical uses of various `KRI Data Fields` as detailed in the PRMIA Operational Risk Manager Handbook.
    *   **Inputs**: A predefined dictionary or pandas DataFrame containing the `Attribute`, `Description`, and `Use` for each KRI data field.
    *   **Output**: An interactive table displaying these three columns, providing a structured reference.
    *   **Interactivity**: Incorporate features such as search, sort, and filter capabilities to facilitate easy navigation and information retrieval within the table.

#### 3.5 General Visualization Style and Usability
-   **Color Palette**: A color-blind-friendly palette will be consistently applied across all visualizations.
-   **Font Size**: All textual elements, including titles, axis labels, and legends, will have a minimum font size of $12$ pt to ensure optimal readability.
-   **Clarity**: Plots will feature clear, descriptive titles, appropriately labeled axes, and comprehensive legends.
-   **Interactivity**: For plots generated with Plotly, interactive features such as zoom, pan, and hover tooltips will be enabled to enhance user exploration.
-   **Static Fallback**: To ensure accessibility across different environments, a static image (PNG format) of each core visualization will be generated and displayed alongside or as an alternative to interactive plots.

---

**4. Additional Notes or Instructions**

#### 4.1 Assumptions
-   The synthetic time-series data generated will represent regular intervals (e.g., daily, weekly).
-   All user-provided threshold values are assumed to be valid numeric inputs that align logically with the nature of the KRIs.
-   The mathematical relationships and proportionality between underlying metrics for compound KRI calculations are linear as per the specified formulas.
-   This notebook is designed purely for educational and simulation purposes and is not intended to be a substitute for, or directly deployed as, a real-world operational risk management system.

#### 4.2 Constraints
-   **Performance**: The entire notebook, from data generation to final visualization, must execute efficiently on a mid-spec laptop (8 GB RAM) within a maximum duration of 5 minutes. This mandates optimized data processing and visualization routines.
-   **Library Usage**: The implementation must exclusively use open-source Python libraries available via PyPI.
-   **Documentation**: All significant logical steps within the notebook will be thoroughly documented through:
    -   Inline code comments explaining *what* specific lines or blocks of code accomplish.
    -   Accompanying narrative Markdown cells that describe *what* is happening at each major step and *why* it is being performed, providing context within the KRI framework.

#### 4.3 Customization Instructions
-   **Interactive Parameters**: Users will be provided with intuitive `ipywidgets` (sliders, dropdowns, text inputs) at the beginning of the notebook to customize various aspects of the simulation:
    -   Adjust the duration of the simulated period.
    -   Modify the initial base values and volatility parameters for underlying metrics to create diverse scenarios.
    -   Select specific KRIs to be generated, analyzed, and visualized from a predefined list.
    -   Set and experiment with `Amber` and `Red` thresholds for each selected KRI, enabling robust scenario analysis of risk appetite.
    -   Choose the specific business locations to include in the analysis.
-   **Inline Help/Tooltips**: Each interactive control will feature inline help text or tooltips, clearly describing its function, valid input ranges, and the potential impact of its adjustment on the simulation and analysis, thereby enhancing the learning experience.

#### 4.4 References
This interactive lab draws its conceptual framework and specific examples from:

[1] Chapter 5: Risk Information, PRMIA Operational Risk Manager Handbook, https://www.e-education.psu.edu/earth107/sites/www.e-education.psu.edu.earth107/files/Unit2/Mod4/Module4LabWorksheet_Rev-12-16-24.pdf. This chapter serves as the primary source detailing Key Risk Indicators, their selection, implementation strategies, and their crucial role in monitoring risk exposure within an organization.

All mathematical formulas, including those for KRI status determination and compound KRI calculations, are explicitly detailed in the "Mathematical and Theoretical Foundations" section. This ensures clarity, traceability, and a deep understanding of the underlying principles guiding the lab's simulations.

---
