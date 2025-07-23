import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# -------------------------------------------------------------
# Helper functions (taken from your original pages)
# -------------------------------------------------------------
def run_page1():
    @st.cache_data
    def generate_synthetic_data(duration, num_locations,
                                base_values, volatility, trend_factors):
        """Return a DataFrame with synthetic operational metrics."""
        dates = pd.date_range(start='2023-01-01', periods=duration)
        data = []
        for loc in range(num_locations):
            for date in dates:
                days = (date - dates[0]).days
                trades = base_values['trades'] * (
                    1 + np.random.normal(0, volatility)
                    + trend_factors['trades'] * days
                )
                unreconciled = base_values['unreconciled'] * (
                    1 + np.random.normal(0, volatility)
                    + trend_factors['unreconciled'] * days
                )
                staff = base_values['staff'] * (
                    1 + np.random.normal(0, volatility)
                    + trend_factors['staff'] * days
                )

                data.append({
                    'Date': date,
                    'Location': f'Location {loc+1}',
                    'Volume of Trades per day': max(0, int(trades)),
                    'Number of unreconciled trades > 5 days': max(0, int(unreconciled)),
                    'Staff turnover': max(0, int(staff)),
                    'System outages': np.random.randint(0, 2),
                    'Number of Back Office Staff': max(1, int(staff*5))
                })
        return pd.DataFrame(data)


    def calculate_kpis(df):
        """Add derived KRI columns."""
        if df.empty:
            return df
        df['Unreconciled items as % of volume'] = (
            df['Number of unreconciled trades > 5 days']
            / df['Volume of Trades per day'].replace(0, np.nan)
        ).fillna(0) * 100

        df['Volume per staff'] = (
            df['Volume of Trades per day']
            / df['Number of Back Office Staff'].replace(0, np.nan)
        ).fillna(0)
        return df


    def assign_kri_status(df, kri, amber, red):
        """Return df with a status column for the selected KRI."""
        col = f'{kri} status'
        df[col] = df[kri].apply(
            lambda x: 'Green' if x <= amber else
                    ('Amber' if x <= red else 'Red')
        )
        return df, col


    # -------------------------------------------------------------
    # Main page
    # -------------------------------------------------------------
    st.title("Key Risk Indicator Framework Simulator")

    st.markdown("""
    Use the **sidebar** to configure synthetic data and KRI thresholds, then scroll down to explore generated tables and charts.
    """)

    # 1. Sidebar – data inputs
    st.sidebar.header("Data generation")
    duration = st.sidebar.slider("Days of data", 10, 365, 60)
    num_locations = st.sidebar.slider("Number of locations", 1, 5, 2)

    st.sidebar.markdown("##### Base values")
    base_vals = {
        'trades': st.sidebar.number_input("Base trades / day", 1000),
        'unreconciled': st.sidebar.number_input("Base unreconciled", 30),
        'staff': st.sidebar.number_input("Base staff turnover", 8)
    }

    st.sidebar.markdown("##### Volatility and trend")
    vol = st.sidebar.slider("Volatility", 0.0, 0.5, 0.1)
    trend_vals = {
        'trades': st.sidebar.number_input("Trend trades", 0.01),
        'unreconciled': st.sidebar.number_input("Trend unreconciled", -0.005),
        'staff': st.sidebar.number_input("Trend staff", 0.001)
    }

    st.sidebar.header("KRI choices")
    all_kri = ['Number of unreconciled trades > 5 days', 'Staff turnover',
            'System outages', 'Unreconciled items as % of volume',
            'Volume per staff']
    selected_kri = st.sidebar.multiselect(
        "Pick KRIs to analyse", all_kri,
        default=['Number of unreconciled trades > 5 days', 'Staff turnover']
    )

    st.sidebar.markdown("##### Thresholds (apply to the first selected KRI)")
    amber_thr = st.sidebar.number_input("Amber threshold", value=70.0)
    red_thr = st.sidebar.number_input("Red threshold", value=85.0)

    # 2. Generate data
    st.markdown("### 1. Generate synthetic data")
    if st.button("Run simulation"):
        df = generate_synthetic_data(duration, num_locations,
                                    base_vals, vol, trend_vals)
        st.success("Data generated")
        st.dataframe(df.head(n=20))
        st.markdown("""#### Synthetic Data Preview
This table shows the first few rows of the simulated operational dataset you just created.  
Each row represents one day of activity for a specific location, including trade volumes, unreconciled items, staff turnover, outages, and supporting head‑count.
""")
        st.markdown("""
By scanning these rows you can sanity‑check magnitudes—e.g., do trades fall near the intended base value, does unreconciled volume look realistic, and are dates and locations populated as expected?  Any obvious anomalies here suggest revisiting the sidebar parameters before moving on to KPI analysis.
""")
    else:
        st.warning("Click **Run simulation** to create data before continuing")
        st.stop()

    # 3. Calculate KPIs
    st.markdown("### 2. Calculate derived KRIs")
    df = calculate_kpis(df)
    st.dataframe(df[selected_kri + ['Date', 'Location']].head(n=20))
    st.markdown("""
This table adds the calculated KRIs (e.g., “Unreconciled% of volume”, “Volume per staff”) to the raw data.  
Only the KRIs you selected in the sidebar are displayed, alongside Date and Location.

Seeing the derived columns lets you verify that transformations—such as percentages and per‑staff ratios—behave sensibly (no divide‑by‑zero artefacts, extreme outliers, or missing values).  These computed KRIs feed directly into status scoring and trend visualisations, so confirming their reasonableness here prevents garbage‑in/garbage‑out further downstream.

""")
    # 4. Trend chart
    st.markdown("### 3. Trend view for first selected KRI")
    if not selected_kri:
        st.error("Please select at least one KRI in the sidebar.")
        st.stop()
        
    st.markdown("""
                ##### What You’re Looking At
The line graph tracks the first selected KRI across time for every location.  
Horizontal Amber and Red lines mark the warning and breach thresholds you set.
""")

    kri_focus = selected_kri[0]
    df, status_col = assign_kri_status(df, kri_focus, amber_thr, red_thr)

    fig_line = px.line(df, x="Date", y=kri_focus, color="Location",
                    title=f"{kri_focus} over time")
    fig_line.add_hline(y=amber_thr, line=dict(color="orange"),
                    annotation_text="Amber threshold")
    fig_line.add_hline(y=red_thr, line=dict(color="red"),
                    annotation_text="Red threshold")
    st.plotly_chart(fig_line, use_container_width=True)
    st.markdown("""
This time‑series picture reveals whether the chosen KRI is drifting toward—or oscillating around—your appetite limits.  Persistent breaches (lines hovering above the red threshold) signal structural process issues; intermittent spikes may hint at seasonal surges or data noise.  Comparing multiple locations lets you pinpoint which sites require immediate attention or best‑practice sharing.
""")    
    
    # 5. Aggregated status
    st.markdown("### 4. Aggregated status count")
    status_counts = df[status_col].value_counts().reindex(['Green', 'Amber', 'Red']).fillna(0)
    status_df = pd.DataFrame({'Status': status_counts.index,
                            'Count': status_counts.values})
    fig_bar = px.bar(status_df, x='Status', y='Count',
                    color='Status', title="Status distribution")
    st.plotly_chart(fig_bar, use_container_width=True)
    st.markdown("""
Aggregating status this way quantifies the *scale* of concern.  A tall Red bar means high‑frequency breaches—not just isolated incidents—indicating a chronic risk condition.  An Amber‑heavy profile suggests exposures that consistently test appetite but seldom cross tolerance, which might warrant pre‑emptive mitigation rather than crisis response.
""")
    
    # 6. KRI data-field reference
    with st.expander("KRI data-field reference"):
        st.markdown("""
    Below is a quick reference of common data-field definitions used for KRIs.
    """)
        ref = {
            'Attribute': ['Measures / description', 'KRI construction',
                        'Reported by', 'Reporting frequency', 'Thresholds'],
            'Description': ["Raw metric, percent, count, etc.",
                            "Formula or transformation used to compute the KRI",
                            "Business area providing data",
                            "Daily, monthly, quarterly",
                            "Green–Amber–Red levels that trigger escalation"]
        }
        st.dataframe(pd.DataFrame(ref))
        st.markdown("""
        Keeping these definitions handy ensures consistency and auditability when KRIs move from sandbox to production dashboards.  Clear metadata supports lineage tracing, comparability across business lines, and faster regulator or audit reviews—ultimately strengthening the governance framework that underpins the numerical insights seen above.
        """)
