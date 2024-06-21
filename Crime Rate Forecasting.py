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

# Function to train the Prophet model
# def train_model(data):
#     model = Prophet()
#     model.fit(data)
#     return model

# Function to make future predictions
def make_predictions(model, periods):
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast

# Main Streamlit app
def main():
    st.title('Crime Rate Forecasting using Facebook Prophet ⚖️')
    st.write('This application forecasts future crime rates using historical data. 👮🚨')

    # Load data
    data = load_data()
    # st.subheader('Historical Crime Data')
    # tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
    # tab2.write(data)


    # dates = []
    # for y in range(2005, 2013):
    #     dates += [str(y)+"-"+str(m) for m in range(1, 13)]
    #     x = np.arange(len(dates))

    # Plot historical data
    st.image('crime_img.png', caption='Crime Picture')
    # fig, ax = plt.subplots()
    # ax.plot(data['ds'], data['y'], label='Crime Rate')
    # ax.set_xlabel('Date')
    # ax.set_ylabel('Crime Rate')
    # ax.legend()
    # st.pyplot(fig)

    # def _plot_series(series, series_name, series_index=0):
    #     palette = list(sns.palettes.mpl_palette('Dark2'))
    #     xs = series['ds']
    #     ys = series['y']
  
    #     plt.plot(xs, ys, label=series_name, color=palette[series_index % len(palette)])

    # fig, ax = plt.subplots(figsize=(10, 5.2), layout='constrained')
    # df_sorted = data.sort_values('ds', ascending=True)
    # _plot_series(df_sorted, '')
    # sns.despine(fig=fig, ax=ax)
    # plt.xlabel('ds')
    # _ = plt.ylabel('y')

    # Train model
    # model = train_model(data)

    # with open('prophet_model.json', 'r') as fin:
    #     model = model_from_json(json.load(fin))  # Load model
    
    # Get user input for prediction period
    # periods = st.slider('Select number of days for forecasting:', min_value=30, max_value=730, value=180)
    
    # Make predictions
    # forecast = make_predictions(model, periods)
    
    # Display forecast data
    # st.subheader('Forecast Data')
    # st.write(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']])
    
    # Plot forecast
    # fig1 = model.plot(forecast)
    # st.pyplot(fig1)
    
    # Plot forecast components
    # fig2 = model.plot_components(forecast)
    # st.pyplot(fig2)

if __name__ == "__main__":
    main()
