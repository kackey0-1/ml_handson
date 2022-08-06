# Ambiguous Things
## TabNet algorithm with TensorFlow
TabNet is to effectively apply deep neural networks on tabular data which still consists of a large portion of users and processed data across various application such as healthcare, banking, retail, finance, marketing, etc.

https://www.geeksforgeeks.org/tabnet/

## About Reinforcement Learning
Reinfocement Learning Algorithm provides a software agent that evaluates possible solutions through a progressive reward in repeated attempts. RL does not need to provide labels.

But it requires a lot of data and several trials and the possibility to evaluatethe validity of each attempts.

- Example of RL Algorithm
  - Q-Learning
  - Markov Decision Processes
  - SARSA(State Action Reward State Action)


## About AutoEncoder Neural Network
- Autoencodoer
  - Autoencoder is a type of artificial neural network that is used in the case of unlabeled data(unsupervised learning).
  - Autoencoder is an excellent system for generalization and therefore to reduce dimensionality, training the network to ignore insignificant data(noise)

## Boosted Tree - XGBoost
XGBoost is evolution of the decision trees, has recently been widely used.

This is supervised learning!!

<img src="https://s3.amazonaws.com/media.whizlabs.com/learn/ml8.png"/>

Consider using XGBoost for any supervised machine learning task when statisfies the following criteria
- When you have large number of observations in training data
- Number features < number of observations in training data
- It performs well when data has mixture numerical and categorical features or just numerical features
- When the model performance metrics are to be considered

https://www.kdnuggets.com/2020/12/xgboost-what-when.html

## Binary Classification
Logistic regression with a classification threshold too high.

Lowering the classification threshold classifies more items as positive, thus increasing both False Positives and True Positives.

- Accuracy
  - (TP + TN)/(TP+FP+FN+TN)
- Precision: Rate of correct positivve idencifications
  - Precision measures the percentage of emails flagged as spam that were correctly classified.
  - TP/(TP+FP)
  - Precision will be more important when you want to avoid FP detection like spam.
- Recall: Rate of real positive correctly identified
  - Recall measures the percentage of actual spam emails that were correctly classified.
  - TP/(TP+FN)
  - Recall will be more important when you can accept FP detection like medical check.

TP FP
FN TN

An ROC curve plots TPR vs. FPR at different classification thresholds. 
Lowering the classification threshold classifies more items as positive, thus increasing both False Positives and True Positives. The following figure shows a typical ROC curve.

https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc

## About Kubeflow Pipelines
It is within the Kubeflow ecosystem, which is the machine learning tookit for Kubernetes

- Using packaged tempaltes
in Docker images in a k8s environment
- Manage your various test/experiments
- Simplifying the orchestration of ML pipelines
- Reuse components and pipelines

## About Scaling
- Feature Clipping
  - Feature Clipping caps all numbers outside a certain range
- Log Scaling
  - Scaling means transforming feature values into a standard range, like from 0 and 1.
- Z-Score
  - z-score is similar to scaling, but uses the deviation from the mean divided by the standard deviation, which is the classic index of variability. So it gives how many standard deviations each value is away from the mean.

Note: 
  - What is z-test ?
    - z-test is a statistic that is used to prove if a sample mean belongs to specific population.
    - For example, it is used in medical trials to prove whether a new drug is effective or not.

https://www.investopedia.com/terms/z/z-test.asp

## About Bias-Variance dilenma
- The bias error is the non-estimable part of the learning algorithm. 
  - The higher the Bias is, the more underfitting there is.
- Variance is the sensitivity to differences in the training dataset.
  - The higher Variance is, the more overfitting there is.

<img src="https://s3.amazonaws.com/media.whizlabs.com/learn/ml17.png" />

https://towardsdatascience.com/understanding-the-bias-variance-tradeoff-165e6942b229

- Blending
  - Blending indicates an ensemble of ML models
- Learning Rate
  - Learning Rate is hyperparameter in neural networks
- Feature Cross
  - Feature Cross is the method for obtaining new feature by multiplying other ones
- Bagging
  - Bagging is an ensemble method like Blending

## About quick and managed solution for ML automation
Vertext AI Pipelines and TensorFlow Extended TFX!!

- Cluster Compute Engine and KubeFlow
- GKE and TFX
- GKE and KubeFlow

All options are correct. But not optimal for a quick and managed solution

## ML Product which is fully managed and serverless services to simplify the ML pipeline.

- BigQuery and BigQuery ML
  - can do feature engineering
  - of course can train ML models
  - can setup scheduled jobs 
  - can perform hyperparameter tuning
  - can export a BigQuery ML model to a Docker image


