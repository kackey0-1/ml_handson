# Ambiguous Things v2

## About GCP products
- Cloud Armor Security policies
  - Cloud Armor is a security service at the edge against attacks like DDoS
- Cloud HSM
  - Cloud HSM is a service for cryptography based on special and certified hardware and software

- VPC(Virtual Private Cloud)
  - VPC lets you build a security perimeter that is not accessible from outsides
- Cloud Data Loss Prevention
  - Cloud Data Loss Prevention is a service that can discover, conceal and mask personal information in data.

## About Non-Parametric ML algorithm
- Non-Parametric 
  - Non-Parametric methods, which do not assume any distribution with any function with parameters.
  - Algorithms that do not make strong assumptions about the form of the mapping function are called nonparametric machine learning algorithms

  - Example of Algorithms
    - K-Nearest Neighbor
        - KNN is a simple supervised learning algorithm
    - Decision Trees like CART and C4.5
        - Decision Tree has a series of tests inside a flowchart-like structure.
    - Support Vector Machines

https://machinelearningmastery.com/parametric-and-nonparametric-machine-learning-algorithms/

## About ensemble type algorithms
- Random Forests
- XGBoost
- Gradient Boost

https://towardsdatascience.com/all-machine-learning-algorithms-you-should-know-in-2021-2e357dd494c7

Note:
- DCN(Deep & Cross Networks)
  - DCN are a new kind of Neural Networks.

## About TFRecords
- BigQuery to Cloud Storage TFRecords 
  - The BigQuery to Cloud Storage TFRecords template is a pipeline that reads data from a BigQuery query and writes it to a Cloud Storage bucket in TFRecord format
https://cloud.google.com/dataflow/docs/guides/templates/provided-batch#bigquerytogcstfrecords


## About lazy learning
- Lazy Learning
  - Lazy Learning means that the algorithm only stores the data of the training part without leaning a function.
  - The stored data will be used for evaluation of a new query point


## About TensorFlow Probability
- Probability distributions and differentiable and injective functions
- Tools for deep probabilistic models building
- Inference and Simulation methods support
- Optimizers such as Nelder-Mead, BFGS, and SGLD

## About BigQueryML Open
BigQueryML Open is related to Open Data
https://github.com/doitintl/BigQueryML-Examples

## About TensorFlow-Hub
TensorFlow Hub is ready to use repository of trained machine learning models.

## About GCP for cost optimization
- Ephemeral Instance
  - used for a limited time
  - ephemeral instances, not as long living ones
- Automatic shutdown routine
- Preemptible VMs per long-running interrupible task
  - Preemptible VMs are far cheaper than normal instances, which for long runnning (batch) large experiments
  - Compute Engine might stop (preempt) these instances if it needs to reclaim the compute capacity for allocation to other VMs
- Monitoring Alerts about GCP usage

## About Tools to explain NeuralNetworks
- What-If Tool 
  - What-If Tool(WIT) is an open source tool that lets you visually understand classification and regression ML models.
  - WIT lets you see data points distributions with different shapes and colors and interactively try new inferences.
  - WIT shows which features affect your model the most, together with many other characteristics
- Language Interpretability Tool(LIT)
  - Language Interpretability Tool is an open source tool developed specifically to explain and visualize NLP natural language processing models
  - LIT offers visual explanations of the model's predictions and analysis with metrics, tests and validations
- Integrated Gradient
  - Integrated Gradient is an explainability technique for DNN that gives information about the model's prediction
  - Integrated Gradient works highlighting the feature importance.
  - Integrated Gradient computes the gradient of the model's prediction output regarding its input features without modification to the original model.

Note:
- Tensorboard
  - Tensorboard provides visualization and tooling needed for experiments, not for explaining inference.
  - We can access the What-If tool from TensorBoard
- Tableuu and Looker
  - both of them are graphical tools for data reporting
- Principal Component Analysis 
  - PCA transforms and reduces the number of features by creating new variables from linear combinations of the original variables

## About BigQuery method
- EXCEPT
  - EXCEPT gives all rows or fields on the left side execpt the one coming from the right side of the query
- ROLLUP
  - ROLLUP is a group function for subtotals
- UNNEST
  - UNNEST gives the elements of a structured file like json
- LAG
  - LAG returns the field value on a preceding row

## About avoiding multicollinearity and optimizing categories
- FEATURE_CROSS
  - a feature cross is a new feature that joins two or more input features together
  - Usually numeric new features are created by multiplying two or more other features
- QUANTILE_BUCKETIZE
  - quantile bucketize groups a continuous numerical feature into categories with the bucket name as the value based on quantiles
  - Bucketizes a continuous numerical feature into a STRING with the bucket name as the value based on quantiles.

https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-preprocessing-functions#quantile_bucketize

## About tools for direct access to BigQuery
- tf.data.dataset
  - <!-- TODO write codes for this --> 
  - tf.data.dataset reader for BigQuery is the way to connect directly to BigQuery from TensorFlow or Keras
