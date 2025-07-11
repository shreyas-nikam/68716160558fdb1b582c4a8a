
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
