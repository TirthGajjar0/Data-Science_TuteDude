# Assignment 6 - Sales Forecasting Case Study

## Overview

This project focuses on forecasting future sales using time series and regression-based techniques. The workflow includes data exploration, preprocessing, feature engineering, forecasting, and model evaluation using a real-world sales dataset.

## What I Did

* Explored sales trends and seasonality
* Converted date columns and extracted time-based features
* Built forecasting models:

  * Linear Regression
  * ARIMA
  * Prophet
* Compared model performance using multiple evaluation metrics

## Results

| Model             |       MAE |       RMSE |   R² Score |
| ----------------- | --------: | ---------: | ---------: |
| Linear Regression |     85.02 |     122.96 |     -0.381 |
| ARIMA             |    144.69 |     158.42 |     -1.292 |
| Prophet           | **83.16** | **117.55** | **-0.262** |

Among the evaluated models, **Prophet** achieved the lowest MAE and RMSE, making it the best-performing forecasting model for this dataset.

## Tools & Libraries

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-Learn
* Statsmodels
* Prophet

## Key Learning Outcomes

* Time Series Analysis
* Sales Forecasting
* Feature Engineering
* ARIMA
* Prophet
* Regression Evaluation

## Educational Purpose

Completed as part of my Data Science learning journey to gain hands-on experience with forecasting techniques and model comparison using a sales dataset.

## Project Status

Completed as part of my Data Science Learning Journey.

