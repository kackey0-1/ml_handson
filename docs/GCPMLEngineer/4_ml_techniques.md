# Technique
## Data Exploratory
### Suitable for accessing tabular data as required
- BigQuery Python Client
  - BigQuery Python Client allows you to get BQ data in Pandas
- BigQuery I/O Connector
  - BigQuery I/O Connector is used by DataFlow(Apache Beam) for reading Data for transformation and processing.
- tf.data.dataset reader
  - You must first access the data using `tf.data.dataset` reader for BigQuery

Not `tf.data.Iterator` because `tf.data.Iterator` is used for enumerating elements in a Dataset, using TensorFlow API.

---

## TensorFlow API
### tf.RaggedTensor
RaggedTensor is a tensor with ragged dimensions, that is with different lengths like this `[[6,4,7,4],[], [8,12,5], [9], []]`

### tf.quantization
quantization is aimded to reduce CPU and TPU GPU latency, processing, and power.

### tf.train.Feature
`tf.train` is feature for Graph-based Neural Structured model training

### TFProfiler
TensorFlow Profiler is a tool for checking the performance of your TensorFlow models and helping you to obtain an optimized version.

In TensorFlow 2, the default is eager execution. So, one-off operations are faster, but recurring ones may be slower. So you need to optimize the model.

### TF function
TF function is a transformation tool used to make graphs out of your programs. It helps to create performant and portable models but is not a tool for optimization.

### TF tracing
TF tracing lets you record TensorFlow Python operations in a graph.

### TF debugging
TF debugging is for Debugger V2 and creates a log of debug information

### TF Checkpoint
TF Checkpoins catch the value of all prameters in a serializaed SavedModel format.

### TabNet with TensorFlow Estimator API
### TensorFlow Object Detection API
- designed to identify and localize multiple objects within images 

### TensorFlow Extended(=TFX)
- A platform that allows you to create scalable production ML pipelines for TensorFlow projects, therefore KubeFlow.
- It allows you to manage entire life-cycle seamlessly from training, and validating, up to production start-up and management of the inference service.
- Executor components
  - Apache Beam
  - TensorFlow Extended
    - TensorFlow Data Validation (TFDV)
    - [//]: # (TODO check other components)
  - simple python program
  - container(Kubeflow, Apache Airflow)

## BigQuery ML
- XGBoost by BQ
  - designed for structured data
- BigQuery Boosted Tree
  - an ensemble of Decision Trees which is not suitable for time-series data
- BigQuery ARIMA
  - ML ARIMA_PLUS can manage time-series forecasts
---
# How to improve learning quality
## Normalization Techniques
### Feature Clipping
  - Feature of Clipping is that eliminates outliers that are too high or too low

### Log Scaling
Log Scaling can compress the data range: x1 = log(x)

Log Scaling uses the logalgarithms instead of your values to change the shape. This is possible because the log function preserves monotonicity.

### Scaling to a range
  - Scaling means transforming feature values into a standard range
    - from 0 and 1
    - or sometimes -1 to +1
    - or even distribution between minimum and maximum

### Z-score
  - gives us insight of how many standard deviation each value is away from the mean.

Note: z-test is used to prove if a sample mean belongs to a specific population. For example, it is used in medical trials to prove whether a new drug is effective or not.

---

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

[//]: # (TODO add some more description)
#### Count Vector
Count Vector gives a matrix with the count of every single word in every example. 0 if no occurence.
#### TF-IDF Vector
TF-IDF vectorization counts words in entire experiments, not single example or sentence.
#### Co-Occurence Matrix
Co-Occurence Matrix puts together words that ocurr together. So it is more useful for text understanding.

Note: CoVariance Matrix is not embedding. since CoVariance Matrixes are square matrixes with the covariance between each pair of elements. it measures how much the change.

## Functinal Data Analysis
Functinal Data Analysis, which copes with complexity. but it is used where it is possible to substitute features with `functions-`.

[//]: # (TODO add some more description)

## Principal Components Analysis(= PCA)
A technique to reduce the number of features by creating new variables obtained from linear combinations or mixes of the original variables, which can replace them but retain most of the information useful for the model.

And new features are all independent of each other.

A linear model is assumed as a bias. Therefore the variables are called principal components.

## When you want to improve a Linear Regression model, unsatisfactory results caused by many variables are correlated.
If you have independent variables, some of which are correlated with each other. You have multi-collinearity; therefore you cannot use classical linear regression.

- Partial Least Squares
  - Partial Least Squares method uses projected new variables using functions

- Principal Components
  - The main PCA components reduce the variables while managing their variance. Hence, the ammount of variability contained in the original characteristics.
Partial Least Squares and Principal Companents create new variables that are uncorrelated.
  
- Multivariate Regression
  - Multivariate Regression finds out ways to explain how different elements in variables react together to changes

- Not Maximum Likelihood Estimation 
  - Maximum Likelihood Estimation requires independence for variables
  - Maximum Likelihood Estimation finds model parameter values with probability, maximizing the likelihood of seeing the examples given the model.

## Model Evaluation Technique
### Regression Model Evaluation
### Classification Model Evaluation
- Which metric for classification models evaluation gives you the percentage of real spam email that was recognized correctly?
  - Precision
    - Precision is the metric that shows the percentage of true positives related to all your positive class predictions
  - Recall 
    - this is correct answer [//]: # (TODO read more details)
  - Accuracy
    - Not Accuracy because this is the percentage of correct prediction on all outcomes
  - F1 Score
    - Not F1 score because this is harmonic mean between Precision and Recall

<img src="https://s3.amazonaws.com/media.whizlabs.com/learn/44.png">

## Monitoring Technique
### Data Validation Problems
- Omitted values(欠損値)
  - omitted values may change fundamental statistics like average for example.
- Duplicated examples
  - Duplicated examples may change fundamental statistics
- Bad labels
  - Having Bad labels leads to a bad model
- Bad feature values
  - Having Bad features leads to a bad model

Note
- `Categories` are not related to Data Validation. Usually categories are string variables that in ML usually are mapped in numerical set before learning

### ML Problems
## Over Fitting Problem
### How to address over fitting problem
- L1 Lasso Regression
- L2 Ridge Regression
- Dropout
- EarlyStop

## Anscombe Quartet Problem
Anscombe's Quartet ocmprises four data sets that have nearly identical simple descriptive statistic, yet have very different distributions and appear very different when graphed.

In Japanese:
回帰分析において、散布図はそれぞれ異なるのに回帰直線やその他の統計量が同じになってしまう現象

- Not linear relation between independent and dependent variables
- Outliers that change the result

<img src="https://upload.wikimedia.org/wikipedia/commons/e/ec/Anscombe%27s_quartet_3.svg">



