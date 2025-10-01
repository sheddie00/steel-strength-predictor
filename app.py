import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("steel_strength_xgb_model.pkl")

# Streamlit page setup
st.set_page_config(page_title="Steel Strength Predictor", page_icon="⚙️", layout="centered")
st.title("⚙️ Steel Strength Prediction App")
st.write("Enter the steel composition to predict **Ultimate Tensile Strength (UTS, MPa).**")

# Try to get expected features
try:
    expected_features = model.feature_names_in_
except AttributeError:
    # fallback: manually list the features you used in training
    expected_features = ["C (Min)", "Mn (Min)", "Si (Min)", "Ni (Min)", 
                         "Cr (Min)", "Mo (Min)", "Ti (Min)"]

# Debug info (you can remove this later)
st.sidebar.header("🔎 Debug Info")
st.sidebar.write("Expected by model:", model.get_booster().feature_names)
st.sidebar.write("Using features:", expected_features)

# Input form
user_inputs = {}
for feature in expected_features:
    user_inputs[feature] = st.number_input(f"{feature}", value=0.0)

# Convert user input into DataFrame
input_data = pd.DataFrame([user_inputs])

# Reorder columns to match training order
input_data = input_data[expected_features]

# Prediction button
if st.button("🔮 Predict UTS"):
    try:
        # Try with named features
        prediction = model.predict(input_data)[0]
    except ValueError:
        # If mismatch occurs, fallback to numpy (ignores column names, uses only order)
        prediction = model.predict(input_data.to_numpy())[0]

    st.success(f"### 🏋️ Predicted UTS: **{prediction:.2f} MPa**")
