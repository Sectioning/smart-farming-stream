import streamlit as st
import joblib

model = joblib.load("virtual_irrigation_model.pkl")

st.title("🌾 Smart Farming: Virtual Irrigation Controller")

temp = st.slider("Temperature (°C)", 15, 45, 30)
humidity = st.slider("Humidity (%)", 20, 100, 50)
soil = st.slider("Soil Moisture (%)", 0, 100, 30)
rain = st.slider("Rainfall (mm)", 0, 20, 1)

if st.button("Predict"):
    result = model.predict([[temp, humidity, soil, rain]])[0]
    if result == 1:
        st.success("💧 Irrigation Needed — Turning Pump ON")
    else:
        st.info("✅ No Irrigation Needed")