- BigQuery Python Client library
  - for any framework, we can use BigQuery Python client library
- BigQuery I/O Connector
  - BigQuery I/O Connector is the way to connect directly to BigQuery from Dataflow

Note:
- BigQuery Omni
  - BigQuery Omni is for multi-cloud analytics solution
  - You can access from BigQuery data across GoogleCloud, AWS, Azure

## About Vertex AI Explainable AI
Vertex AI Explainable AI helps to detect it, both for classification and regression tasks. 
So functions are useful for testing, tuning, finding biases and thus improving the process.

You can get explanations from Vertex Explainable AI both for online batch inference but only regarding these ML models.

- Structured data models(AutoML, classification and regression)
- Custom-trained models with tabular data and images

Vertex AI Explainable AI uses three methods for feature attributions
- Sampled Shapley
  - Sampled Shapley uses scores for each feature and their permutations
- Integrated Gradextension of the integrated gradients
  - Integrated Gradextension of the integrated gradients method creates saliency map with overlapping regions of the image
- XRAI method
  - XRAI method combines the integrated gradients method with additional steps to determine which regions of the image contribute the most to a given class prediction

https://cloud.google.com/vertex-ai/docs/explainable-ai/overview#feature-attribution-methods

## About Concurrency for ML performance
- tf.distribute.MirroredStrategy
  - MirroredStrategy lets you use multiple GPUs in a single VM, with a replica for each CPU
- tf.distribute.TPUStrategy
  - TPUStrategy lets you use TPU to process
- tf.distribute.MultiWorkerMirroredStrategy
  - MultiWorkerMirroredStrategy lets you use multiple machines
- tf.distribute.OneDeviceStrategy
  - this is like the default strategy, is for a single device, so a single virtual CPU

https://www.tensorflow.org/guide/distributed_training

## About eager mode
When you develp and test a model, the eager mode is really useful because it lets you execute operations one by one and facilitate debugging.

But when in production, it is better to use graphs, which are data structures with Tensors and integrated computations Python indepenedent.
In this way, they can be deployed on different devices(like mobiles) and are optimizable.

to do that, you have to use tf.function decoration function for a new tf.Graph creation

<!-- TODO checkout eager mode execution -->
https://colab.research.google.com/github/zaidalyafeai/Notebooks/blob/master/Eager_Execution_Enabled.ipynb

## About Vertex AI Pipeline and Kubeflow
- Vertex AI Pipeline
  - Vertex AI Pipeline is a managed service in GCP
  - Vertex AI support code written with Kubeflow Pipelines SDK v2 domain-specfic language(DSL)
  - Vertex AI can use Cloud Storage FUSE. so Vertex AI can leverage Cloud Storage bucket like file systems on linux or macos.
- Kubeflow
  - an open source tool based on Kubernetes and TensorFlow for any environment

## About Cloud Composer
- Cloud Composer is not ETL tools.
- Cloud Composer is used in ML proceesses, but as a workflow tool not for data transformation

https://cloud.google.com/vertex-ai/docs/datasets/datasets

## About Recommendation System
- Cosine Similarity
  - Cosine Similarity is method to discover similarities between products so that you may recommend a movie to another user because the different user like similar objects
  - Take two products and their characteristics(all transformed in numbers=vectors)
  - Compute difference between vecotrs in the euclidean space. Geometrically, that means that they have different lengths and different angles

Note:
- Matrix Factorization
  - this is used for recommendation system as well
  - Matrix Factorization is used with a significant amount of data
  - Matrix Factorization has the problem of reducing dimensionality.

## About Preprocessing
When you have various fields that have no value or report NaN.

- Compute Mean/Median for numeric measures
- Replace Categories with the most frequent one
- Use another ML model for missing values guess

https://towardsdatascience.com/7-ways-to-handle-missing-values-in-machine-learning-1a6326adf79e


## Question 43 & 48
## About Logistic Regression
- ROC-AUC 
  - ROC curve=(receiver operating characteristic curve)
    - ROC is a graph showing the behaivior of the model with positive guesses at different classification threshold
  - AUC=(Area Under the Curve) index
  - AUC index is the area under the ROC curve and indicates the capability of binary classifier to discriminate between two categories.
  - it is always a value between 0 and 1

- Log Loss
  - Log Loss is a loss function used especially for logistic regression
  - it measures loss so it is highly dependent on threshold

<img src="https://s3.amazonaws.com/media.whizlabs.com/learn/8.2.png">


## About Loss function
- Log Loss
  - with a logistic regression model, the optimal loss function is the log loss
  - The intuitive explanation is that when you want to emphasize the loss of bigger mistakes, you need to find a way to penalize such differences.
- Mean Bias Error
  - Mean Bias Error takes just the value of the difference between prediction and actual outcomes


