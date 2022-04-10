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

[//]: # (TODO)
# ML Evaluation 
- Classification model
  - Binary Classification
    - When there is an imbalance between true and false ratio, it is necessary to modify the classification threshold
    - https://developers.google.com/machine-learning/crash-course/classification/precision-and-recall
      - Precision: Rate of correct positive identification
      - Recall: Rate of real positive correctly identified

# Technique
- TensorFlow API
  - TabNet with TensorFlow Estimator API
  - TensorFlow Object Detection API
    - designed to identify and localize multiple objects within images 
- BigQuery ML
  - XGBoost by BQ
    - designed for structured data
  - BigQuery Boosted Tree
    - an ensemble of Decision Trees which is not suitable for time-series data
  - BigQuery ARIMA
    - ML ARIMA_PLUS can manage time-series forecasts

# How to address over fitting problems
- L1 Lasso Regression
- L2 Ridge Regression
- Dropout
- EarlyStop


# GCP Products
## Queueing Service
### Pub/Sub
- to capture the data stream
- It's convenient in many ways, such as being loosely coupled and easy to scale.

## Data Cleaning Service
### Dataprep
Dataprep allows users to explore data visually by transforming the file into CSV, JSON, or in a graphical table format.
- Provisioning: Fully automated provisioning of clusters
- System Integration: BigTable and BigQuery
- Ease of Use: Easy to use
- Approach: Fully managed, No ops approach
- Unique For: UI driven processing of data

### Dataproc
With the in-built monitoring system, you can transfer your cluster data to your applications. 
You can get quick-reports from the system and also have the feature of storing data in Google’s BigQuery.
- Provisioning: provisioning clusters is done manually
- System Integration: Apache Spark and Hadoop
- Ease of Use: simple, easy to use
- Approach: Hands-On, DevOps Approach
- Unique For: Data Science / ML Ecosystem

### Dataflow
ETL(Extract, transform, and load) data into multiple data warehouses at the same time.
Dataflow is considered as MapReduce replacement to handle large number of parallelization tasks.
to aggregate and extract insights in real-time in BigQuery
- Provisioning: Serverless, automatic provisioning of clusters
- System Integration: Apache Beam
- Ease of Use: Relatively difficult
- Approach: Fully managed, No Ops Approach
- Unique For: Batch and Streaming of data

### Composer  

## Data Storage Service

### BigQuery
- to create models
### BigTable

## AI Products
### Kubeflow Pipeline
an open-source platform to create and deploy ML workflow based on docker container
- Using packaged templates in Dokcer images in a k8s environment
- Manage your various tests/experiments
- Simplifying the orchestration of ML pipelines
- Reuse components and pipelines

### Vertex AI
- Train an ML without code(AutoML) and with custom
- Evaluate and Tune models
- Deploy models
- Manage prediction batch, online and monitoring
- Manage models version, workflows and retraining
- Manage the complete model maintenance cycle