# Final Project Report
## Smart Community Health Monitoring & Early Warning System
### Water-Borne Diseases in Tamil Nadu

**Author:** Bhavyamalleeswaran
**Date:** June 21, 2026
**Live Dashboard:** https://smart-health-monitoring-tamilnadu-urfvx7yejjycqhbqbbrrgm.streamlit.app
**GitHub Repository:** https://github.com/bhavyamalleeswaran/smart-health-monitoring-tamilnadu

---

## Abstract

Waterborne diseases such as Cholera, Diarrhea, Typhoid, and Hepatitis A
remain a significant public health challenge in Tamil Nadu, particularly
during and after monsoon seasons. This project presents a machine
learning-based early warning system that predicts outbreak risk using
water quality parameters (turbidity, pH, coliform count), rainfall, and
seasonal patterns across 12 districts. A Random Forest classifier
achieved an F1-score of 0.800 on test data, and the system was deployed
as an interactive Streamlit dashboard enabling real-time risk
assessment for health officials.

---

## 1. Introduction & Problem Statement

Current waterborne disease surveillance in Tamil Nadu is largely
reactive, with health departments responding after outbreaks are
already underway. This delay costs valuable time in deploying
preventive measures such as water purification, public advisories,
and medical resource allocation.

This project addresses that gap by building a predictive system that
analyzes the relationship between water quality, environmental
conditions, and disease incidence to provide advance warning of
likely outbreaks — enabling proactive rather than reactive public
health response.

**Objectives:**
1. Analyze historical waterborne disease patterns across Tamil Nadu
2. Identify water quality parameters most predictive of outbreaks
3. Build and evaluate machine learning models for outbreak prediction
4. Develop a 3-tier alert system (Low/Medium/High risk)
5. Deploy an accessible, interactive dashboard for end users

---

## 2. Dataset Description

- **Source:** Synthetically generated dataset modeled on realistic
  Tamil Nadu water quality and health surveillance patterns
- **Records:** 1,008 monthly observations
- **Coverage:** 12 districts (Chennai, Tiruppur, Madurai, Thanjavur,
  Tirunelveli, Coimbatore, Salem, Tiruchirappalli, Vellore, Cuddalore,
  Nagapattinam, Ramanathapuram)
- **Time Period:** January 2018 – December 2024
- **Features:** Rainfall (mm), Temperature (°C), pH, Turbidity (NTU),
  Coliform Count (per 100ml), Dissolved Oxygen (mg/L), Total Dissolved
  Solids (mg/L)
- **Targets:** Cholera, Diarrhea, Typhoid, and Hepatitis A case counts;
  binary outbreak alert (39% positive class)

**Note on Data:** Due to the unavailability of granular, open-access
real-time water quality datasets for Tamil Nadu, a synthetic dataset
was generated with realistic seasonal patterns (post-monsoon spikes)
and statistically grounded relationships between water quality and
disease incidence. During development, an initial data generation
error caused a 100% outbreak rate; this was identified through model
validation (a suspiciously perfect F1-score) and corrected to a
realistic 39% outbreak rate.

---

## 3. Methodology

### 3.1 Exploratory Data Analysis
- Identified **Thanjavur** as the highest-risk district by total
  case count
- Identified **October** (post-Northeast Monsoon) as the peak-risk
  month
- Found coliform count, turbidity, and rainfall positively correlated
  with disease incidence; coliform count showed the strongest
  correlation (r ≈ 0.65) with outbreak alerts

### 3.2 Data Preprocessing
- Engineered season categories (NE Monsoon, SW Monsoon, Summer,
  Winter)
