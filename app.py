import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the pre-trained model
with open("RidgeModel.pkl", "rb") as file:
    model = pickle.load(file)

# Add background image and custom CSS
def add_bg_from_url():
    st.markdown(
        """
        <style>
        body {
            background-image: url("https://www.example.com/your-background-image.jpg");
            background-size: cover;
        }
        .main-container {
            background-color: rgba(255, 255, 255, 0.9); 
            padding: 20px;
            border-radius: 15px;
            max-width: 700px;
            margin: auto;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Apply the background
add_bg_from_url()

# App title
st.markdown("<h1 style='text-align: center;'>🏠 Real Estate Price Prediction App</h1>", unsafe_allow_html=True)

# Main container for inputs and results
st.markdown("<div class='main-container'>", unsafe_allow_html=True)

# Input fields
st.subheader("Enter Property Details")

area_type = st.selectbox("Area Type", ["Built-up Area", "Plot Area", "Super Built-up Area", "Carpet Area"])
availability = st.selectbox("Availability", ["Ready to Move", "Under Construction"])
location = st.text_input("Location", "Enter the location")
size = st.text_input("Size", "Enter size (e.g., 2 BHK, 3 BHK)")
society = st.text_input("Society", "Enter society name")
total_sqft = st.number_input("Total Area (sqft)", min_value=0.0, step=1.0)
bath = st.slider("Number of Bathrooms", 0, 10, 2)
balcony = st.slider("Number of Balconies", 0, 5, 1)

# Process input data for prediction
def process_input():
    # Encode area type and availability
    area_type_encoded = {"Built-up Area": 0, "Plot Area": 1, "Super Built-up Area": 2, "Carpet Area": 3}[area_type]
    availability_encoded = {"Ready to Move": 0, "Under Construction": 1}[availability]

    # Encode size (e.g., "2 BHK" -> 2)
    try:
        bhk = int(size.split(" ")[0])
    except ValueError:
        bhk = 0  # Default value if parsing fails

    # Create a DataFrame matching the model's training data
    input_df = pd.DataFrame({
        "location": [location],
        "total_sqft": [total_sqft],
        "bath": [bath],
        "bhk": [bhk],
    })
    return input_df

# Predict button
if st.button("Predict"):
    input_data = process_input()
    try:
        prediction = model.predict(input_data)
        st.subheader("🏡 Predicted Price")
        st.write(f"💰 ₹ {prediction[0]:,.2f}")
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")

# Display entered data for confirmation
st.subheader("Entered Details")
st.write({
    "Area Type": area_type,
    "Availability": availability,
    "Location": location,
    "Size": size,
    "Society": society,
    "Total Sqft": total_sqft,
    "Bath": bath,
    "Balcony": balcony,
})

# Close the styled container
st.markdown("</div>", unsafe_allow_html=True)
