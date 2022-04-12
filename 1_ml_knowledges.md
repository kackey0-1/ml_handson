# Model index
## Unsupervised Learning
### K-Means
### MeanShift
### Gaussian Mixture Model(=GMM)
### Variational Bayesian Gaussian Mixture(= VBGM)

### Hierarchical Clustering
Hierarchical Clustering creates clusters using a hierarchical tree. 
It may be effective on recommendation system but it is heavy with a lot of data.

## Supervised Learning
### Linear Model
- Simple Linear Model
- L1 Lasso Regression
  - linear model with penalties
- L2 Ridge Regression
  - [//]: # (TODO)
- Logistic Regression
  - Binary Logistic Regression
  - Multiclass Logistic Regression

### KNN(K-Nearest Neighbor)
- supervised ML algorithm for classification

### SVM(Support Vector Machine)
- supervised ML algorithm for classification
  1. K-NN distances are computed 
  2. These distances are not between data points, but with hyper-plane, that better divides different classifications

### XGBoost
  - Optimized Gradient Boosting algorithm through parallel processing tree-pruning, handling missing values and regularization to avoid over-fitting / bias
  - Evolution of version of Decision Trees. this has been widely used in fraud detection field(unsupervised learning). and has had many positive results.
### Deep Learning

#### Convolutional Neural Networks
- Used for image classification
- Used with 
  - Kernel Selection
    - filters or kernels are computations on a sub-matrix of pixels
    - We use multiple convolution filters or kernels that run over the image and compute a dot product
  - Stride
    - the amount of stride we choose affects the size of the feature extracted
  - Max Pooling Layer
    - Max pooling layer helps reduce the spatial size of the convolved features and also helps reduce over-fitting by providing an abstracted representation of them
- [//]: # (TODO Check which problem is suitable for)

#### Matrix Factorization
- Used for recommendation system
- Can be used with Collaborative Filtering

#### FeedForward Neural Networks
The classic example of neural networks. In fact, they were the first and most elementary type of artificial neural network.    

Feedforward Neural Networks are mainly used for supervised learning when data, mainly numerical, to be learned is neither time-series nor sequential(Such as NLP)

#### Recurrent Neural Network
Recurrent Neural Network is a class of artificial neural networks where connections between nodes form a directed graph along temporal sequence.

#### Transformers
Deep learning model that can give different importance to each part of the input data. this is used for NLP(Natural Language Processing and Computer Vision) area

#### GAN Generative Adversarial Learning
GAN is a special class of machine learning frameworks used for the automatic generation of facial images.
GAN can create new cha

#### Autoencoder and self-encoder
Neural Network aimed to transform and learn with a compressed representation of raw data.(Unsupervised Learning)

Autoencoder and self-encoder are useful when you need to reduce the number of variables under consideration for the model, therefore for dimentionality reduction.

#### Collaborative Filtering
Collaborative Filtering works the idea that a user may like same things of the people with similar profiles and preferences. So exploiting the choices of other users, the recommendation system makes a guess and can advise people on things not yet been rated by them.
<img src="https://s3.amazonaws.com/media.whizlabs.com/learn/ml33.png">

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

## Cross-Validation
Cross-Validation involves running out modeling process on various subsets of data.
Obviously, Cross-Validation creates a computational load. Therefore, it can be prohibitive in very large datasets, but it is great when you have smalll datasets

<img scr="https://s3.amazonaws.com/media.whizlabs.com/learn/38.png">


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

## Feature Engineering
### Ordinal Encoding
Ordinal Encoding simply creates a correspondence between each unique category with an integer.
  
### One-Hot Encoding
One-Hot Encoding simply creates a sparse matrix with values that indicate the presence(or absence) of each possible value.
<img src="https://s3.amazonaws.com/media.whizlabs.com/learn/36.png">

### Feature Crosses
Feature Crosses creates a new feature created by joining or multiplying multiple variables to add further predictive capabilities, such as transforming the geographic location of properties into a region of interest.
- this will add non-linearity
- To transform the categorical features to simplify the model and make it more efficient and faster

### Embeddings
Embeddings are often used with texts and in NLP(Natural Language Processing) and address the problem of complex categories linked together.
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
