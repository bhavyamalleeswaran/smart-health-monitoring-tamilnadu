"""
Alert System for Waterborne Disease Early Warning
Tamil Nadu Smart Health Monitoring Project
"""

import joblib
import numpy as np
import pandas as pd
import os

# Get the directory of this file, then go up one level to project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(BASE_DIR, 'models')


def load_models():
    """Load the trained model, scaler, and encoders."""
    model = joblib.load(os.path.join(MODELS_DIR, 'best_model.pkl'))
    scaler = joblib.load(os.path.join(MODELS_DIR, 'scaler.pkl'))
    le_district = joblib.load(os.path.join(MODELS_DIR, 'le_district.pkl'))
    le_season = joblib.load(os.path.join(MODELS_DIR, 'le_season.pkl'))
    return model, scaler, le_district, le_season


def get_season(month):
    """Determine season from month number."""
    if month in [10, 11, 12]:
        return 'NE_Monsoon'
    elif month in [6, 7, 8, 9]:
        return 'SW_Monsoon'
    elif month in [3, 4, 5]:
        return 'Summer'
    else:
        return 'Winter'


def check_outbreak_risk(rainfall_mm, temperature_celsius, pH,
                         turbidity_NTU, coliform_count_per100ml,
                         dissolved_oxygen_mg_L,
                         total_dissolved_solids_mg_L,
                         month, district,
                         cases_last_month=0,
                         cases_2_months_ago=0,
                         rainfall_last_month=0):
    """
    Predict outbreak risk based on water quality and environmental
    parameters.

    Returns a dictionary with risk_level, probability, and
    recommendations.
    """
    model, scaler, le_district, le_season = load_models()

    season = get_season(month)

    try:
        district_encoded = le_district.transform([district])[0]
    except ValueError:
        district_encoded = 0  # default if district not in training data

    season_encoded = le_season.transform([season])[0]

    # Build feature vector in the SAME order as training
    features = pd.DataFrame([{
        'rainfall_mm': rainfall_mm,
        'temperature_celsius': temperature_celsius,
        'pH': pH,
        'turbidity_NTU': turbidity_NTU,
        'coliform_count_per100ml': coliform_count_per100ml,
        'dissolved_oxygen_mg_L': dissolved_oxygen_mg_L,
        'total_dissolved_solids_mg_L': total_dissolved_solids_mg_L,
        'month': month,
        'district_encoded': district_encoded,
        'season_encoded': season_encoded,
        'cases_last_month': cases_last_month,
        'cases_2_months_ago': cases_2_months_ago,
        'rainfall_last_month': rainfall_last_month
    }])

    features_scaled = scaler.transform(features)

    probability = model.predict_proba(features_scaled)[0][1]

    if probability < 0.3:
        risk_level = "LOW"
        emoji = "🟢"
        recommendation = ("Water quality parameters are within safe " +
                          "range. Continue routine monitoring.")
    elif probability < 0.6:
        risk_level = "MEDIUM"
        emoji = "🟡"
        recommendation = ("Increase water testing frequency. Monitor " +
                          "vulnerable populations. Alert local health " +
                          "workers to watch for early symptoms.")
    else:
        risk_level = "HIGH"
        emoji = "🔴"
        recommendation = ("Issue public health advisory immediately. " +
                          "Deploy water purification measures. " +
                          "Increase medical staff readiness in the " +
                          "affected district.")

    return {
        'risk_level': risk_level,
        'emoji': emoji,
        'probability': round(float(probability), 3),
        'recommendation': recommendation,
        'district': district,
        'season': season
    }


if __name__ == "__main__":
    # Quick test when running this file directly
    result = check_outbreak_risk(
        rainfall_mm=250,
        temperature_celsius=30,
        pH=7.2,
        turbidity_NTU=18,
        coliform_count_per100ml=300,
        dissolved_oxygen_mg_L=5,
        total_dissolved_solids_mg_L=600,
        month=11,
        district='Thanjavur'
    )
    print(result)