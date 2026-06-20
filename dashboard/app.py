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

st.markdown("---")
st.caption("Data Source: Tamil Nadu Waterborne Disease Dataset (2018-2024) | "
           "Built with Streamlit | Smart Health Monitoring Project")