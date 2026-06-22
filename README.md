# 🏥 Smart Community Health Monitoring & Early Warning System
### Water-Borne Diseases in Tamil Nadu

![Python](https://img.shields.io/badge/Python-3.14-blue)
![ML](https://img.shields.io/badge/ML-scikit--learn-orange)
![Dashboard](https://img.shields.io/badge/Dashboard-Streamlit-red)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

---

## 🌐 Live Dashboard
**[🔗 Click here to view the live dashboard](https://smart-health-monitoring-tamilnadu-urfvx7yejjycqhbqbbrrgm.streamlit.app)**

> ⚠️ Note: If the app shows "Zzzz... gone to sleep," just click 
> **"Yes, get this app back up!"** — it takes about 30-60 seconds 
> to wake up since it's hosted on Streamlit's free tier.

---

## 📌 Problem Statement
Waterborne diseases like Cholera, Diarrhea, Typhoid, and Hepatitis A
cause thousands of cases annually in Tamil Nadu, especially after
monsoon season. This project builds an ML-based early warning system
to predict outbreak risk using water quality and rainfall data,
enabling proactive rather than reactive public health response.

---

## 🎯 Objectives
- Analyze waterborne disease patterns across 12 Tamil Nadu districts
- Identify key water quality parameters that trigger outbreaks
- Build an ML model to predict outbreak risk (Low / Medium / High)
- Create an interactive dashboard for health officials

---

## 📸 Screenshots

### Dashboard Overview
![Dashboard Overview](reports/screenshots/dashboard_v1.png)

### Risk Prediction — Low Risk
![Low Risk](reports/screenshots/prediction_low_risk.png)

### Risk Prediction — High Risk
![High Risk](reports/screenshots/prediction_high_risk.png)

---

## 🗺️ Scope
- **State:** Tamil Nadu
- **Districts:** Chennai, Tiruppur, Madurai, Thanjavur, Tirunelveli,
  Coimbatore, Salem, Tiruchirappalli, Vellore, Cuddalore,
  Nagapattinam, Ramanathapuram
- **Period:** 2018–2024
- **Diseases:** Cholera, Diarrhea, Typhoid, Hepatitis A

---

## 🛠️ Tech Stack
| Component | Tool |
|---|---|
| Language | Python 3.14 |
| Data Analysis | pandas, numpy |
| Visualization | matplotlib, seaborn |
| ML Models | scikit-learn, XGBoost |
| Dashboard | Streamlit |
| Deployment | Streamlit Cloud |

---

## 📁 Project Structure

smart-health-monitoring-tamilnadu/

├── data/         → Dataset (water quality + disease cases)

├── notebooks/    → 8 Jupyter notebooks (EDA → ML → Alert System)

├── src/          → Alert system source code

├── models/       → Saved ML models (.pkl)

├── dashboard/    → Streamlit app

├── reports/      → Final report, charts, screenshots

└── progress/     → Daily progress log (17 days)

---

## 📊 Dataset
- **Rows:** 1,008 | **Columns:** 25 | **Period:** 2018–2024
- **Districts:** 12 districts across Tamil Nadu
- **Features:** Rainfall, Temperature, pH, Turbidity, Coliform Count,
  Dissolved Oxygen, Total Dissolved Solids
- **Target:** Outbreak Alert (39% positive class — realistic balance)

---

## 🔬 Methodology
1. **Data Collection** → Realistic synthetic dataset modeling TN
   water quality and disease patterns
2. **EDA** → Seasonal trends, district analysis, correlations
3. **Preprocessing** → Feature engineering, lag features, scaling
4. **ML Models** → Logistic Regression, Decision Tree, Random Forest,
   XGBoost (classification) + Random Forest Regressor (case count
   prediction)
5. **Alert System** → 3-level risk: 🟢 Low / 🟡 Medium / 🔴 High
6. **Dashboard** → Streamlit interactive visualization + live
   prediction

---

## 📈 Model Performance

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---|---|---|---|
| Logistic Regression | [0.856] | [0.847] | [0.772] | [0.808] |
| Decision Tree | 0.822 | 0.779 | 0.759 | 0.769 |
| **Random Forest (Best)** | **0.847** | **0.816** | **0.785** | **0.800** |

**Most Important Feature:** Coliform Count (32% importance)

---

## 🚀 How to Run Locally
```bash
# Clone the repo
git clone https://github.com/bhavyamalleeswaran/smart-health-monitoring-tamilnadu.git

# Navigate to project
cd smart-health-monitoring-tamilnadu

# Install dependencies
pip install -r requirements.txt

# Run dashboard
python -m streamlit run dashboard/app.py
```

---

## 🎥 Demo Video
**[Watch the project demo](https://drive.google.com/file/d/1SOk5V2DSus3yTIEm4amP8dyELBwmUtBe/view?usp=sharing)**

---

## 📅 Progress
This project was built over 17 days with daily commits. Check
[`progress/daily_log.md`](progress/daily_log.md) for the complete
day-by-day journey, including challenges faced (like discovering and
fixing a data imbalance bug on Day 7!) and how they were solved.

---

## 📄 Full Report
See [`reports/final_report.md`](reports/final_report.md) for the
complete project report including methodology, results, and findings.

---

## 👤 Author
**Bhavyamalleeswaran**
Dindigul, Tamil Nadu
📅 Project Duration: June 13 – June 30, 2026