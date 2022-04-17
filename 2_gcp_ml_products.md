# GCP Products
## Queueing Service
### Pub/Sub
- to capture the data stream
- It's convenient in many ways, such as being loosely coupled and easy to scale.

This document may give us more useful information
https://developers.cyberagent.co.jp/blog/archives/1672/

---

## Data Cleaning Service
### Dataprep
Dataprep allows users to explore data visually by transforming the file into CSV, JSON, or in a graphical table format.
- Provisioning: Fully automated provisioning of clusters
- System Integration: BigTable and BigQuery
- Ease of Use: Easy to use
- Approach: Fully managed, No ops approach
- Unique For: UI driven processing of data(cleaning/exploration/preparation)

### Dataproc
With the in-built monitoring system, you can transfer your cluster data to your applications. 
You can get quick-reports from the system and also have the feature of storing data in Google’s BigQuery.
- Provisioning: provisioning clusters is done manually
- System Integration: Apache Spark and Hadoop(managed Hadoop service)
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

### Could Data Fusion
Could Data Fusion is a managed service for quickly building data pipelines and ETL processes.
It is based on the open-source CDAP(Clinical Data Analytics Platform) project and therefore is portable to any environment.
It has a visual interface that allows you to create codeless data pipelines as required.

- Data Warehouse
- Data Migration
- Data Consolidation
- Master Data Management
- Data Consistency

<img src="https://s3.amazonaws.com/media.whizlabs.com/learn/ml35.png">

### Composer
[//]: # (TODO Check Composer products in details)

---

## Data Storage Service

### BigQuery
- Allow us to do Exploratory Data Analysis and Feature Selection
- Allow us to do Model building, Training and Hyperparameter tuning but not Automatic deployment and serving

### BigTable

---

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

### Document AI
A complete service for the automatic understanding of documents and their management,
Document AI, which integrates computer natural language processing, OCR and vision and enable us to create pre-trained templates aimed at intelligent document administration.

### Recommendation AI
It's a ready-to-use service for all the requirements. Users don't need to create models, tune, train, all that is done by the service with users' data. Also delivery is automatically done, with high-quality recommendations via web, mobile, email.

#### Features
- Select your recommendation type
- Select your objective
- Set business rules

#### Recommendation Types
- Others you may like
- Frequently Bought Together
- Recommended for you
- Recently Viewed
  - This recommendation is useless for new products
  - And this is actually not recommendation 

<img src="https://s3.amazonaws.com/media.whizlabs.com/learn/ml24.png">

### AutoML
#### AutoML Tables
AutoML tables is aimed to automatically build and deploy models on your data in the fastest way possible. It is integrated within BigQuery ML and is available i the unified Vertex AI.

#### AutoML Vision
AutoML Vision lets you train models to classify your images with your own characteristics and labels. 
So you can tailor your work as you want.

#### AutoML Vision Edge
AutoML Vision Edge lets you model deployed on edge devices such as mobile phone.

### Vision AI
Vision AI uses pre-trained models trained by Google. This is powerfull, but less customizable for customized classifications.

### Video AI
Video AI manages videos, not images.
It can extract metadata from any streaming video, get insights in a far shorter time, and let trigger events

### TensorFlow Extended
TensorFlow Extended is for deploying production ML pipelines, and it doesn't have any AutoML Services.

