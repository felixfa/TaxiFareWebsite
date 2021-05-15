import streamlit as st
import streamlit.components.v1 as components
import datetime
import requests
import time
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")
'''# New York Taxi Fare'''


col1, col2, col3= st.beta_columns((1, 1, 2))

with col1:
    '''### Date'''
    date = st.date_input("",datetime.date(2015, 7, 6))
    '''### Pickup'''
    pickup_longitude = st.number_input('Insert a pickup longitude', format='%f', value=40.7614327)
    pickup_latitude = st.number_input('Insert a pickup latitude', format='%f',value=-73.9798156)
    '''### Passengers'''
    passenger_count = st.slider('How many passengers?', 1, 6, 2)


with col2:
    '''### Time'''
    input_time = st.time_input('', datetime.time(17, 15))
    '''### Dropoff'''
    dropoff_longitude = st.number_input('Insert a dropoff longitude', format='%f', value=40.6431166)
    dropoff_latitude = st.number_input('Insert a dropoff latitude', format='%f', value=-73.787408)


with col3:

    @st.cache
    def get_map_data():
        print('get_map_data called')
        return pd.DataFrame({
                'lon':[pickup_latitude, dropoff_latitude],
                'lat':[pickup_longitude, dropoff_longitude]

            })

    df = get_map_data()
    st.map(df)


date_time=str(date) + ' ' + str(input_time) + ' ' + 'UTC'

df = {
        'key':[date_time],
        'pickup_datetime': [date_time],
        'pickup_longitude': [pickup_longitude],
        'pickup_latitude': [pickup_latitude],
        'dropoff_longitude': [dropoff_longitude],
        'dropoff_latitude': [dropoff_latitude],
        'passenger_count': [passenger_count]
        }

#Make Prediction, when you click the button


c1,c2,c3,c4,c5 = st.beta_columns(5)

with c3:
    if st.button('------------ Predict the price! ------------'):
        # print is visible in server output, not in the page
        BASE_URI = 'https://taxifaremodel-m2ianlcoya-ew.a.run.app/predict_fare'
        r = requests.get(BASE_URI, params=df).json()
        result = r['prediction']


        st.write(f"The predicted price is **{result}** US Dollar.")


