id: 68716160558fdb1b582c4a8a_user_guide
summary: First lab of Module 4 user_guide
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# Exploring Key Risk Indicators with QuLa

## Introduction to QuLab and Key Risk Indicators
Duration: 00:02

Welcome to QuLab, your interactive guide to understanding Key Risk Indicators (KRIs) in operational risk management. In today's dynamic business environment, identifying and monitoring potential risks is crucial for maintaining stability and ensuring success. Operational risk refers to the risk of loss resulting from inadequate or failed internal processes, people and systems, or from external events.

**Key Risk Indicators (KRIs)** are metrics used to provide an early signal of increasing risk exposure in an organization. Think of them as the "dashboard warning lights" for your business operations. By tracking KRIs, organizations can proactively identify potential problems, anticipate future losses, and take timely corrective actions before minor issues escalate into major crises.

This QuLab application provides a hands-on experience to:
*   **Simulate KRI data**: Understand how operational metrics can lead to KRI values.
*   **Set thresholds**: Define what constitutes a "normal," "cautionary," or "critical" risk level.
*   **Analyze trends**: Visualize how KRIs evolve over time.
*   **Aggregate risk status**: Get a consolidated view of risk across different business units.
*   **Explore KRI definitions**: Understand the standard attributes of KRIs.

By the end of this codelab, you will have a clearer understanding of how KRIs are used to manage operational risk effectively.

## Understanding KRI Data Fields
Duration: 00:03

Before diving into data generation and analysis, it's essential to understand the fundamental attributes that define a KRI. Standardizing KRI definitions ensures consistency and clarity across an organization, making risk reporting more reliable and actionable.

1.  **Navigate to the "KRI Data Fields Reference" page.**
    *   On the left sidebar, locate the "Navigation" dropdown.
    *   Select "KRI Data Fields Reference".

    You will see a table with three columns: "Attribute," "Description," and "Use."

    <aside class="positive">
    This page helps you understand the **standardization** of KRI definitions. Each row describes a specific characteristic or piece of information associated with a KRI, such as how it's measured, who reports it, or its link to risk categories.
    </aside>

2.  **Explore the KRI Data Fields.**
    *   **Attribute**: This column lists the specific characteristic of a KRI, like "Measures/Description" or "Reporting Frequency."
    *   **Description**: This provides a brief explanation of what the attribute entails. For instance, "KRI Construction" describes the methodology for computing the KRI.
    *   **Use**: This explains the practical importance or benefit of including this attribute in KRI documentation. For example, "Data Thresholds" are crucial because they "Define risk appetite and drives action/mitigation."

    Take a moment to scroll through the table and familiarize yourself with these concepts. Understanding these attributes is foundational to properly defining and utilizing KRIs in risk management.

## Configuring KRIs and Generating Synthetic Data
Duration: 00:05

One of the powerful features of QuLab is its ability to generate synthetic (simulated) data. This allows you to experiment with different scenarios without needing real-world data, helping you understand how various factors influence KRI values.

1.  **Navigate to the "KRI Configuration & Data Generation" page.**
    *   On the left sidebar, select "KRI Configuration & Data Generation" from the "Navigation" dropdown.

    On this page, you will see a main section for displaying data and a sidebar for configuration.

2.  **Understand Data Generation Parameters.**
    The sidebar contains parameters that control how the synthetic data is generated:
    *   **Duration (days)**: This slider determines the number of days for which data will be simulated. A longer duration means more data points over time.
    *   **Number of Locations**: This slider specifies how many different business locations the data will be generated for. This helps simulate data across different operational units.
    *   **Base Values**: These are the starting or average values for core operational metrics like "Base Trades," "Base Unreconciled (trades)," and "Base Staff." These are the foundational numbers from which the simulation starts.
    *   **Volatility**: This slider introduces randomness or "noise" into the data. Higher volatility means more fluctuations in the simulated values, mimicking real-world unpredictability.
    *   **Trend Factors**: These inputs determine if the operational metrics show an increasing or decreasing trend over time. For example, a positive trend factor for "Trades" would mean the number of trades generally increases daily.

    <aside class="positive">
    Experimenting with these parameters allows you to simulate a wide range of operational scenarios, from stable environments to rapidly changing or stressful conditions.
    </aside>

3.  **Select Key Risk Indicators (KRIs).**
    *   Under "KRI Selection" in the sidebar, you can choose which specific KRIs you are interested in simulating.
    *   Common KRIs are already provided, such as "Number of unreconciled trades > 5 days" or "Staff turnover." You can select one or multiple.

4.  **Run the Simulation.**
    *   Once you've adjusted the parameters to your liking, click the "Run Simulation" button in the sidebar.
    *   The application will generate a table of synthetic data in the main area. This table includes the simulated values for metrics like "Volume of Trades per day," "Number of unreconciled trades > 5 days," and "Staff turnover" for each date and location. This raw data forms the basis for calculating and analyzing your chosen KRIs.

    Observe the generated data. Notice how the values change over time and across different locations, influenced by the parameters you set.

## Analyzing KRI Trends
Duration: 00:07

Once you have operational data, the next crucial step is to calculate and visualize your KRIs to identify trends and potential breaches of defined risk thresholds.

1.  **Navigate to the "KRI Trend Analysis" page.**
    *   On the left sidebar, select "KRI Trend Analysis" from the "Navigation" dropdown.

    <aside class="negative">
    Please note: For demonstration purposes, this page uses pre-loaded sample data. In a full operational system, this page would typically use the data you generated in the previous step, or real-world data.
    </aside>

