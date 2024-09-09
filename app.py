import streamlit as st
import pickle
import numpy as np

# Load the model
model = pickle.load(open('GB.pkl', 'rb'))

# Load custom CSS
# def load_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# load_css("styles.css")

# Title of the application
st.title("Solar Power Generation Prediction")

# Input fields
distance_to_solar_noon = st.number_input("Distance to Solar Noon")
temperature = st.number_input("Temperature")
wind_direction = st.number_input("Wind Direction")
wind_speed = st.number_input("Wind Speed")
sky_cover = st.number_input("Sky Cover")
visibility = st.number_input("Visibility")
humidity = st.number_input("Humidity")
average_wind_speed_period = st.number_input("Average Wind Speed (Period)")
average_pressure_period = st.number_input("Average Pressure (Period)")

# Predict Button
if st.button("Predict"):
    # Prepare the input data
    input_data = np.array([[distance_to_solar_noon, temperature, wind_direction, wind_speed, sky_cover, visibility, humidity, average_wind_speed_period, average_pressure_period]])
    
    # Predict the output
    prediction = model.predict(input_data)[0]
    prediction = max(prediction,0)
    
    # Display the prediction
    st.success(f"Predicted Power Generation: {prediction} MW")
