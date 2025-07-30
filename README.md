
# QuLab: Operational Risk Management with Key Risk Indicators

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://www.streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📊 Project Description

QuLab is an interactive Streamlit application designed for exploring Key Risk Indicators (KRIs) within the context of operational risk management. This lab project allows users to simulate KRI data, configure alert thresholds, analyze trends, and gain aggregated insights into risk statuses across various business units. It also provides a valuable reference for standard KRI data fields, making it a comprehensive tool for understanding and managing operational risk.

## ✨ Key Features

This application offers a suite of functionalities to facilitate operational risk analysis:

*   **KRI Configuration**: Define and select predefined Key Risk Indicators (KRIs) relevant to operational risk. Users can customize Amber and Red alert thresholds for each selected KRI, enabling proactive risk monitoring.
*   **Synthetic Data Generation**: Simulate realistic time-series data for selected KRIs across multiple business locations. The generation includes underlying operational metrics, allowing for a dynamic environment to test KRI behaviors.
*   **Interactive Dashboards**: Visualize KRI trends over time with interactive plots. The dashboards highlight threshold breaches (Amber and Red) and allow for exploration of relationships between compounded KRIs and their underlying metrics.
*   **Aggregated KRI View**: Get a consolidated, high-level overview of KRI statuses (Green, Amber, Red) across different business units. This aggregated comparison helps identify areas of heightened risk at a glance.
*   **KRI Data Fields Exploration**: An interactive table provides clear descriptions of standard KRI data fields, their construction methodologies, and their practical uses in operational risk reporting.

## 🚀 Getting Started

Follow these instructions to get the application up and running on your local machine.

### Prerequisites

*   Python 3.8 or higher
*   `pip` (Python package installer)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/QuantUniversity/QuLab-Streamlit.git
    cd QuLab-Streamlit
    ```
    *(Note: Replace `https://github.com/QuantUniversity/QuLab-Streamlit.git` with the actual repository URL if different.)*

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    *   On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    *   On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4.  **Install the required packages:**
    Create a `requirements.txt` file in the root directory (`QuLab-Streamlit/`) with the following content:

    ```
    streamlit
    pandas
    numpy
    plotly
    ```

    Then, install them using pip:

    ```bash
    pip install -r requirements.txt
    ```

## 🖥️ Usage

Once the prerequisites are installed and the virtual environment is activated, you can run the Streamlit application.

1.  **Run the application:**

    ```bash
    streamlit run app.py
    ```

2.  **Access the application:**
    Your web browser should automatically open to the Streamlit application (usually at `http://localhost:8501`). If it doesn't, copy and paste the URL from your terminal into your browser.

3.  **Navigate the application:**
    *   Use the **sidebar navigation** on the left to switch between different sections of the application:
        *   **KRI Configuration & Data Generation**: Configure KRI parameters, select KRIs, and generate synthetic operational data.
        *   **KRI Trend Analysis**: Visualize trends of selected KRIs, observe threshold breaches (Amber/Red), and analyze relationships.
        *   **Aggregated KRI Status**: View a consolidated summary of KRI statuses across locations.
        *   **KRI Data Fields Reference**: Explore detailed descriptions of standard KRI data attributes.

## 📂 Project Structure

The project is organized into modular components for clarity and maintainability:

```
QuLab-Streamlit/
├── app.py                      # Main Streamlit application entry point
├── requirements.txt            # List of Python dependencies
├── README.md                   # Project documentation
└── application_pages/          # Directory containing individual application pages
    ├── __init__.py             # Initializes the directory as a Python package
    ├── page1.py                # KRI Configuration & Data Generation logic
    ├── page2.py                # KRI Trend Analysis logic
    ├── page3.py                # Aggregated KRI Status logic
    └── page4.py                # KRI Data Fields Reference logic
```

## 🛠️ Technology Stack

This application is built using the following technologies:

*   **Python**: The core programming language.
*   **Streamlit**: The framework used for building the interactive web application.
*   **Pandas**: For data manipulation and analysis.
*   **NumPy**: For numerical operations, especially in synthetic data generation.
*   **Plotly Express**: For creating interactive and visually appealing data visualizations.

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements, new features, or bug fixes, please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name` or `bugfix/issue-description`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add new feature'`).
5.  Push to the branch (`git push origin feature/your-feature-name`).
6.  Open a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
*(Note: A `LICENSE` file containing the MIT License text should be created in the root directory if it doesn't exist.)*

## 📞 Contact

For any inquiries or further information about this project, please contact:

*   **Organization**: QuantUniversity
*   **Website**: [www.quantuniversity.com](https://www.quantuniversity.com/)
*   **Email**: info@qusandbox.com

## License

## QuantUniversity License

© QuantUniversity 2025  
This notebook was created for **educational purposes only** and is **not intended for commercial use**.  

- You **may not copy, share, or redistribute** this notebook **without explicit permission** from QuantUniversity.  
- You **may not delete or modify this license cell** without authorization.  
- This notebook was generated using **QuCreate**, an AI-powered assistant.  
- Content generated by AI may contain **hallucinated or incorrect information**. Please **verify before using**.  

All rights reserved. For permissions or commercial licensing, contact: [info@qusandbox.com](mailto:info@qusandbox.com)
