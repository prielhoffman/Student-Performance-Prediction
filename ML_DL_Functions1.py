import numpy as np
def ID1():
    '''
        Write your personal ID here.
    '''
    # Insert your ID here
    return 318277308
def ID2():
    '''
        Only If you were allowed to work in a pair will you fill this section and place the personal id of your partner otherwise leave it zeros.
    '''
    # Insert your ID here
    return 000000000

def LeastSquares(X,y):
  '''
    Calculates the Least squares solution to the problem
    X*theta=y using the least squares method
    :param X: input matrix
    :param y: input vector
    :return: theta = (Xt*X)^(-1) * Xt * y 
  '''
  X_T = np.transpose(X)
  XTX_inv = np.linalg.inv(np.dot(X_T, X))
  theta = np.dot(np.dot(XTX_inv, X_T), y)
  return theta

def classification_accuracy(model,X,s):
  '''
    calculate the accuracy for the classification problem
    :param model: the classification model class
    :param X: input matrix
    :param s: input ground truth label
    :return: accuracy of the model
  '''
  predictions = model.predict(X)
  correct_predictions = (predictions == s).sum()
  total_predictions = len(s)
  accuracy = (correct_predictions / total_predictions) * 100.0
  return accuracy

def linear_regression_coeff_submission():
  '''
    copy the values from your notebook into a list in here. make sure the values
    seperated by commas
    :return: list of coefficiants for the linear regression problem.  
  '''
  return [-6.33915144e-02,  3.70157249e-02, -6.01100244e-02,  1.16481061e-02,
 -4.37419745e-02, -2.02136601e-02,  8.39248620e-02,  5.80003243e-03,
 -9.35075926e-03, -3.22170733e-02,  5.02801520e-02,  9.57740053e-03,
  7.73385544e-02,  1.36428693e-01,  7.79062571e-01,  1.99306208e-02,
  1.38539965e-02,  1.35050777e-02,  1.96148399e-02, -3.21511327e-02,
  2.78810682e-02,  3.65736787e-02,  2.58612655e-04, -1.44393227e-02,
 -3.63945526e-02,  1.39593555e-02, -2.11409944e-02,  5.72032401e-03]

def linear_regression_intrcpt_submission():
  '''
    copy the intercept value from your notebook into here.
    :return: the intercept value.  
  '''
  return -1.260470039163094e-16

def classification_coeff_submission():
  '''
    copy the values from your notebook into a list in here. make sure the values
    seperated by commas
    :return: list of coefficiants for the classification problem.  
  '''
  return [[-1.14888407, -0.46914789,  0.13509315, -0.45974826, -0.34399461, -0.27641878,
  -0.39650568, -0.03751856,  0.13095072,  0.57231221, -0.70769723,  0.19408778,
   0.00238034,  0.83114968,  1.9584107,  -0.80262472, -0.03936414,  0.32541045,
  -0.19177923, -0.22886109,  0.63438591,  0.4998931,  -0.15504522, -0.50291642,
  -1.36928918,  0.59189798,  0.51386132,  1.03008252]]

def classification_intrcpt_submission():
  '''
    copy the intercept value from your notebook into here.
    :return: the intercept value.  
  '''
  return [-1.31431253]

def classification_classes_submission():
  '''
    copy the classes values from your notebook into a list in here. make sure the values
    seperated by commas
    :return: list of classes for the classification problem.  
  '''
  return [0, 1]