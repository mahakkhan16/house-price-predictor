import streamlit as st
import pandas as pd
import joblib

# Load the trained model and column structure
model = joblib.load('house_price_model.pkl')
model_columns = joblib.load('model_columns.pkl')

st.title("House Price Predictor")
st.write("Enter house details below to get a predicted sale price.")

lot_area = st.number_input("Lot Area (sq ft)", min_value=500, max_value=50000, value=8000)
overall_qual = st.slider("Overall Quality (1-10)", 1, 10, 5)
year_built = st.number_input("Year Built", min_value=1900, max_value=2025, value=2000)
gr_liv_area = st.number_input("Above Ground Living Area (sq ft)", min_value=300, max_value=6000, value=1500)
total_bsmt_sf = st.number_input("Total Basement Area (sq ft)", min_value=0, max_value=6000, value=800)
garage_cars = st.slider("Garage Capacity (cars)", 0, 5, 2)

if st.button("Predict Price"):
    input_data = pd.DataFrame([[0] * len(model_columns)], columns=model_columns)

    input_data['LotArea'] = lot_area
    input_data['OverallQual'] = overall_qual
    input_data['YearBuilt'] = year_built
    input_data['GrLivArea'] = gr_liv_area
    input_data['TotalBsmtSF'] = total_bsmt_sf
    input_data['GarageCars'] = garage_cars

    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Sale Price: ${prediction:,.2f}")
