# Ambiguous Things
## TabNet algorithm with TensorFlow
TabNet is to effectively apply deep neural networks on tabular data which still consists of a large portion of users and processed data across various application such as healthcare, banking, retail, finance, marketing, etc.

https://www.geeksforgeeks.org/tabnet/

## Boosted Tree - XGBoost
XGBoost is evolution of the decision trees, has recently been widely used.

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

https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc

## About Scaling
- Feature Clipping
  - Feature Clipping caps all numbers outside a certain range
- Log Scaling
  - Scaling means transforming feature values into a standard range, like from 0 and 1.
- Z-Score
  - z-score is similar to scaling, but uses the deviation from the mean divided by the standard deviation, which is the classic index of variability. So it gives how many standard deviations each value is away from the mean.

Note: 
  - What is z-test ?
    z-test is a statistic that is used to prove if a sample mean belongs to specific population. For example, it is used in medical trials to prove whether a new drug is effective or not.

## About Bias-Variance dilenma
- The bias error is the non-estimable part of the learning algorithm. 
  - The higher it is, the more underfitting there is.
- Variance is the sensitivity to differences in the training dataset.
  - The higher it is, the more overfitting there is.

<img src="https://s3.amazonaws.com/media.whizlabs.com/learn/ml17.png" />

https://towardsdatascience.com/understanding-the-bias-variance-tradeoff-165e6942b229

## ML Product which is fully managed and serverless services to simplify the ML pipeline.

- BigQuery and BigQuery ML
  - can do feature engineering
  - of course can train ML models
  - can setup scheduled jobs 
  - can perform hyperparameter tuning
  - can export a BigQuery ML model to a Docker image


## About Feature Engineering 
- Functional Data Analysis
  - Functional Data Analysis has the goal to cope with complexity, but it is used when it is possible to substitute features with functions-.
- Embeddings
  - Embeddings, which transforms largre sparse vectors into smaller vectors are used for categorical feature
  - a learned representation for text where words that have the same meaning have a similar representation

## About ML Production 
To organize and manage training, validatio, tuning and updating models with new data, distribution and monitoring in production.

- Adopt Vertex AI: Custom tooling and pipelines
- Migrate all models to BigQuery ML with AutoML
  - On 2021-06-29, AutoML Table models are available in BigQuery ML.
  - https://cloud.google.com/blog/products/data-analytics/automl-tables-now-generally-available-bigquery-ml
- Migrate all models to AutoML Tables
  - AutoML Tables enables your entire team to automatically build and deploy state-of-the-art machine learning models on structured data at massively increased speed and scale

## About Neural Networks
- Feedforward Neural Network
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

## About Recommendation
- Matrix Factorization
  - Matrix Factorization is a simple embedding model
- Collaborative Filtering 
  - Collaborative Filtering is a technique used by recommender system.
  - CF works on the idea that a user may like the same things of the people with similar profiles and preferences

https://developers.google.com/machine-learning/recommendation/collaborative/matrix

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

https://jayendrapatil.com/google-cloud-dataflow-vs-dataproc/#:~:text=Cloud%20Dataproc%20is%20a%20managed,%2C%20streaming%2C%20and%20machine%20learning.

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

## Question 41
- Multiple Linear Regression with MLE

## About Embedding
- Count Vector
- TF-IDF Vector
- Co-Occurence Matrix

Note:
- CoVariance Matrix
  - CoVariance matrices is square matrices with the covariance between each pair of elements.
  - CoVariance measures how much the change of one with respect to another is related

## About Anscombe Quartet Problem
Anscombe Quartet Problem is a phenomenon that statistic measurements such as R-square, coeffient of determination(決定係数) are same, but distribution is different from each other like image

<img src="https://upload.wikimedia.org/wikipedia/commons/e/ec/Anscombe%27s_quartet_3.svg">

- Not linear relation between independent and dependent variables
- Outliers that change the result




