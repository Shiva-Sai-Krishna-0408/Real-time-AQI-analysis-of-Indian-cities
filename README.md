# Real-time AQI Analysis of Indian Cities

A machine learning system that scores and visualizes air quality risk 
across Indian cities using real-time pollution data.

## Project Overview

This project pulls real-time air quality data from the 
OpenAQ API, processes and engineers features using NumPy and Pandas, 
builds a risk scoring model using Random Forest Regression, and 
visualizes results on an interactive Indian map using Folium and 
Streamlit.

The system currently monitors 13 Indian cities, classifying each 
station by PM2.5 and PM10 pollution levels using WHO air quality 
guidelines as thresholds.

## Live Demo
https://real-time-aqi-india.streamlit.app/

## Tech Stack
- **Data Collection**: Python, Requests, OpenAQ API
- **Data Processing**: Pandas, NumPy
- **Machine Learning**: Scikit-learn (Random Forest Regressor)
- **Visualization**: Folium, Streamlit
- **Environment**: Jupyter Notebook, VS Code

## Project Structure
```
Real-time AQI Analysis/
├── data/
│   ├── india_aqi_locations.csv
│   ├── india_aqi_final.csv
│   ├── india_features.csv
│   └── india_features_v2.csv
├── notebooks/
│   ├── 01_data_collection.ipynb
│   └── 02_visualization.ipynb
├── outputs/
│   └── india_risk_map.html
├── app.py
├── requirements.txt
└── README.md
```

## How It Works
1. Real-time PM2.5 and PM10 data is pulled from OpenAQ API 
   across 25 Indian monitoring stations
2. Data is cleaned — outliers removed, missing values dropped, 
   duplicate sensors averaged
3. Features engineered: Min-Max normalized pollution scores, 
   WHO-aligned risk categories (Good → Hazardous), geographic 
   region classification (North/South/East/West)
4. Combined risk score calculated as weighted average of 
   normalized PM2.5 and PM10 scores (0-100 scale)
5. Random Forest Regressor trained to predict risk scores 
   from location and pollution features
6. Results visualized on interactive Folium map, deployed 
   publicly via Streamlit

## Results
- **Dataset**: 13 Indian cities with complete PM2.5 and PM10 data
- **Model MAE**: 4.79 (on held-out test set)
- **Key Finding**: North Indian cities average PM2.5 of 120+ µg/m³ — 
  nearly 4x the WHO safe limit of 15 µg/m³. Southern cities like 
  Bengaluru average below 55 µg/m³
- **Risk Distribution**: 7 of 13 stations classified Unhealthy 
  or above for PM2.5

## Limitations & Future Work
- Dataset limited to 13 cities due to API data availability 
  constraints at time of collection
- Risk score currently based on PM2.5 and PM10 only
- Future versions will incorporate NO2, SO2, temperature, 
  and humidity data
- Plan to expand to global dataset for broader cross-country analysis
- Prediction model will be retrained with larger dataset for 
  statistically meaningful results
- The target variable is driven from mean of normalized scores of parameters which were used to train the model, making its    learning circular

## How to Run
1. Clone the repository
```
git clone https://github.com/Shiva-Sai-Krishna-0408/Real-time-AQI-analysis-of-Indian-cities.git
```
2. Create and activate virtual environment
```
python -m venv .venv
.venv\Scripts\Activate.ps1
```
3. Install dependencies
```
pip install -r requirements.txt
```
4. Run the Streamlit app
```
streamlit run app.py
```

## About
Built as part of an AI/ML learning journey focused on using 
data science for environmental impact. All data sourced from 
OpenAQ's public API.
