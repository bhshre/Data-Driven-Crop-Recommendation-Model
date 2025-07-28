import streamlit as st
import numpy as np
import joblib
import pandas as pd

# ---- load artifacts ----
model = joblib.load("crop_model.pkl")
scaler = joblib.load("scaler.pkl")
le = joblib.load("label_encoder.pkl")
feature_order = joblib.load("feature_order.pkl")   # ['N','P','K','temperature','humidity','ph','rainfall']

st.title("🌾 Crop Recommendation System")
st.markdown("Enter soil nutrients & weather conditions to get the best crop recommendation.")

# ---- inputs ----
N = st.number_input("Nitrogen (N)", min_value=0.0, max_value=200.0, value=50.0, step=1.0)
P = st.number_input("Phosphorus (P)", min_value=0.0, max_value=200.0, value=40.0, step=1.0)
K = st.number_input("Potassium (K)", min_value=0.0, max_value=200.0, value=40.0, step=1.0)
temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=60.0, value=25.0, step=0.1)
humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=70.0, step=0.1)
ph = st.number_input("Soil pH", min_value=0.0, max_value=14.0, value=6.5, step=0.1)
rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=400.0, value=200.0, step=1.0)

if st.button("Recommend Crop"):
    # Arrange data in the same order as training
    sample = pd.DataFrame([[N, P, K, temperature, humidity, ph, rainfall]], columns=feature_order)

    # Scale the data
    sample_scaled = scaler.transform(sample)

    # Predict crop
    pred_idx = model.predict(sample_scaled)[0]
    pred_label = le.inverse_transform([pred_idx])[0]

    # Show result
    st.success(f"🌱 Recommended Crop: **{pred_label}**")
