# Crime Rate Forecasting Using Facebook Prophet and Streamlit

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
6. [Data](#data)
7. [Problems Faced and Solved](#problems-faced-and-solved)

## Introduction
Crime Rate Forecasting is a project aimed at predicting future crime rates using historical data. The project leverages Facebook Prophet for time series forecasting and Streamlit for building an interactive web application. The motivation for using data science techniques in solving this problem is to provide law enforcement agencies and policymakers with accurate crime predictions to enhance resource allocation and public safety.

## Features
- Data Preprocessing: Handles missing values and outliers in crime data.
- Time Series Forecasting: Uses Facebook Prophet to model and predict future crime rates.
- Interactive Visualization: Provides an interactive web application built with Streamlit to visualize historical data and future forecasts.
- User Inputs: Allows users to dynamically adjust the forecasting period and visualize updated predictions.

## Installation
### Prerequisites
- Python 3.6+
- pip

### Install Required Libraries
```sh
pip install pandas prophet streamlit matplotlib
```

### Clone the Repository
```sh
git clone https://github.com/viral-prajapati/Crime-Rate-Forecasting-Using-Facebook-Prophet-and-Streamlit.git
cd Crime Rate Forecasting.py
```

## Usage
1. **Prepare the Data:**
   - Ensure your crime data is preprocessed and saved in a CSV file named `crime_data.csv` with columns `date` and `crime_rate`.

2. **Run the Streamlit Application:**
   ```sh
   streamlit run '.\Crime Rate Forecasting.py'
   ```
3. **Interact with the Application:**
   - Open your browser and navigate to the provided local URL (typically `http://localhost:8501`).
   - Use the sidebar to adjust the number of days for forecasting and view updated predictions and visualizations.

## Project Structure
```
crime-rate-forecasting/
│
├── Crime Rate Forecasting.py    # Main Streamlit application
├── crime_data.csv               # Sample crime data (ensure your actual data is properly formatted)
├── README.md                    # Project documentation
└── data_preprocessing.ipynb     # Jupyter notebook for data preprocessing (if needed)
```

## Data
### Source
- Public crime data repositories (e.g., Kaggle, government databases).
- Dataset: https://www.kaggle.com/currie32/crimes-in-chicago

### Format
- CSV files containing records of crime incidents with attributes such as date, type of crime, location, and severity.

### Statistics
- Descriptive statistics are performed to understand the distribution and trends within the data.

## Problems Faced and Solved
1. **Data Quality Issues:** Cleaned and preprocessed the data to handle missing values and outliers, ensuring quality and consistency.
2. **Model Performance:** Fine-tuned the Facebook Prophet model parameters to optimize forecasting accuracy.
3. **User Accessibility:** Developed an interactive Streamlit application to make the forecasting tool user-friendly and accessible.
4. **Model Validation:** Split the data into training and testing sets to validate the model and ensure reliable predictions.
5. **Scalability:** Implemented a scalable data storage solution using PostgreSQL or cloud storage to handle large datasets efficiently.

- Github Link: https://github.com/viral-prajapati/Crime-Rate-Forecasting-Using-Facebook-Prophet-and-Streamlit

This README file provides a comprehensive overview of your project, including setup instructions, usage guidelines, and details on the project's structure and features.