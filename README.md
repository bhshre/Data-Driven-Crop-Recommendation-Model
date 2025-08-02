# 🌾 Data-Driven Crop Recommendation Model

##  Objective

This project presents a **machine learning-based crop recommendation system** that predicts the most suitable crop based on soil nutrients and weather conditions. The model is deployed using **Streamlit** for easy local use.

---

##  Problem Statement

Farmers often face difficulty choosing the right crop based on soil and climate. This project helps solve that problem using a trained ML model that takes input parameters like nitrogen, phosphorus, potassium, temperature, humidity, pH, and rainfall to suggest the best crop.

---

## Features

- Trained Random Forest machine learning model
- Input interface for farmers via Streamlit
- Instant crop recommendation
-  Local deployment using Python
-  Lightweight and beginner-friendly

---

## Project Structure
cropapp/
│
├── app.py # Streamlit application

├── requirements.txt # Python dependencies

├── crop_model.pkl # Trained ML model

├── scaler.pkl # Scaler used during training

├── label_encoder.pkl # Label encoder for crops

├── feature_order.pkl # List of feature column order

├── streamlit_app.png # Screenshot of app interface

---
## Files Included
app.py: Streamlit application

crop_model.pkl: Trained model

scaler.pkl, label_encoder.pkl: Encoders used during preprocessing

requirements.txt: Python packages

---

## How It Works

1. User enters soil and environmental details.
2. Model processes inputs and returns a crop recommendation.
3. Built using a trained model, deployed with Streamlit for easy use.

---

##  Screenshot

![App Screenshot](https://github.com/bhshre/Data-Driven-Crop-Recommendation-Model/blob/main/streamlit_app.png)

---

## Python Notebook 
[Notebook](https://github.com/bhshre/Data-Driven-Crop-Recommendation-Model/blob/main/Crop_Recommendation_System_.ipynb)

---

##  Technologies Used

- Python
- Streamlit
- Pandas, NumPy
- Scikit-learn
- Joblib

---

##  Installation & Run Locally

1. **Install dependencies**
pip install -r requirements.txt
2. **Run the app**
streamlit run app.py

---

## **Conclusion**
The Data-Driven Crop Recommendation Model empowers farmers with intelligent crop choices. This project showcases the power of machine learning and Streamlit for real-world agricultural applications.

## **Author**
This project was created by Shreya Bhattacharjee, MSC in data science, an aspiring Data Scientist and Data Engineer passionate about solving real-world problems through data.

Let's connect on [LinkedIn](https://www.linkedin.com/in/shreya-bhattacharjee-47b01129a/) or check out more projects on [GitHub](https://github.com/bhshre)




