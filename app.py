
import streamlit as st

st.set_page_config(page_title="QuLab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab")
st.divider()
st.markdown("""
In this lab, we will explore Key Risk Indicators (KRIs) and their application in operational risk management. This application allows you to simulate KRI data, set thresholds, and analyze the aggregated risk status across different business units. You can also explore the descriptions of standard KRI data fields.

**Key Features:**
- **KRI Configuration**: Select predefined KRIs and set custom Amber and Red alert thresholds.
- **Synthetic Data Generation**: Simulate time-series data for selected KRIs across multiple business locations, including underlying operational metrics.
- **Interactive Dashboards**: Visualize KRI trends over time, highlighting threshold breaches, and examine relationships between compounded KRIs.
- **Aggregated KRI View**: Provides a consolidated view of KRI statuses (Green, Amber, Red) across business units, using an aggregated comparison.
- **KRI Data Fields Exploration**: An interactive table displaying descriptions of standard KRI data fields.
""")

page = st.sidebar.selectbox(label="Navigation", options=["KRI Configuration & Data Generation", "KRI Trend Analysis", "Aggregated KRI Status", "KRI Data Fields Reference"])

if page == "KRI Configuration & Data Generation":
    from application_pages.page1 import run_page1
    run_page1()
elif page == "KRI Trend Analysis":
    from application_pages.page2 import run_page2
    run_page2()
elif page == "Aggregated KRI Status":
    from application_pages.page3 import run_page3
    run_page3()
elif page == "KRI Data Fields Reference":
    from application_pages.page4 import run_page4
    run_page4()
