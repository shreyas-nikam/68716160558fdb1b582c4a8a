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

    # Introduction Section
    with st.expander("What is a Key Risk Indicator (KRI)?", expanded=True):
        st.markdown("""
        **Key Risk Indicators (KRIs)** are metrics used to provide early warning signals of increasing risk exposure 
        in various areas of an organization. Think of them as a "health check" for your business operations.
        
        **Key Concepts:**
        - **KRI**: A measurable value that indicates potential risk levels
        - **Threshold**: Preset limits that trigger alerts (Amber = Warning, Red = Critical)
        - **Trend Analysis**: Tracking KRI values over time to identify patterns
        - **Status Assignment**: Color-coding system (Green = Safe, Amber = Caution, Red = Action Required)
        
        **Example**: If you have 1000 trades per day and 50 are unreconciled, your "Unreconciled %" KRI would be 5%.
        """)

    st.markdown("---")
    
    # Step-by-step guide
    st.markdown("## How to Use This Lab - Step by Step Guide")
    
    st.markdown("""
    **Step 1: Configure Data Parameters** (Use the sidebar on the left)
    - Set how many days of data you want to simulate
    - Choose number of business locations to analyze
    - Adjust base values for your operational metrics
    
    **Step 2: Generate Synthetic Data**
    - Click the "Run simulation" button below
    - Review the generated data table
    
    **Step 3: Analyze KRI Calculations**
    - Examine how derived KRIs are calculated from raw data
    
    **Step 4: View Trend Analysis**
    - See how your selected KRI performs over time
    - Observe threshold breaches
    
    **Step 5: Review Status Distribution**
    - Understand the overall risk profile through status counts
    """)

    st.markdown("---")

    # 1. Sidebar – data inputs
    st.sidebar.header("Step 1: Data Configuration")
    st.sidebar.markdown("**Time Period and Scope**")
    duration = st.sidebar.slider(
        "Days of data to simulate", 
        min_value=10, max_value=365, value=60,
        help="More days = longer time series for trend analysis"
    )
    num_locations = st.sidebar.slider(
        "Number of business locations", 
        min_value=1, max_value=5, value=2,
        help="Each location represents a different business unit or office"
    )

    st.sidebar.markdown("**Base Operational Values**")
    st.sidebar.caption("These represent typical daily volumes for your business")
    base_vals = {
        'trades': st.sidebar.number_input(
            "Base trades per day", 
            value=1000, min_value=100,
            help="Average number of financial transactions processed daily"
        ),
        'unreconciled': st.sidebar.number_input(
            "Base unreconciled trades", 
            value=30, min_value=0,
            help="Average number of trades not yet matched/verified"
        ),
        'staff': st.sidebar.number_input(
            "Base staff turnover", 
            value=8, min_value=1,
            help="Average number of staff leaving per period"
        )
    }

    st.sidebar.markdown("**Market Dynamics**")
    vol = st.sidebar.slider(
        "Volatility (randomness)", 
        min_value=0.0, max_value=0.5, value=0.1, step=0.01,
        help="Higher values = more day-to-day variation in your data"
    )
    
    st.sidebar.caption("Trend factors control whether metrics increase/decrease over time")
    trend_vals = {
        'trades': st.sidebar.number_input(
            "Daily trade growth rate", 
            value=0.01, step=0.001, format="%.3f",
            help="Positive = growing business, Negative = declining business"
        ),
        'unreconciled': st.sidebar.number_input(
            "Daily unreconciled change rate", 
            value=-0.005, step=0.001, format="%.3f",
            help="Negative = improving reconciliation processes"
        ),
        'staff': st.sidebar.number_input(
            "Daily staff turnover change rate", 
            value=0.001, step=0.001, format="%.3f",
            help="Positive = increasing turnover over time"
        )
    }

    st.sidebar.markdown("---")
    st.sidebar.header("Step 2: KRI Selection and Thresholds")
    
    all_kri = [
        'Number of unreconciled trades > 5 days', 
        'Staff turnover',
        'System outages', 
        'Unreconciled items as % of volume',
        'Volume per staff'
    ]
    
    selected_kri = st.sidebar.multiselect(
        "Select KRIs to analyze", 
        all_kri,
        default=['Number of unreconciled trades > 5 days', 'Staff turnover'],
        help="Choose which risk indicators you want to monitor"
    )

    st.sidebar.markdown("**Alert Thresholds**")
    st.sidebar.caption("These apply to your first selected KRI")
    amber_thr = st.sidebar.number_input(
        "Amber threshold (Warning level)", 
        value=70.0, min_value=0.0,
        help="Values above this trigger a warning status"
    )
    red_thr = st.sidebar.number_input(
        "Red threshold (Critical level)", 
        value=85.0, min_value=0.0,
        help="Values above this trigger a critical alert"
    )
    
    if red_thr <= amber_thr:
        st.sidebar.error("Red threshold must be higher than Amber threshold!")

    # 2. Generate data
    st.markdown("### Step 2: Generate Your Synthetic Dataset")
    
    st.info("""
    **What happens when you click 'Run simulation':**
    - Creates realistic operational data for your specified time period
    - Applies volatility and trends to make data dynamic
    - Generates data for all your selected locations
    """)
    
    if st.button("Run simulation", type="primary"):
        with st.spinner("Generating synthetic operational data..."):
            df = generate_synthetic_data(duration, num_locations,
                                        base_vals, vol, trend_vals)
        st.success(f"Successfully generated {len(df)} rows of operational data!")
        
        st.markdown("#### Raw Operational Data Preview")
        st.dataframe(df.head(20), use_container_width=True)
        
        st.markdown("""
        **Understanding Your Data:**
        - **Date**: Each row represents one business day
        - **Location**: Different business units or offices
        - **Volume of Trades per day**: Total transactions processed
        - **Number of unreconciled trades > 5 days**: Trades awaiting reconciliation
        - **Staff turnover**: Number of employees who left
        - **System outages**: Technical disruptions (0 or 1)
        - **Number of Back Office Staff**: Support staff count
        
        **Data Quality Check**: Verify that the numbers look reasonable for your business context. 
        If values seem too high or low, adjust the base values in the sidebar.
        """)
    else:
        st.warning("Click 'Run simulation' above to generate data and continue with the analysis")
        st.stop()

    # 3. Calculate KPIs
    st.markdown("### Step 3: Calculate Derived KRIs")
    
    with st.expander("Understanding KRI Calculations"):
        st.markdown("""
        **Derived KRIs** are calculated from your raw operational data:
        
        1. **Unreconciled items as % of volume** = (Unreconciled trades ÷ Total trades) × 100
           - *Interpretation*: Higher percentages indicate reconciliation problems
        
        2. **Volume per staff** = Total trades ÷ Number of staff
           - *Interpretation*: Higher values may indicate efficiency or staff overload
        
        These calculations help transform raw numbers into meaningful risk indicators.
        """)
    
    df = calculate_kpis(df)
    
    if selected_kri:
        display_columns = selected_kri + ['Date', 'Location']
        available_columns = [col for col in display_columns if col in df.columns]
        
        st.dataframe(df[available_columns].head(20), use_container_width=True)
        
        st.markdown("""
        **Reviewing Your KRI Values:**
        - Look for any unusually high or low values
        - Check if the calculated percentages make business sense
        - Notice variations between different locations and dates
        
        These derived metrics will be used to determine risk status in the next steps.
        """)
    else:
        st.error("Please select at least one KRI in the sidebar to continue.")
        st.stop()

    # 4. Trend chart
    st.markdown("### Step 4: KRI Trend Analysis Over Time")
    
    if not selected_kri:
        st.error("Please select at least one KRI in the sidebar.")
        st.stop()
        
    kri_focus = selected_kri[0]
    
    st.info(f"""
    **Analyzing: {kri_focus}**
    - **Green Zone**: Values below {amber_thr} (Acceptable risk level)
    - **Amber Zone**: Values between {amber_thr} and {red_thr} (Warning - Monitor closely)
    - **Red Zone**: Values above {red_thr} (Critical - Take immediate action)
    """)

    df, status_col = assign_kri_status(df, kri_focus, amber_thr, red_thr)

    fig_line = px.line(
        df, x="Date", y=kri_focus, color="Location",
        title=f"Trend Analysis: {kri_focus}",
        labels={kri_focus: "KRI Value", "Date": "Time Period"}
    )
    fig_line.add_hline(
        y=amber_thr, line=dict(color="orange", dash="dash"),
        annotation_text=f"Amber Threshold ({amber_thr})"
    )
    fig_line.add_hline(
        y=red_thr, line=dict(color="red", dash="dash"),
        annotation_text=f"Red Threshold ({red_thr})"
    )
    fig_line.update_layout(height=500)
    st.plotly_chart(fig_line, use_container_width=True)
    
    st.markdown("""
    **How to Read This Chart:**
    - **Lines**: Each colored line represents a different business location
    - **Horizontal Lines**: Amber and Red threshold levels
    - **Trend Direction**: Is the KRI generally improving or worsening over time?
    - **Threshold Breaches**: Points where lines cross above the threshold lines indicate risk events
    - **Location Comparison**: Compare which locations perform better or worse
    
    **Key Questions to Ask:**
    - Are there persistent breaches above the red line?
    - Do you see seasonal patterns or one-off spikes?
    - Which locations need immediate attention?
    """)
    
    # 5. Aggregated status
    st.markdown("### Step 5: Overall Risk Status Summary")
    
    status_counts = df[status_col].value_counts().reindex(['Green', 'Amber', 'Red']).fillna(0)
    status_df = pd.DataFrame({
        'Status': status_counts.index,
        'Count': status_counts.values,
        'Percentage': (status_counts.values / status_counts.sum() * 100).round(1)
    })
    
    # Display summary metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
            "Green Days", 
            int(status_counts.get('Green', 0)),
            help="Days when KRI was within acceptable limits"
        )
    with col2:
        st.metric(
            "Amber Days", 
            int(status_counts.get('Amber', 0)),
            help="Days when KRI triggered warnings"
        )
    with col3:
        st.metric(
            "Red Days", 
            int(status_counts.get('Red', 0)),
            help="Days when KRI was in critical status"
        )
    
    fig_bar = px.bar(
        status_df, x='Status', y='Count',
        color='Status', 
        color_discrete_map={'Green': 'green', 'Amber': 'orange', 'Red': 'red'},
        title=f"Risk Status Distribution for {kri_focus}",
        text='Percentage'
    )
    fig_bar.update_traces(texttemplate='%{text}%', textposition='outside')
    fig_bar.update_layout(height=400, showlegend=False)
    st.plotly_chart(fig_bar, use_container_width=True)
    
    st.markdown("""
    **Interpreting Your Risk Profile:**
    - **High Green %**: Good risk management, KRI mostly within acceptable bounds
    - **High Amber %**: Consistent warnings - consider reviewing processes or thresholds  
    - **High Red %**: Serious risk exposure - immediate management attention required
    
    **Management Actions Based on Results:**
    - **Mostly Green**: Continue current monitoring approach
    - **Frequent Amber**: Investigate root causes, consider preventive measures
    - **Regular Red**: Implement immediate controls, review business processes
    """)
    
    # 6. Summary and Next Steps
    st.markdown("### Step 6: Summary and Recommendations")
    
    total_days = len(df)
    red_percentage = (status_counts.get('Red', 0) / total_days * 100)
    amber_percentage = (status_counts.get('Amber', 0) / total_days * 100)
    
    if red_percentage > 20:
        risk_level = "HIGH RISK"
        recommendation = "Immediate action required. Review processes and controls."
        color = "red"
    elif amber_percentage > 30:
        risk_level = "MODERATE RISK"  
        recommendation = "Monitor closely and consider process improvements."
        color = "orange"
    else:
        risk_level = "LOW RISK"
        recommendation = "Continue current monitoring approach."
        color = "green"
    
    st.markdown(f"""
    **Overall Risk Assessment: :{color}[{risk_level}]**
    
    **Recommendation**: {recommendation}
    
    **Key Insights from Your Analysis:**
    - Total observation period: {total_days} days across {num_locations} locations
    - Risk status breakdown: {status_counts.get('Green', 0)} Green, {status_counts.get('Amber', 0)} Amber, {status_counts.get('Red', 0)} Red days
    - Primary KRI analyzed: {kri_focus}
    
    **Next Steps in Real Implementation:**
    1. **Validate Thresholds**: Ensure amber/red levels align with business risk appetite
    2. **Automate Monitoring**: Set up automated alerts for threshold breaches  
    3. **Define Response Procedures**: Create action plans for amber and red status
    4. **Regular Review**: Periodically reassess KRI relevance and threshold levels
    5. **Expand Coverage**: Add more KRIs to get comprehensive risk view
    """)

    # 7. Technical Reference
    with st.expander("Technical Reference: KRI Data Field Definitions"):
        st.markdown("""
        **Standard KRI Data Field Structure:**
        
        Understanding these elements is crucial for implementing KRIs in production systems.
        """)
        
        ref_data = {
            'Field Category': [
                'Data Source', 
                'Calculation Method', 
                'Reporting Unit', 
                'Update Frequency', 
                'Threshold Levels',
                'Status Logic',
                'Escalation Process'
            ],
            'Description': [
                "System or process generating the raw data (e.g., Trading System, HR Database)",
                "Mathematical formula or business rule used to compute the KRI value",  
                "Business unit, geography, or functional area being measured",
                "How often the KRI is calculated and reported (daily, weekly, monthly)",
                "Predetermined values that trigger amber and red alerts",
                "Rules for assigning Green/Amber/Red status based on KRI values",
                "Defined actions and responsibilities when thresholds are breached"
            ],
            'Example for Unreconciled %': [
                "Trade Settlement System",
                "(Unreconciled Trades ÷ Total Trades) × 100", 
                "Back Office Operations - Location A",
                "Daily at 9 AM",
                "Amber: 5%, Red: 10%",
                "Green ≤ 5%, Amber 5-10%, Red > 10%",
                "Amber: Team Lead Review, Red: Manager Investigation"
            ]
        }
        
        st.dataframe(pd.DataFrame(ref_data), use_container_width=True)
        
        st.markdown("""
        **Implementation Best Practices:**
        - **Data Quality**: Ensure source data is accurate and timely
        - **Business Relevance**: KRIs should reflect actual business risks
        - **Actionable Thresholds**: Set levels that trigger meaningful responses
        - **Clear Ownership**: Assign responsibility for monitoring and response
        - **Regular Calibration**: Review and adjust thresholds based on experience
        - **Documentation**: Maintain clear definitions and calculation methods
        """)
