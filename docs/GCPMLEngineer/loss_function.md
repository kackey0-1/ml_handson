# Evalution Function

## For Regression Problem
### Log Loss
Log Loss is a loss function used especially for logistic regression.
So it is highly dependent on threshold values.

<img src="https://s3.amazonaws.com/media.whizlabs.com/learn/2-43.png"/>

### Mean Square Error
Mean Square Error is the most frequently used loss function used for linear regression.
It takes the square of the difference between predictions and real values.

### Mean Absolute Error
Mean Absolute Error is a loss function.
It takes the absolute value of the difference between predictions and actual outcomes.

## For Classification Problem
### Softmax
softmax function is used in *multi-class classification* models which is clearly not suitable in the case of a binary-class logarithmic loss

## Others
### Mean Bias Error
Mean Bias Error takes just the value of the difference between predictions and actual outcomes.
So, it compensates positive and negative differences between predicted/actual values. 
It is used to calculate the average bias in the model.
