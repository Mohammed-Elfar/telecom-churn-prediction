# Telecom Churn Prediction

The goal is to predict whether a telecom customer will churn (stop using the service) based on features like usage patterns, account details, and customer service interactions. 

**link of the app** : https://telecom-churn-prediction-dyetrdabpc2obkzvpluqiu.streamlit.app/

## Approach & Steps:

1- Understanding the data variables: This step is important because it allows you to understand the meaning of each variable and how it might be related to the dependent variable

2- checked if the data types were correct and didn’t need changes, then looked for missing or repeated data.

3- Univariate analysis:  In this step i will go through each column and fix problems , look at the distribution of each variable and do Eda for features to understand

4- Creating new features: This step allows you to create new features that are based on the existing features. This can be helpful if you want to improve the accuracy of your model.

5- Identifying the most important variables using diff tests: This step allows you to identify the variables that have the biggest impact on the dependent variable 

6- Pipeline Building: A pipeline was created to handle preprocessing, feature engineering, and model integration, ensuring a smooth and consistent workflow for training.

7- Model Building: The model building process utilized a pipeline and cross-validation to train and test multiple models and choose best model, ensuring no data leakage and  effective model. A pipeline was established to preprocess data and integrate various models, maintaining a consistent workflow.

8- Tuning: Tune The model using 5- cross-validation and grid search to optimize hyperparameters.