2.  **Understand KRI Calculation.**
    This page demonstrates how specific KRIs are derived from underlying operational metrics. For example:
    *   **"Unreconciled items as % of volume"**: This KRI is calculated as:
        $$ \frac{\text{Number of unreconciled trades > 5 days}}{\text{Volume of Trades per day}} \times 100 $$
        This percentage tells you how significant the unreconciled trades are relative to the total trade volume.
    *   **"Volume per staff"**: This KRI is calculated as:
        $$ \frac{\text{Volume of Trades per day}}{\text{Number of Back Office Staff}} $$
        This indicates the efficiency of staff in handling trade volumes.

3.  **Select a KRI for Analysis.**
    *   In the main area, use the "Select KRI" dropdown to choose one of the available KRIs, such as "Number of unreconciled trades > 5 days" or "Unreconciled items as % of volume."

4.  **Set Amber and Red Thresholds.**
    *   Below the KRI selection, you will find "Amber Threshold" and "Red Threshold" input fields. These are critical for defining your risk appetite:
        *   **Amber Threshold**: When a KRI value exceeds this level, it indicates a potential issue requiring attention. It's a "caution" or "warning" sign.
        *   **Red Threshold**: When a KRI value exceeds this level, it signifies a significant problem or critical risk exposure that demands immediate action.

    <aside class="positive">
    Adjust these thresholds to see how they impact the visualization. Different organizations will have different risk appetites, meaning their thresholds for the same KRI might vary.
    </aside>

5.  **Interpret the KRI Trend Chart.**
    *   A line chart will be displayed showing the trend of your selected KRI over time.
    *   **Colored Lines**: Each line represents a different "Location" (if multiple locations are present in the sample data).
    *   **Threshold Lines**: A horizontal orange line indicates the Amber Threshold, and a red line indicates the Red Threshold.
    *   **Status Indicators**: The points on the KRI trend lines are colored to indicate their status:
        *   **Green**: KRI value is below the Amber Threshold.
        *   **Amber**: KRI value is between the Amber and Red Thresholds.
        *   **Red**: KRI value is above the Red Threshold.

    Analyze the chart to identify periods when the KRI crosses thresholds. These crossings signal a change in risk exposure and warrant further investigation. For instance, if "Number of unreconciled trades > 5 days" consistently moves into the Red zone, it indicates a significant operational bottleneck or issue.

## Aggregating KRI Status
Duration: 00:05

While individual KRI trends are important, understanding the overall risk posture across multiple KRIs and business units is equally vital. The "Aggregated KRI Status" page helps consolidate this information into a high-level overview.

1.  **Navigate to the "Aggregated KRI Status" page.**
    *   On the left sidebar, select "Aggregated KRI Status" from the "Navigation" dropdown.

    <aside class="negative">
    Similar to the KRI Trend Analysis page, this section also uses pre-loaded sample data to demonstrate the aggregation functionality. This allows you to see the concept of aggregation in action without needing to generate complex interconnected data across pages.
    </aside>

2.  **Understand KRI Status Aggregation.**
    The core idea here is to count how many times a particular KRI (or status of a KRI) falls into "Green," "Amber," or "Red" categories across all recorded instances or locations. This provides a summary view of where the most significant risks lie.

3.  **Select KRI Statuses for Aggregation.**
    *   Use the "Select KRI Statuses" multiselect box to choose which KRI status columns you want to include in the aggregation. These are typically columns ending with `_status`, such as `KRI1_status` or `KRI2_status` in the sample data.
    *   By default, all available statuses are often pre-selected.

4.  **View Aggregated Data and Chart.**
    *   After selecting, a table will appear, showing the counts for "Green," "Amber," and "Red" statuses for each selected KRI. For example, if you see `KRI1_Green: 5`, it means KRI1 was in a "Green" status 5 times across the sample data.
    *   Below the table, a bar chart visually represents these aggregated counts.
        *   The X-axis shows the different KRIs.
        *   The Y-axis shows the "Count" of occurrences.
        *   The bars are colored by "Status" (Green, Amber, Red).

    <aside class="positive">
    This aggregated view is extremely useful for senior management or risk committees, providing a quick snapshot of the overall operational risk landscape and highlighting areas that require immediate attention (e.g., KRIs with a high number of "Red" or "Amber" statuses).
    </aside>

    Analyze the bar chart to identify which KRIs have the most occurrences in "Amber" or "Red" zones, indicating higher risk areas that need focused attention.

## Conclusion and Further Exploration
Duration: 00:02

Congratulations! You have successfully explored the key functionalities of the QuLab application, gaining a practical understanding of Key Risk Indicators and their role in operational risk management.

You've learned:
*   The fundamental attributes that define and categorize KRIs.
*   How to simulate operational data and configure parameters that influence KRI behavior.
*   How to visualize KRI trends over time, understand the significance of Amber and Red thresholds, and identify risk breaches.
*   How to aggregate KRI statuses to gain a high-level overview of overall risk exposure.

Operational risk management is an ongoing process that requires continuous monitoring and adaptation. Tools like QuLab can greatly assist in this process by providing a clear, interactive way to analyze and communicate risk information.

**Further Exploration:**
*   Return to the "KRI Configuration & Data Generation" page and experiment with different `Volatility` and `Trend Factors`. How do these changes impact the simulated data and, consequently, the potential KRI trends?
*   Imagine a real-world scenario. What operational metrics would be crucial for your business, and how might you define KRIs and their thresholds based on those metrics?
*   Consider how the concepts of KRI aggregation could be extended. Could you aggregate by different attributes, such as "Risk Category" or "Relevant Process"?

We hope this codelab has provided you with valuable insights into the world of Key Risk Indicators and their practical application in managing operational risk. Keep exploring and applying these concepts to enhance your understanding of risk management!