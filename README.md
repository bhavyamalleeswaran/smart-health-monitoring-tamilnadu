# 🏥 Smart Community Health Monitoring & Early Warning System
### Water-Borne Diseases in Tamil Nadu

![Python](https://img.shields.io/badge/Python-3.x-blue)
![ML](https://img.shields.io/badge/ML-scikit--learn-orange)
![Dashboard](https://img.shields.io/badge/Dashboard-Streamlit-red)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)

---

## 📌 Problem Statement
Waterborne diseases like Cholera, Diarrhea, Typhoid, and Hepatitis A 
cause thousands of deaths annually in Tamil Nadu, especially after 
monsoon season. This project builds an ML-based early warning system 
to predict outbreaks 2 weeks in advance using water quality and 
rainfall data.

---

## 🎯 Objectives
- Analyze waterborne disease patterns across 12 Tamil Nadu districts
- Identify key water quality parameters that trigger outbreaks
- Build an ML model to predict outbreak risk (High / Medium / Low)
- Create an interactive dashboard for health officials

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
| Language | Python 3.x |
| Data Analysis | pandas, numpy |
| Visualization | matplotlib, seaborn |
| ML Models | scikit-learn, XGBoost |
| Dashboard | Streamlit |
| Deployment | Streamlit Cloud |

---

## 📁 Project Structure
smart-health-monitoring-tamilnadu/

├── data/         → Dataset (water quality + disease cases)

├── notebooks/    → Jupyter notebooks (EDA, ML model)

├── src/          → Alert system source code

├── models/       → Saved ML models

├── dashboard/    → Streamlit app

├── reports/      → Final report and charts

└── progress/     → Daily progress log

---

## 📊 Dataset
- **Rows:** 1008 | **Columns:** 19 | **Period:** 2018–2024
- **Districts:** 12 districts across Tamil Nadu
- **Features:**
  - Rainfall (mm)
  - Temperature (°C)
  - pH level
  - Turbidity (NTU)
  - Coliform Count (per 100ml)
  - Dissolved Oxygen (mg/L)
  - Total Dissolved Solids (mg/L)
- **Target:** Outbreak Alert (0 = No Outbreak, 1 = Outbreak)

---

## 🔬 Methodology
1. **Data Collection** → Synthetic dataset based on TN health patterns
2. **EDA** → Seasonal trends, district-wise analysis, correlations
3. **Preprocessing** → Feature engineering, scaling, train-test split
4. **ML Model** → Random Forest / XGBoost classifier
5. **Alert System** → 3-level risk: 🟢 Low / 🟡 Medium / 🔴 High
6. **Dashboard** → Streamlit interactive visualization

---

## 📈 Model Performance
*(To be updated after model training)*
| Metric | Score |
|---|---|
| Accuracy | - |
| F1-Score | - |
| R² Score | - |

---

## 🌐 Live Dashboard
**[Click here to view the live dashboard](https://smart-health-monitoring-tamilnadu-urfvx7yejjycqhbqbbrrgm.streamlit.app)**

## 🚀 How to Run Locally
```bash
# Clone the repo
git clone https://github.com/bhavyamalleeswaran/smart-health-monitoring-tamilnadu.git

# Install dependencies
pip install -r requirements.txt

# Run dashboard
streamlit run dashboard/app.py
```

---

## 📅 Progress
Check [`progress/daily_log.md`](progress/daily_log.md) for daily updates.

---

## 👤 Author
**Bhavyamalleeswaran**  
Dindigul, Tamil Nadu  
📅 Project Deadline: June 30, 2025
