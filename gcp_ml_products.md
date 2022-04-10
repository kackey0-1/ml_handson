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

## Solutions 
### When you want to Simplify the pipelines as much as possible and use fully-managed or even serverless services as far as you can
Use BigQuery & BigQuery ML

- BigQuery
  - You can use Standard SQL and CLI interfaces via bq command
  - BigQuery Jobs
    - You can use BigQuery jobs to automate tasks and operations
- BigQuery ML
  - able to train ML models with rich set of algorithms with data.
  - able to perform feature engineering and hyperparameter tuning
  - able to export BigQuery ML models to a Docker Images as required

About Vertex AI, 
it is managed service and enable you to use AutoML and custom training efficiently.
But this is not serverless service especially for custom training.

### When you want to automate entire process of train to production start-up from static deep
Vertex AI Pipelines can run pipelines built by using TFX(=TensorFlow Extended)
<img src="https://s3.amazonaws.com/media.whizlabs.com/learn/ml19.png" />
