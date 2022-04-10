# Model index
 
## Unsupervised Learning
- K-Means
- MeanShift
- Gaussian Mixture Model(=GMM)
- Variational Bayesian Gaussian Mixture(= VBGM)

## Supervised Learning
- Linear Model
  - Simple Linear Model
  - L1 Lasso Regression
    - linear model with penalties
  - L2 Ridge Regression
    - [//]: # (TODO)
  - Logistic Regression
    - Binary Logistic Regression
    - Multiclass Logistic Regression
- KNN(K-Nearest Neighbor)
  - supervised ML algorithm for classification
- SVM(Support Vector Machine)
  - supervised ML algorithm for classification
    1. K-NN distances are computed 
    2. These distances are not between data points, but with hyper-plane, that better divides different classifications
- XGBoost
  - Optimized Gradient Boosting algorithm through parallel processing tree-pruning, handling missing values and regularization to avoid over-fitting / bias
  - Evolution of version of Decision Trees. this has been widely used in fraud detection field(unsupervised learning). and has had many positive results.
- Deep Learning
  - Convolutional Neural Networks
    - Used for image classification
    - Used with 
      - Kernel Selection
        - filters or kernels are computations on a sub-matrix of pixels
        - We use multiple convolution filters or kernels that run over the image and compute a dot product
      - Stride
        - the amount of stride we choose affects the size of the feature extracted
      - Max Pooling Layer
        - Max pooling layer helps reduce the spatial size of the convolved features and also helps reduce over-fitting by providing an abstracted representation of them
  - Matrix Factorization
    - Used for recommendation system

## Reinforcement Learning(RL)
RL provides a software agent that evaluates possible solutions through a progressive reward in repeated attempts.
it does not require labels. But it requires a lot of data and several trial and the possibility to evaluate the validity of each attempt.
- Q-Learning
- deep Q-network(DQN)
- deep deterministic policy gradient

[//]: # (TODO summarize other models evaluation)
# ML Evaluation 
- Classification model
  - Binary Classification
    - When there is an imbalance between true and false ratio, it is necessary to modify the classification threshold
    - https://developers.google.com/machine-learning/crash-course/classification/precision-and-recall
      - Precision: Rate of correct positive identification
      - Recall: Rate of real positive correctly identified

# Technique
## TensorFlow API
- TabNet with TensorFlow Estimator API
- TensorFlow Object Detection API
  - designed to identify and localize multiple objects within images 
- TensorFlow Extended(=TFX)
  - A platform that allows you to create scalable production ML pipelines for TensorFlow projects, therefore KubeFlow.
  - It allows you to manage entire life-cycle seamlessly from training, and validating, up to production start-up and management of the inference service.
  - Executor components
    - Apache Beam
    - tensorflow
    - simple python program
    - container(Kubeflow, Apache Airflow)

## BigQuery ML
- XGBoost by BQ
  - designed for structured data
- BigQuery Boosted Tree
  - an ensemble of Decision Trees which is not suitable for time-series data
- BigQuery ARIMA
  - ML ARIMA_PLUS can manage time-series forecasts

# How to improve learning quality
## Normalization Techniques
- Clipping
  - Feature of Clipping is that eliminates outliers that are too high or too low
- Log Scaling
- Scaling to a range
  - Scaling means transforming feature values into a standard range
    - from 0 and 1
    - or sometimes -1 to +1
    - or even distribution between minimum and maximum
- Z-score
  - gives us insight of how many standard deviation each value is away from the mean.

## Bias-Variance Dilemma
The bias error is the non-estimable part of the learning algorithm.
The higher it is, The more under-fitting there is.

Variance is the sensitivity to differences in the training set.
The higher it is, the more over-fitting there is.

So we have to find optimized point between the bias and variance

[//]: # (TODO read more documents and improve understanding)
https://atmarkit.itmedia.co.jp/ait/articles/2009/09/news025.html

## Feature Crosses
- this will add non-linearity
- To transform the categorical features to simplify the model and make it more efficient and faster

## Embeddings
Embeddings, which transforms large sparse vectors into smaller vectors are used for categorical data.

## Functinal Data Analysis
Functinal Data Analysis, which copes with complexity. but it is used where it is possible to substitute features with `functions-`.

[//]: # (TODO add some more description)

## Principal Components Analysis(= PCA)
A technique to reduce the number of features by creating new variables obtained from linear combinations or mixes of the original variables, which can replace them but retain most of the information useful for the model.

And new features are all independent of each other.

A linear model is assumed as a bias. Therefore the variables are called principal components.


# How to address over fitting problems
- L1 Lasso Regression
- L2 Ridge Regression
- Dropout
- EarlyStop
