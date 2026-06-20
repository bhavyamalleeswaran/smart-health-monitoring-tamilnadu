"""
Smart Community Health Monitoring & Early Warning System
Tamil Nadu - Streamlit Dashboard
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import os

# Allow importing from src/
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="TN Waterborne Disease Early Warning",
    page_icon="🏥",
    layout="wide"
)

# ---------- LOAD DATA ----------
@st.cache_data
def load_data():
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data',
                              'processed_data.csv')
    df = pd.read_csv(data_path)
    return df

df = load_data()

# ---------- HEADER ----------
st.title("🏥 Smart Community Health Monitoring")
st.subheader("Early Warning System for Waterborne Diseases — Tamil Nadu")
st.markdown("---")

# ---------- SIDEBAR ----------
st.sidebar.header("📍 Filters")

districts = sorted(df['district'].unique())
selected_district = st.sidebar.selectbox(
    "Select District", districts, index=districts.index('Chennai')
    if 'Chennai' in districts else 0
)

years = sorted(df['year'].unique())
selected_years = st.sidebar.multiselect(
    "Select Year(s)", years, default=years
)

st.sidebar.markdown("---")
st.sidebar.info(
    "This dashboard monitors waterborne disease risk across "
    "12 districts in Tamil Nadu using water quality and "
    "environmental data from 2018-2024."
)

# ---------- FILTER DATA ----------
filtered_df = df[
    (df['district'] == selected_district) &
    (df['year'].isin(selected_years))
]

# ---------- KEY METRICS ----------
st.header(f"📊 Overview — {selected_district}")

col1, col2, col3, col4 = st.columns(4)

with col1:
    total_cases = filtered_df['total_disease_cases'].sum()
    st.metric("Total Disease Cases", f"{total_cases:,.0f}")

with col2:
    avg_cases = filtered_df['total_disease_cases'].mean()
    st.metric("Avg Monthly Cases", f"{avg_cases:.0f}")

with col3:
    outbreak_months = filtered_df['outbreak_alert'].sum()
    st.metric("Outbreak Months", f"{outbreak_months:.0f}")

with col4:
    outbreak_rate = filtered_df['outbreak_alert'].mean() * 100
    st.metric("Outbreak Rate", f"{outbreak_rate:.1f}%")

st.markdown("---")

# ---------- DISEASE TREND CHART ----------
st.header("📈 Disease Trend Over Time")

trend_data = filtered_df.sort_values('date')

fig, ax = plt.subplots(figsize=(14, 5))
ax.plot(trend_data['date'], trend_data['total_disease_cases'],
        color='crimson', linewidth=2, marker='o', markersize=3)
ax.set_xlabel('Date')
ax.set_ylabel('Total Disease Cases')
ax.set_title(f'Disease Cases Trend — {selected_district}')
ax.tick_params(axis='x', rotation=45)
plt.tight_layout()
st.pyplot(fig)

st.markdown("---")

# ---------- DISTRICT COMPARISON ----------
st.header("🗺️ District Comparison")

district_summary = df.groupby('district')['total_disease_cases'].sum() \
    .sort_values(ascending=False)

fig2, ax2 = plt.subplots(figsize=(14, 5))
colors = ['crimson' if d == selected_district else 'steelblue'
          for d in district_summary.index]
ax2.bar(district_summary.index, district_summary.values, color=colors)
ax2.set_xlabel('District')
ax2.set_ylabel('Total Cases (2018-2024)')
ax2.set_title('Total Disease Cases by District')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
st.pyplot(fig2)

# ---------- PREDICTION SECTION ----------
st.markdown("---")
st.header("🔮 Predict Outbreak Risk")
st.write("Enter current water quality and environmental parameters "
         "to get a real-time outbreak risk assessment.")

from alert_system import check_outbreak_risk

pred_col1, pred_col2, pred_col3 = st.columns(3)

with pred_col1:
    st.subheader("🌧️ Environmental")
    input_rainfall = st.slider("Rainfall (mm)", 0.0, 400.0, 100.0)
    input_temperature = st.slider("Temperature (°C)", 20.0, 40.0, 30.0)
    input_month = st.selectbox("Month", list(range(1, 13)),
                                index=10,
                                format_func=lambda m: [
                                    'January', 'February', 'March', 'April',
                                    'May', 'June', 'July', 'August',
                                    'September', 'October', 'November',
                                    'December'][m-1])

with pred_col2:
    st.subheader("💧 Water Quality")
    input_pH = st.slider("pH Level", 5.5, 9.0, 7.2)
    input_turbidity = st.slider("Turbidity (NTU)", 0.0, 40.0, 10.0)
    input_coliform = st.slider("Coliform Count (per 100ml)",
                                0.0, 500.0, 100.0)

with pred_col3:
    st.subheader("🧪 Additional Parameters")
    input_do = st.slider("Dissolved Oxygen (mg/L)", 2.0, 10.0, 6.0)
    input_tds = st.slider("Total Dissolved Solids (mg/L)",
                           150.0, 1300.0, 600.0)
    input_district = st.selectbox("District", districts)
    input_cases_last_month = st.slider(
        "Cases Last Month", 0, 200, 50)
    input_cases_2mo_ago = st.slider(
        "Cases 2 Months Ago", 0, 200, 40)

st.markdown("")

if st.button("🔍 Predict Outbreak Risk", type="primary",
              use_container_width=True):
    result = check_outbreak_risk(
        rainfall_mm=input_rainfall,
        temperature_celsius=input_temperature,
        pH=input_pH,
        turbidity_NTU=input_turbidity,
        coliform_count_per100ml=input_coliform,
        dissolved_oxygen_mg_L=input_do,
        total_dissolved_solids_mg_L=input_tds,
        month=input_month,
        district=input_district,
        cases_last_month=input_cases_last_month,
        cases_2_months_ago=input_cases_2mo_ago
    )

    st.markdown("### Prediction Result")

    risk_colors = {
        'LOW': 'success',
        'MEDIUM': 'warning',
        'HIGH': 'error'
    }

    result_col1, result_col2 = st.columns([1, 2])

    with result_col1:
        if result['risk_level'] == 'LOW':
            st.success(f"{result['emoji']} **{result['risk_level']} RISK**")
        elif result['risk_level'] == 'MEDIUM':
            st.warning(f"{result['emoji']} **{result['risk_level']} RISK**")
        else:
            st.error(f"{result['emoji']} **{result['risk_level']} RISK**")

        st.metric("Outbreak Probability",
                  f"{result['probability']*100:.1f}%")

    with result_col2:
        st.write(f"**District:** {result['district']}")
        st.write(f"**Season:** {result['season']}")
        st.write(f"**Recommendation:**")
        st.info(result['recommendation'])

    # Probability bar
    st.progress(result['probability'])

st.markdown("---")
st.caption("Data Source: Tamil Nadu Waterborne Disease Dataset (2018-2024) | "
           "Built with Streamlit | Smart Health Monitoring Project")

# ---------- ABOUT SECTION ----------
st.markdown("---")
with st.expander("ℹ️ About This Project"):
    st.write("""
    **Smart Community Health Monitoring & Early Warning System**
    
    This system was built to predict waterborne disease outbreaks
    (Cholera, Diarrhea, Typhoid, Hepatitis A) across 12 districts
    in Tamil Nadu using water quality and environmental data.
    
    **How it works:**
    - A Random Forest machine learning model analyzes water quality
      parameters (turbidity, coliform count, pH) alongside rainfall
      and seasonal patterns
    - The model predicts outbreak risk 2 weeks in advance
    - Risk levels are categorized as Low, Medium, or High to guide
      public health response
    
    **Tech Stack:** Python, scikit-learn, XGBoost, Streamlit, pandas
    
    **Data Period:** 2018-2024 (1008 monthly records)
    """)