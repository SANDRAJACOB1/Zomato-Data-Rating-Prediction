import streamlit as st
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Load the model
model3 = pickle.load(open('zomato.pkl', 'rb'))

# Set up the app with custom CSS
st.set_page_config(page_title='Zomato Rating Predictor', layout='wide')

# Custom CSS
st.markdown(
    """
    <style>
    .reportview-container {
        background: #f0f2f6;
    }
    .sidebar .sidebar-content {
        background: #fff;
        padding: 20px;
        border-radius: 10px;
    }
    .css-1aumxhk {
        display: none;
    }
    .css-10trblm {
        font-size: 1.5rem;
        color: #ff4b4b;
    }
    .stButton>button {
        color: white;
        background-color: #ff4b4b;
        border: none;
        border-radius: 10px;
        padding: 10px 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Image
st.title('Zomato Restaurant Rating Prediction')
image = Image.open("/content/zomato.jpg")
st.image(image, use_column_width=True)

# Function to get user input
def user_report():
    CountryCode = st.sidebar.slider('Country Code', 1, 200, 1)
    Has_Table_Booking = st.sidebar.selectbox('Has Table Booking', ['Yes', 'No'])
    Has_Online_delivery = st.sidebar.selectbox('Has Online Delivery', ['Yes', 'No'])
    Price_range = st.sidebar.slider('Price Range', 1, 4, 2)
    Votes = st.sidebar.slider('Votes', 0, 10000, 100)
    Average_Cost_for_two = st.sidebar.slider('Average Cost for Two', 100, 10000, 500)
    
    Has_Table_Booking = 1 if Has_Table_Booking == 'Yes' else 0
    Has_Online_delivery = 1 if Has_Online_delivery == 'Yes' else 0

    user_report_data = {
        'CountryCode': CountryCode,
        'Has_Table_booking': Has_Table_Booking,
        'Has_Online_delivery': Has_Online_delivery,
        'Price_range': Price_range,
        'Votes': Votes,
        'Average_Cost_for_two': Average_Cost_for_two,
    }
    report_data = pd.DataFrame(user_report_data, index=[0])
    return report_data

user_data = user_report()
st.header('Restaurant Data')
st.write(user_data)

# Prediction
if st.button('Predict Rating'):
    rating = model3.predict(user_data)
    st.subheader('Predicted Rating')
    st.subheader(np.round(rating[0], 2))

else:
    st.subheader('Click the button to predict the rating!')

# Additional Information
st.sidebar.markdown("""
    ### How to use this app:
    - Use the sliders and dropdowns to input restaurant details.
    - Click on the 'Predict Rating' button to get the predicted rating.
    - See the visualization of the input feature values.
""")