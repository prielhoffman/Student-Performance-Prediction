# Student Performance Prediction
This repository contains a project aimed at predicting student performance using machine learning models. The dataset used in this project, the "Student Performance Dataset," includes various features related to students' grades, demographics, social factors, and school-related aspects. These data points were collected through school reports and questionnaires. The primary goal is to build models that predict a student's final grade and classify whether their performance will be above average.

# Overview
The project involves two main tasks:
1) Linear Regression Model: Predicts the student's final grade at the end of the year.
2) Classification Model: Classifies whether a student's final performance will be above average based on the dataset features.

# Dataset
The "Student Performance Kit" can be downloaded from the student-mat.csv file associated with this Repository.

# Files in the Repository
1) main.ipynb: A Jupyter Notebook containing the step-by-step implementation of the linear regression and classification models.
2) ML_DL_Functions1.py: A Python file where utility functions are implemented.
3) student_performance.csv: The dataset file containing student data.

# Project Structure
* Data Exploration: Initial exploration of the dataset to understand the features, check for missing values, and perform any necessary preprocessing steps.
* Linear Regression Model: Building a linear regression model to predict the target variable G3, which represents the student's final grade.
* Feature Engineering: Transforming and selecting features to improve the model's performance.
* Classification Model: Building a classifier to determine if a student's performance at the end of the year is above average. The classifier uses the preprocessed features and can utilize various algorithms like Logistic Regression, Decision Trees, or Random Forests.
* Model Evaluation: Evaluating both models using appropriate metrics such as Mean Squared Error (MSE) for regression and Accuracy, Precision, Recall, or F1-Score for classification.

# Note
Ensure the dataset file (student-mat.csv) is located in the same directory as the Jupyter Notebook for the notebook to load it properly.

# Acknowledgments
The "Student Performance Dataset" is sourced from the UCI Machine Learning Repository.
