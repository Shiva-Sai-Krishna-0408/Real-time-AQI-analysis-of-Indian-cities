import streamlit as st
import folium
import pandas as pd
from streamlit_folium import st_folium

def get_color(risk_score):
    return "green" if risk_score <= 25 else "orange" if risk_score > 25 and risk_score <= 50 else "red" if risk_score > 50 and risk_score <= 75 else "darkred"

st.title("Real-time AQI Analysis of Indian Cities")
df = pd.read_csv("data/india_features_v2.csv")
st.dataframe(df)

india_map = folium.Map(location=[20.5937,78.9629],zoom_start=5)



for _,row in df.iterrows():
    folium.CircleMarker(
        location = [row["latitude"],row["longitude"]],
        radius = 10,
        color = get_color(row["risk_score"]),
        fill = True,
        fill_color = get_color(row["risk_score"]),
        fill_opacity=0.6,
        popup=f"{row['name']} | Risk Score: {row['risk_score']}",
        tool_tip="Click me"
    ).add_to(india_map)

st_folium(india_map, width=700)