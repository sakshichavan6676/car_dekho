import streamlit as st
import pickle

# Load model
with open("car_price_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Car Selling Price Prediction")

# -------- NUMERIC INPUTS --------
km_driven = st.number_input("Kilometers Driven", min_value=0)
seats = st.number_input("Number of Seats", min_value=1, max_value=10)
years_old = st.number_input("Car Age (Years)", min_value=0)
mileage_value = st.number_input("Mileage (km/l)")
engine_value = st.number_input("Engine (CC)")
max_power_value = st.number_input("Max Power (bhp)")

# -------- OWNER (ORDINAL) --------
owner = st.selectbox(
    "Owner",
    ["First Owner", "Second Owner", "Third Owner", "Fourth & Above Owner"]
)

owner_map = {
    "First Owner": 0,
    "Second Owner": 1,
    "Third Owner": 2,
    "Fourth & Above Owner": 3
}
owner_encoded = owner_map[owner]

# -------- FUEL TYPE (ONE-HOT) --------
fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "LPG", "CNG"])

fuel_Petrol = 1 if fuel == "Petrol" else 0
fuel_Diesel = 1 if fuel == "Diesel" else 0
fuel_LPG = 1 if fuel == "LPG" else 0
fuel_CNG = 1 if fuel == "CNG" else 0

# -------- SELLER TYPE (ONE-HOT) --------
seller_type = st.selectbox(
    "Seller Type",
    ["Individual", "Trustmark Dealer"]
)

seller_type_Individual = 1 if seller_type == "Individual" else 0
seller_type_Trustmark_Dealer = 1 if seller_type == "Trustmark Dealer" else 0

# -------- TRANSMISSION (ONE-HOT) --------
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
transmission_Manual = 1 if transmission == "Manual" else 0

# -------- PREDICTION --------
if st.button("Predict Selling Price"):
    input_data = [[
        km_driven,
        owner_encoded,
        seats,
        years_old,
        mileage_value,
        engine_value,
        max_power_value,
        fuel_Diesel,
        fuel_LPG,
        fuel_Petrol,
        fuel_CNG,
        seller_type_Individual,
        seller_type_Trustmark_Dealer,
        transmission_Manual
    ]]

    prediction = model.predict(input_data)
    st.success(f"Predicted Selling Price: ₹ {prediction[0]:,.2f}")