## About Feature Engineering 
- Principal Component Analysis(PCA)
  - PCA is a technique to reduce the number of features by creating new variables obtained from linear combinations or mixes of the original variables.
  - PCA can replace them but retain most of the information useful for the model
  - created features are all independent of each other
  - A linear model is assumed as a biasis. Therefore, the variables are independent of each other.
- Feature Crosses
  - Feature Crosses are for the same objective, but they add non-linearity
- Functional Data Analysis
  - Functional Data Analysis has the goal to cope with complexity, but it is used when it is possible to substitute features with functions-.
- Embeddings
  - Embeddings, which transforms largre sparse vectors into smaller vectors are used for categorical feature
  - a learned representation for text where words that have the same meaning have a similar representation

https://developers.google.com/machine-learning/crash-course/embeddings/categorical-input-data
https://builtin.com/data-science/step-step-explanation-principal-component-analysis

## About ML Production 
To organize and manage training, validatio, tuning and updating models with new data, distribution and monitoring in production.

Adopt Vertex AI: Custom tooling and pipelines!!

- Migrate all models to BigQuery ML with AutoML
  - On 2021-06-29, AutoML Table models are available in BigQuery ML.
  - https://cloud.google.com/blog/products/data-analytics/automl-tables-now-generally-available-bigquery-ml
- Migrate all models to AutoML Tables
  - AutoML Tables enables your entire team to automatically build and deploy state-of-the-art machine learning models on structured data at massively increased speed and scale

Vertex AI integrates many GCP ML services, especially AutoML and AI Platform, and includes many different tools to help you in every step of the ML workflow.

There is two strategies for ML training
1. AutoML
2. Personalized Training(custom training)

<img src="https://s3.amazonaws.com/media.whizlabs.com/learn/ml26.png">

## About Neural Networks
- Feedforward Neural Network(Sequantial Neural Network in Keras)
  - the classic example of neural networks. 
  - Feedforward Neural Networks are mainly used for supervised learning when the data mainly numerical, to be learned is neither time-series nor sequential(such as NLP)
- Convolutional Neural Network
  - for image data
    - using kernel selection
    - using stride
    - using max pooling layer
- Recurrent Neural Network
  - RNN is a class of artificial neural networks where connections between nodes form a directed graph along a temporal sequence
  - this is used for NLP and Time-Series as well
  - 時系列や自然言語などのシーケンスデータのモデリングを強力に行うニューラルネットワーククラス
- Transformers
  - Transformer is a deep learning model that can give different importance to each part of the input data
  - Used for Natural Language Processing
- Reinforcement Learning
  - Reinforcement Learning provides a software agent that evaluates possible solutions through a progresive reward in repeated attempts.
  - it does not need to provide labels
  - Q-Learning
- GAN: Generative Adversarial Network
  - Neural Network to generate images
  - A special class of machine learning frameworks used for the automatic generation of facial images
- Autoencoder and self-encoder
  - Autoencoder is a neural network aimed to transform and learn with a compressed representation of raw data
  - Autoencoder is a type of artificial neural network that is used in the case of unlabeled data(unsupervised learning).

## About AutoML Tables & BigQuery ML & Vertex AI
AutoML Tables
- Abailable ML Architectures
  - Linear 
  - Feedforward deep neural network
  - Gradient Boosted Decision Tree
  - AdaNet
  - Ensembles of various model architectures
- Automated Feature Engineerng Tasks
  - Normalization 
  - Encoding and embeddings for categorical features
  - Timestamp columns management(important in our case)

Note: 

AutoML Tables is available in BigQuery ML.
But AutoML Tables has additional automated feature engineering and is integrated into Vertex AI

## About Recommendation
- Matrix Factorization
  - Matrix Factorization is a simple embedding model
- Collaborative Filtering 
  - Collaborative Filtering is a technique used by recommender system.
  - Collaborative Filtering works on the idea that a user may like the same things of the people with similar profiles and preferences

https://developers.google.com/machine-learning/recommendation/collaborative/matrix

## About Hierarchical Clustering
- Hierarchical Clustering creates clusters using hierarchical tree.
- Hierarchical Clustering may be effective, but it is heavy with lots of data.

## About data pipeline process
- Cloud Dataflow
  - Cloud Dataflow has functionality for data processing such as batch and stream.
- Cloud Dataproc
  - Cloud Dataproc is the managed Hadoop Service
  - Cloud Dataproc could manage data pipeline
