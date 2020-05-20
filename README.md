# Salary Prediction Project(Python)

The purpose of this project is to use data transformation and machine learning to create a model that will predict house prices when given location (latitude and longitude), year built, lotsize(in square feet), bedroomcount etc.

## Methodology

I took an object oriented approach to solve this problem. I created three different classes, 'data_prep' , 'data_intersection' and 'modelling'. I import these classes in my notebooks for the following purposes:

- Data Wrangling - `Removed duplicates and dropped missing or null values in the dataset.`
- Exploratory Data Analysis - `Analyzed the data and summarized the main characteristics.`
- Machine Learning Algorithms Used - `Linear Regression, Random Forest and Xgboost`
- Evaluation Metrics Used - `Mean Squared Error(MSE) and R-squared`

## Technologies/Libraries Used
  ```
 - Python 3
 - Jupyter
 - Pandas
 - Numpy
 - Seaborn
 - Matplotlib
 - Scikit-Learn
 ```
## Datasets available

There are four datasets available. The train data and the properties of 2016 dataset were joined to create the train dataframe. All the entries of the dataframe are residuals. Besides, the test data and properties of 2017 dataset were joined to create the test dataframe. The data consists of a lot of null values.

## Information Used to Predict Salaries

-  **taxamount:** The column here contains the tax amount to be paid while buying the house
-  **Latitude:** The latitude coordinate of the house
-  **Longitude:** The longitude coordinate of the house
-  **lotsizesquarefeet:** Area in square feet
-  **Yearbuilt:** The year when the house was built

## Summary

*Applying random forest regressor to the features led to the most accurate predictions with the least error . The result was a **mean squared error of 0.0267**.This model can be used as a guide when determining real estate prices since it leads to reasonable predictions when given information on location (latitude and longitude), year built, lotsize(in square feet), bedroomcount etc.
*
