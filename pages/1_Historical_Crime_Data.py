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



st.title('Historical Crime Data 📜')
st.write('This page shows the Crime that happened in Chicago through Charts and Data.')

# Load data
data = load_data()
# st.subheader('Historical Crime Data')
tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])

tab1.image('data_img.png', caption='Historical Data')
tab2.write(data)