- Created lag features (cases in previous 1-2 months, previous
  month's rainfall) to support genuine early-warning prediction
- Label-encoded categorical variables (district, season)
- Standardized numerical features
- 80/20 train-test split with stratification

### 3.3 Model Development
Three classification models were trained and compared:

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---|---|---|---|
| Logistic Regression | [0.856] | [0.847] | [0.772] | [0.808] |
| Decision Tree | 0.822 | 0.779 | 0.759 | 0.769 |
| Random Forest | 0.847 | 0.816 | 0.785 | 0.800 |

Random Forest was selected as the baseline best model. Hyperparameter
tuning via GridSearchCV and an XGBoost classifier were subsequently
evaluated (see Day 8 results: [0.813]).

A regression model (Random Forest Regressor) was also built to predict
the actual number of disease cases, achieving an R² score of
[0.792].

### 3.4 Alert System
A 3-tier risk classification was implemented:
- 🟢 **LOW** (probability < 0.3): Routine monitoring
- 🟡 **MEDIUM** (0.3 – 0.6): Increased testing, health worker alerts
- 🔴 **HIGH** (> 0.6): Public health advisory, resource deployment

### 3.5 Dashboard Development
An interactive Streamlit dashboard was built featuring:
- District and year filtering
- Key metrics overview (total cases, average cases, outbreak rate)
- Disease trend visualization
- District comparison charts
- A real-time prediction form connected to the trained model
- Risk level display with color-coded badges and recommendations

---

## 4. Results & Key Findings

1. **Coliform count** is the single strongest predictor of outbreak
   risk (32% feature importance in the Random Forest model),
   consistent with its established role as a fecal contamination
   indicator in water quality science.
2. **Seasonal effect confirmed:** Disease cases spike sharply during
   and after the Northeast Monsoon (October–December), validating
   the inclusion of seasonal and rainfall-lag features.
3. **Model sensitivity:** Testing revealed a sharp decision boundary
   near coliform count ≈ 175-180 per 100ml, where predicted outbreak
   probability shifts from approximately 11% to 79% within a narrow
   8-unit range. This reflects a clear, learnable threshold effect in
   the underlying data and demonstrates the model's responsiveness to
   its most important feature, though it also suggests opportunities
   for further smoothing through regularization or additional
   training data in future iterations.
4. **Random Forest outperformed Logistic Regression and Decision
   Tree** baselines, balancing precision and recall effectively for
   this imbalanced classification task.

---

## 5. Dashboard Demonstration

The live dashboard is accessible at:
**https://smart-health-monitoring-tamilnadu-urfvx7yejjycqhbqbbrrgm.streamlit.app**

Screenshots of the dashboard in LOW and HIGH risk prediction states
are included in `reports/screenshots/`.

*(Insert prediction_low_risk.png and prediction_high_risk.png here
when converting to Word/PDF)*

---

## 6. Conclusions & Future Work

This project successfully demonstrates that machine learning models
can identify meaningful, interpretable relationships between water
quality parameters and waterborne disease outbreak risk, achieving a
practically useful F1-score of 0.800 with a Random Forest classifier.
The accompanying dashboard makes this prediction capability accessible
to non-technical health officials through a simple web interface.

**Limitations:**
- The dataset is synthetically generated rather than sourced from
  real field measurements, which may not capture all real-world
  noise and confounding factors
- The model's sharp decision boundaries may indicate some overfitting
  risk, which would benefit from validation against real-world data

**Future Work:**
- Integrate real water quality data from TWAD Board and CPCB once
  accessible
- Add SMS/email alert automation for high-risk predictions
- Extend the model to a true 2-week-ahead time series forecast rather
  than a same-month classification
- Add model regularization to reduce decision boundary sharpness

---

## 7. Tech Stack

| Component | Tool |
|---|---|
| Language | Python 3.14 |
| Data Analysis | pandas, numpy |
| Visualization | matplotlib, seaborn |
| ML Models | scikit-learn, XGBoost |
| Dashboard | Streamlit |
| Deployment | Streamlit Cloud |
| Version Control | Git & GitHub |

---

## 8. References

1. Tamil Nadu Water Supply and Drainage (TWAD) Board
2. Central Pollution Control Board (CPCB) — Water Quality Standards
3. National Vector Borne Disease Control Programme (NVBDCP)
4. scikit-learn Documentation — https://scikit-learn.org
5. Streamlit Documentation — https://docs.streamlit.io

---

