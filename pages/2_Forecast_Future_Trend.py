import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
from prophet import Prophet
import matplotlib.pyplot as plt
import json
from prophet.serialize import model_to_json, model_from_json
from matplotlib.dates import YearLocator, DateFormatter

# Function to load data
def load_data():
    data = pd.read_csv('crime_data.csv')
    # data['Date'] = pd.to_datetime(data['Date'])
    data = data.rename(columns={'Date': 'ds', 'Crime Count': 'y'})
    return data

# Function to make future predictions
def make_predictions(model, periods):
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast

st.title('Forecast Future Trend 📉')
st.write('This application forecasts future crime rates using historical data.')

# st.subheader('Forecast Future Trend')
tab1, tab2 = st.tabs(["📈 Forecast Chart", "🗃 Forecast Data"])

with open('prophet_model.json', 'r') as fin:
    model = model_from_json(json.load(fin))  # Load model

# Get user input for prediction period
st.sidebar.header('User Input Parameters')
st.sidebar.subheader('Forecast Period')
periods = st.sidebar.slider('Select number of days for forecasting:', min_value=30, max_value=730, value=90)
# periods = st.slider('Select number of days for forecasting:', min_value=30, max_value=730, value=180)

# Make predictions
forecast = make_predictions(model, periods)

# Display forecast data
tab2.subheader('Forecast Data')
tab2.write(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']])

# Plot forecast
fig1 = model.plot(forecast)
tab1.pyplot(fig1)

# Plot forecast components
fig2 = model.plot_components(forecast)
tab1.pyplot(fig2)