- Cloud Data Fusion
  - Cloud Data Fusion is a managed service for quickly building data pipelines and ETL processes
  - It is based on the open-source CDAP project and therefore is portable to any environment
  - Cloud Data Fusion has visual interface that allows you to create codeless data pipelines as required
- Cloud Dataprep
  - Cloud Dataprep is for cleaning, exploration and preparation ,and is used primarily for ML processes.

https://cloud.google.com/data-fusion

https://jayendrapatil.com/google-cloud-dataflow-vs-dataproc/#:~:text=Cloud%20Dataproc%20is%20a%20managed,%2C%20streaming%2C%20and%20machine%20learning.

## About Cloud TPU
GCP documentation states that the use of TPUs is advisable with models that:
- use TensorFlow
- need training for weeks or months
- have huge matrix computations
- have deals with big datasets and effective batch sizes

## About ML model for human dialogues
- Speech To Text
  - Speech To Text can convert voice to written text
- Cloud NLP
  - Cloud Natural Language API can understand text meanings such as syntax, feelings, content, entities and can create classifications
- Text to Speech
  - Txt to Speech can convert written text to voice
- Speech Synthesis Markup Language(SSML)
  - Speech Synthesis Markup Language(SSML) is not a service but a language used in Text-to-Speech requests
  - SSML gives you the abiilty to indicate how you want to format the audio, pauses, how to read acronyms, dates, times, abbreviations and so on.

## About Techniques or Algorithms
- Partail Least Squares
- Principal Components
  - Partial Least Square and Principal Components create new variables that are uncorrelated  
- Multivariate Multiple Regression
  - Multivariate Multiple Regression contained finds out ways to explain how different elements in variables react together to changes

- Multiple Linear Regression with MLE
  - Multiple Linear Regression is an OLS(Ordinary Least Square) method
- Maximum Likelihood Estimation
  - Maximum Likelihood Estimation requires independence for variables
  - Maximu Likelihood Estimation finds model parameter values, with probability, maximizing the likelihood of seeing the examples given the model

## About tf.data.Iterator
tf.data.Iterator is used for enumerating elements in a Dataset, using TensorFlow API, so it is not suitable for accessing tabular data.

## About Embedding
- Count Vector
- TF-IDF Vector
- Co-Occurence Matrix

Note:
- CoVariance Matrix
  - CoVariance matrices is square matrices with the covariance between each pair of elements.
  - CoVariance measures how much the change of one with respect to another is related

## About UI tools that can help you work and solve all issues.
- Tensorboard
  - Profiling 
  - Monitoring model graph
  - Examine model graph
  - Working with embeddings
- Jupyter notebooks
  - development tools
- Kubeflow UI
  - Pipelines dashboard
  - Hyperparameter tuning 
  - Artifact Store
  - Jupyter notebooks

Note:
- KFServing
  - KFserving is an open source library for Kubernetes that enable serverless inferencing.
  - it works with TensorFlow, XGBoost, scikit-learn, PyTorch, and ONNX to solve issues linked to production model serving 
- Vertex AI
  - Vertex AI is a suite of services that combines AutoML and AI Platform
  - You can use both AutoML trainng and custom training

## About Anscombe Quartet Problem
Anscombe Quartet Problem is a phenomenon that statistic measurements such as R-square, coeffient of determination(決定係数) are same, but distribution is different from each other like image

<img src="https://upload.wikimedia.org/wikipedia/commons/e/ec/Anscombe%27s_quartet_3.svg">

- Not linear relation between independent and dependent variables
- Outliers that change the result

## About TensorFlow Libraries
- tf.RaggedTensor
  - RaggedTensor is a tensor with ragged dimensions, that different lengths like this: `[[6, 4, 7, 4], [], [8, 12, 5], [6], []]`
- tf.quantization
  - quabtization is aimed to reduce CPU and TPU GCP latency
- tf.train.Feature
  - tf.train is a feature for Graph-based Neural Structured model training
- tf.TFRecordReader

## TF tools
- TFProfiler
  - Profiler is a tool for checking the performance of your TensorFlow models and hepling you to obtain an optimized version
- TF function
  - TF Function is a transformation tool used to make graphs out of your pragrams.
  - TF fucntion helps to create performance and portable models but not for optimization
- TF Trace
  - TF tracing lets you record TensorFlow Python operations is a graph
- TF Debugging
  - TF debugging is for debugging v2 and creates a lot of debug information
- TF Checkpoint
  - Checkpoints catch the value of all parameters in a serialized SavedModel format
  


