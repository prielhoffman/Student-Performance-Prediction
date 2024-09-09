# Student Performance Prediction

This repository contains a project aimed at predicting student performance using machine learning models. The dataset used in this project, the "Student Performance Dataset," includes various features related to students' grades, demographics, social factors, and school-related aspects. These data points were collected through school reports and questionnaires. The primary goal is to build models that predict a student's final grade and classify whether their performance will be above average.

## Overview

The project involves two main tasks:

1. **Linear Regression Model**: Predicts the student's final grade at the end of the year.
2. **Classification Model**: Classifies whether a student's final performance will be above average based on the dataset features.

## Dataset

The dataset used in this project is the "Student Performance Dataset," which can be downloaded from the file `student-mat.csv` included in this repository.

## Files in the Repository

- **main.ipynb**: A Jupyter Notebook containing the step-by-step implementation of the linear regression and classification models.
- **ML_DL_Functions1.py**: A Python file with utility functions for data preprocessing, model building, and evaluation.
- **student_performance.csv**: The dataset file containing student data.

## Project Structure

1. **Data Exploration**:
    - Explore the dataset to understand the features.
    - Check for missing values and perform any necessary preprocessing steps.

2. **Linear Regression Model**:
    - Build a linear regression model to predict the target variable `G3`, which represents the student's final grade.

3. **Feature Engineering**:
    - Transform and select features to improve model performance.

4. **Classification Model**:
    - Build a classifier to determine if a student's performance at the end of the year is above average.
    - Use various algorithms such as Logistic Regression, Decision Trees, or Random Forests.

5. **Model Evaluation**:
    - Evaluate both models using appropriate metrics:
        - **Regression**: Mean Squared Error (MSE)
        - **Classification**: Accuracy, Precision, Recall, or F1-Score

## Note

Ensure the dataset file (`student-mat.csv`) is located in the same directory as the Jupyter Notebook to load it properly.

## Acknowledgments

The "Student Performance Dataset" is sourced from the UCI Machine Learning Repository.
