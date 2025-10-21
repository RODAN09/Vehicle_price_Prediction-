import streamlit as st
import pandas as pd
import joblib

# ==============================
# Page Config & Custom CSS
# ==============================
st.set_page_config(page_title="🚗 Vehicle Price Prediction", layout="wide")

st.markdown("""
<style>
body {
    background: linear-gradient(120deg, #0f2027, #203a43, #2c5364);
    color: white;
    font-family: 'Poppins', sans-serif;
}
h1, h2, h3, h4 {
    color: #FFD700;
    text-shadow: 1px 1px 2px black;
}
.stButton>button {
    background-color: #FFA500;
    color: black;
    font-weight: bold;
    border-radius: 10px;
    padding: 8px 15px;
}
.card {
    background: rgba(255, 255, 255, 0.1);
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    backdrop-filter: blur(10px);
    margin-bottom: 25px;
}
.dataframe th, .dataframe td {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# ==============================
# Load Model
# ==============================
model = joblib.load("vehicle_price_model.pkl")

# ==============================
# Title & Description
# ==============================
st.title("🚗 Vehicle Price Prediction App")
st.markdown("Fill the details below to predict the **estimated vehicle price**:")

# ==============================
# Input Form in a Card
# ==============================
st.markdown("<div class='card'>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    engine = st.selectbox("Engine", [
        "24V GDI DOHC Twin Turbo", "OHV", "16V MPFI OHV", "24V DDI OHV Turbo Diesel",
        "Automatic", "Other"
    ])
    fuel = st.selectbox("Fuel Type", ["Gasoline", "Diesel", "Electric", "Hybrid", "Other"])
    transmission = st.selectbox("Transmission", ["Automatic", "8-Speed Automatic", "6-Speed Automatic", "Manual", "Other"])
    body = st.selectbox("Body Type", ["SUV", "Sedan", "Pickup Truck", "Coupe", "Other"])

with col2:
    drivetrain = st.selectbox("Drivetrain", ["Four-wheel Drive", "All-wheel Drive", "Front-wheel Drive", "Rear-wheel Drive"])
    year = st.slider("Year of Manufacture", 1990, 2025, 2023)
    cylinders = st.selectbox("Cylinders", [3, 4, 5, 6, 8, 10, 12])
    mileage = st.number_input("Mileage (in miles)", min_value=0, max_value=300000, value=10000)
    doors = st.selectbox("Doors", [2, 3, 4, 5])

st.markdown("</div>", unsafe_allow_html=True)

# ==============================
# Prepare Input & Predict
# ==============================
age = 2025 - year

input_data = pd.DataFrame([{
    "engine": engine,
    "fuel": fuel,
    "transmission": transmission,
    "body": body,
    "drivetrain": drivetrain,
    "cylinders": cylinders,
    "mileage": mileage,
    "doors": doors,
    "age": age
}])

if st.button("🚀 Predict Price"):
    prediction = model.predict(input_data)[0]
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.metric(label="💰 Estimated Vehicle Price", value=f"${prediction:,.2f}")
    st.markdown("</div>", unsafe_allow_html=True)
