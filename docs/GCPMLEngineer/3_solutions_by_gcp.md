# Solutions 
## When you want to Simplify the pipelines as much as possible and use fully-managed or even serverless services as far as you can
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

---

## When you want to automate entire process of train to production start-up from static deep
Vertex AI Pipelines can run pipelines built by using TFX(=TensorFlow Extended)
<img src="https://s3.amazonaws.com/media.whizlabs.com/learn/ml19.png" />

---

## When you want to automate the re-development and distribution process every time it recieves a new file
1. Could Storage to recieve new files
2. Trigger process
    - Could Functions
    - Pub/Sub
3. Other services like Dataflow

<img src="https://s3.amazonaws.com/media.whizlabs.com/learn/ml21.png">

---

## When you need create a muti-class classification ML model with Keras Sequential model API. in particular, your model must indicate the main categories of a text. 

- Use Feedforward Neural Network
  - is a kind a DNN(Deep Neural Network), widely used for many applications
- N-grams for tokenize text
  - for tokenizing text is a contiguous sequence of items(usually words) in NLP
- Softmax function
  - is an activation function for multi-class classification
- Pre-trained embeddings
  - Embeddings are used for reducing high-dimensional tensors, so categories.
- Dropout Layer
  - Dropout layyer is used for regularization, eliminating input features randomly
- Categorical cross-entropy
  - Categorical cross-entropy is a loss function for multi-class classification

but not K-Means. because this is for unsupervised learning

---

## When you train your DNN with TensorFlow, your input data does not fit into RAM memory. Which can you do in the simplest way ?

tf.data.Dataset allows you to manage a set of complex elements made up of several inner components.
It is designed to create efficient input pipelines and to iterate over the data for their processing.
These iterations happen in streaming. So they work even if the input matrix is very large and doesn't fit in memory.

- Use a queue with tf.train.shuffle_batch
  - it is far more complex, even if it is feasible.

- pandas.DataFrame
- NumPy
  - these  are work in real memory. so they don't solve the problem

---

## When you want to quickly create an optimal model, both from the point of view of the algorithm used and the tuning and life cycle of the model. You work on historical tabular data. 
You work for a large retail company. You are preparing a marketing model. The model will have to make predictions based on the historical and analytical data of the e-commerce site (analytics-360). In particular, customer loyalty and remarketing possibilities should be studied. 

 - AutoML Tables
 - Vertex AI

 would be suitable solutions.
 Because AutoML Tables can select the best model for your needs without having to experiment.

 - Linear
 - Feedforward deep neural network
 - Gradient Boosted Decision Tree
 - AdaNet
 - Ensembles of varous model architecutures

In addition, AutoML Tables automatically performs feature engineering tasks

- Normalization
- Encoding and Embeddings for categorical features
- Timestamp columns management

Vertex AI is a new API that combines AutoML and AI Platform. You can use both AutoML training and custom training in the same environment.

<img src="https://s3.amazonaws.com/media.whizlabs.com/learn/ml30.png">

---

## When you want to increase the power of your training quickly. But your management wants to keep costs down.
https://cloud.google.com/tpu

- Use preemtible Could TPU
  - use preemptible Could TPU(70% cheaper) for your fault-tolerant machine learning workloads
- Use AI Platform with TPUs
  - use TPU in the AI Platform because TensorFlow APIs and custom templates can allow the managed environment to use TPUs and GPUs using scale tiers
- Use the Cloud TPU Profiler TensorBoard plugin
  - TensorBoard is a visual tool for ML experimentation for TensorFlow
  - use the Profiler with TensorBoard

All these solutions ideal for increasing power and speed at the right cost for your training.

---

## When manager asked you what the GCP techniques support the computer's ability to entertain almost human dialogues and if these techniques can be used individually.

- Speech to Text
  - Speech to Text converts voice to written text
- Cloud NLP
  - Cloud Natural Language API can understand text meanings such as syntax, feelings, content, entities and can create classifications
- Text to Speech
  - Text to Speech converts written text to voice
- Speech Synthesis Markup Language(SSML)
  - Speech Synthesis Markup Language is not service but a language used in Text-to-Speech requests.
  - SSML gives you the ability to indicate how you want to format the audit, pauses, how to read acronyms

Polly is AWS service.

---

## When Your model is complex, and you work with huge datasets with complex matrix computations. You have a big problem: your training jobs last for weeks. You are not going to deliver your project in time.
Cloud TPU is the best solution for this use case, which requires following requirements.

- Use TensorFlow
- Need training for weeks or months
- Have huge matrix computations
- Have deals with big datasets and effective batch size

---

## When you want to use TPUs instead of CPUs with Vertex AI. Since you are not using Docker images or custom containers.

Use scale-tier to BASIC_TPU is the best solution.
- Vertex AI lets you perform distributed training and serving with accelerations (GPUs and TPUs)
- You usually must specify the number and types of machines you need for your need for master and worker VMs. But you can also use scale-tiers that are predefined cluster specification.

Note 
- Set Master-machine-type
- Set Worker-machine-type
- Set parameterServerType

workerType, parameterSererType, evaluatorType, workerCount, parameterServerCount and evaluatorCount for jobs use custom concontainer and for TensorFlow jobs

---

## When you are looking for UI tools that can help you work and solve all issues faster. And you have to follow the entire lifecycle: model development, design, and training, testing, deplloyment, and retraining. Following solutions are suitable.
- TensorBoard
  - TensorBoard is aimed at model creation and experimentation.
    - Profiling
    - Monitoring metrics, weights, biases
    - Examine model graph
    - Working with embeddings
- Jupyter notebooks
  - Jupyter notebooks are tool to develop, experiment, and deploy. you may have the latest data science and machine learning frameworks with them.
- Kubeflow UI
  - Kubeflow UIs is for ML pipelines and includes visual tools for
    - Pipelines dashboards
    - Hyperparameter tuning
    - Artifact Store
    - Jupyter notebooks

- Note: there are not correct 
  - KFServing
    - KFServing is an open-source library for Kubernetes that enable serverless inferening. it works with TensorFlow, XGBoost, scikit-learn, PyTorch, and ONNX to solve issues linked to production model serving.
  - Vertex AI
    - Vertex AI is a suite of services that combines AutoML and AI Platform. you ncan use both AutoML and custom training in the same environment

---

## When you are looking for the most convenient way to import and manage this type of data. you need to deal with input data that is binary(images) and made by CSV files.

- tf.TFRecordReader 
  - `tf.TFRecordReader` is most suitable solution.
  - TFRecord format is efficient for storing a sequence of binary and not-binary records using Protocol buffers for serialization of structured data.

---

## When you want to save the model.
A checkpoint is an inermediate dump of a model's entire internal state(its weights, current learning rate, etc) so that the framework can resume the training from that very point.

- Pytorch
  - torch.save()
- Keras
  - callbacks.ModelCheckpoint (keras): intermediate dump
- TensorFlow
  - train.Checkpoints: intermediate dump

<img src="https://s3.amazonaws.com/media.whizlabs.com/learn/ml2-5.png">


## When you want to create an optimized input pipeline to increase the performance of training sessions, avoiding GPUs and TPUs as much as possible because they are expensive
- Caching
  - tf.data.Dataset.cache allows you to cache a dataset increasing performance
- Prefetching
  - tf.data.Dataset.Prefetch: while the execution of a training pass, the data for the next pass is read
- Parallelizing data
  - Parallelizing data transformation
    - tf.data API offers the map function for tf.data.Dataset.map transformation. This transformation can be parallelized across multiple cores with the num_parallel_calls option.
  - Sequential and parallel interleave
    - tf.data.Dataset.interleave offers the possibility of interleaving and allowing multiple datasets to execute in parallel


## When you face following kinds of issue
1. Transform data to hide personal information you don't need
2. Protect your work environment because certain combination of personal data are useful for your model and you need to keep them.

- You can soleve by following services
  - Cloud Data Loss Prevention
    - Cloud Data Loss Prevention is a service that can descover, conceal and mask personal information in data
  - VPC service-controls
    - VPC service-controls is a service that lets you build a security perimeter(セキュリティ境界) that is not accessible from outside. in this way data exfitration dangers are greatly mitigated. it is a network security service that helps protect data in a Virtual Private Cloud in multi tenant environment


## When you are struggling with your model(learning rate, hidden layers and nodes selection) for optimizing processing and letting converge in the fastest way. What is your problem in ML language ?
Hyperparameter Tuning Problem.
Hyperparameter tuning is made during the training job and used to be a manual and tedious process, made by running multiple trials with different values.

- ML Training Manages three main data categories
  - Training Data
    - Training data is called examples or records. It is the main input for model configuration and in supervised learning, presents labels, that are the correct answers based on past experience, input data is used to build the model but will not be part of the model
  - Parameters
    - Parameters are the variables to be found to solve the riddle
  . They are part of the final model and they make the difference among similar models of the same type.
  - Hyperparamter
    - Hyperparamters are configuration variables that influence the training process itself. Learning rate, hidden layers number, number of epochs, regularization, batch size are examples of hyperparameters
　

## When you don't have the labels for all the data, but you have very little time to complete the task for only a subset of it.

- Vertex Data Labeling 
  - Vertex Data Labeling will help you prepare correct labels following your directions.

You have to setup a data labeling job
1. The dataset 
2. A list, vocabulary of the possible labels
3. An instructions document for the professional people

Note:
Mechanical Turk is AWS service
Gitlab is a DevOps lifecycle tool
Tag Manager is in the Google Analytics Ecosystem

## When you have different teams in different projects used to deal with the same feature based on the same data differently. The problem arose when models drifted unexpectedly over time.

The bast strategy is to use the Vertex AI Feature Store.
Vertex Store is a service to organize and store ML features through a central store. This allows you to share and optipize ML features importtant for the specific environment and to reduce them at any time.

- Typical Procedure for using Feature Store
  - Check out the Vertex Feature Store for Features that you can reuse or use as a template
  - If you don't find a Feature that fits perfectly, create or modify on exisiting one.
  - Update or Insert feature of your work in the Vertex Feature Store
  - Use them in training work
  - Set up a periodic job to generate feature vocabulary data and optionally updates the Vertex Feature Store

![pic](https://s3.amazonaws.com/media.whizlabs.com/learn/2-13.png)

Note: Could Storage is not enough for identifing different features. more importantly it will not avoid feature definition overlapping.

---

## When you would like engineer-to-engineer assistance from both Google Cloud and Google's TensorFlow teams. Which of the following services can be used ?

### TensorFlow Enterprise
The TensorFlow Enterprise is a distribution of the open-source platform for ML, linked to specific versions of TensorFlow, trained for enterprise customers.

It is free but only for big enterprises with a lot of serices in GCP. It is prepackaged and optimized for usage with containers and VMs.

It works in Google Cloud, from VM images to managed services like GKE and Vertex AI.

- The TensorFlow Enterprise Library is integrated into the following products
  - Deep Learning VM Images
  - Deep Learning Containers
  - Notebooks
  - AI Platform/Vertex AITraining

It is ready for automatic provisioning and scaling with any kind of processor. it has premimum level of support from Google.

Kubeflow & TFX are open-source libraries with standard support from the community.

## When you have to create a model for recognizing photographic images related to collaborators and consultants. You have do it quickliy, it has be an R-CNN model. you don't want to start from scrach.

TensorFlow-Hub is ready to use repository of trained ML models. It is available for reusing advanced trained model with minimal code. The ML models are optimized for GCP.

---

## Which GCP products are most sutable for project that a small batch of data will be sent that will be collected and processed in order to provide customers with the management of their vehicle health and push notifications in case of important messages.

- Pub/Sub
  - to catch an event and push data to DataFlow process
  - Pub/Sub is for technical data messages.
- DataFlow
  - to collect and process data
  - DataFlow is for data management both in streaming and batch
    - Serialize input data
    - Preprocess and transform data
    - Call the inference function
    - Get the results and postprocess them
- Firebase Messaging
  - to send a message(Push notifications)

Note: Dataproc is the managed Apache Hadoop environment for big data analysis usually for batch processing.

## You need to approximately collect and transform data and then create and tune your models. These procedures will be inserted in an MLOps flow and therefore will have to be automated and be simple as possible. What are the methodologies / services recommended by Google.

### DataFlow
DataFlow is an optimal solution for compute-intensive preprocessing operations because it is fully managed autoscaling service for batch and streaming data processing

### BigQuery
BigQuery is a strategic tool for GCP. BigData at scale, machine learning, preprocessing with plain SQL are all important factors.

### TensorFlow
TensorFlow has many tools for data preprocessing and transformation operations. Main techniques are aimed to feature engineering(cross_column, embedding_column, bucketize) and data transformation(tf.Transformation library)

![pic](https://s3.amazonaws.com/media.whizlabs.com/learn/2-23.png)

Note: Dataprep is a tool for visual data cleaning and preparation. Cloud Fusion is for ETL with a GUI.

## When you want to get help from GCP for hyperparameter tuning, what are the parameters that you must indicate ?
With Vertex AI, It is possible to create a hyperparameter tuning job for LINEAR_REGRESSION and DNN.
You can choose many parameters. But in the case of DNN, you have to use a hyperparameter named learning_rate.

The ConditionalParameterSpec object lets you add hyperparameters to a trial when the value of its parent hyperparameter matches a condition that you specify(added automatically) and the number of hidden layers, that is num_hidden_layers.

- paratemeterServerType
- scale Tier

are paramters for infrastructure set up for a training job.

## When you to predict the demand of its customers both to increase business and improve logistics processes. What managed and fast-to-use GCP products can be used for these types of models?

- AutoML ML
- BigQuery ML

We have in GCP the possibility to use a large number of models and platforms.
But the fastest and most immediate modes are with AutoML and BigQuery ML

Both support quick creation and fine-tuning of templates.

Note: KubeFlow and TFX are open-source libraries that work with TensorFlow. So, they are not managed and so simple.

Moreover, they can work in an environment outside GCP that is a big advantage, but it is not in our requirements.

## When you want to get the most from ML services and the least costs, What are the best practices recommended by Google?

- Notebooks as an ephemeral Instance
  - Notebooks are used for a limited time, but they reserve VM and other resources. So you have to treat them as ephemeral instances, no t as long-living ones
- Automatic shutdown routine
  - an automatic shutdown routine can save your costs
- Preemptible VMs
  - Preemptible VMs are far cheaper than normal instances and are OK for long-running(batch) large experiments.
  - GCP側の都合で停止される可能性がある
  - 最長24時間で必ず停止される
- GPU metrics reporting script
  - this is important since GPU is expensive

## When you have to prepare a demo. You are certain that they will ask you about the understanding of the classification and regression mechanism. You'd like to show them an interactive demo with some interference.

What-If tool will help you.

What-If Tool is an open-source tool that lets you visually understand classification and regression ML models.

It lets you see data points distributions with different shapes and colors and interactively try new inferences.

Moreover, it shows which features affect your model the most together with many other characteristics. (All without code)

- Note: 
  - Tensorboard provides visualization and tooling needed for experiments, not for explaining inference.
  - Tableau and Looker are graphical tools for data reporting
  - LIT(the Language Interpretability Tool) is for NLP models.
    - Language Interpretability Tool is a visual, interactive model-understanding tool for ML modeels, focusing on NLP use-cases
    - It is similar to WIT(What-If tool)

## When you need to demonstrate DNN models.
- Integrated Gradient
  - Integrated Gradient is an explainability technique for deep neural networks that gives information about the model's prediction. Integrated Gradient works highlighting the feature importance.
  - It computes the gradient of the model's prediction output regarding its input features without modification to original model.
  - You can see that it tunes the inputs and computes attributions so that it can compute the feature importances for the input image
  - You can use tf.GradientTape to compute the feature importances for the input image

<img src="https://s3.amazonaws.com/media.whizlabs.com/learn/2-3.png">

## When you have a view with many columns, and you want to make some simplifications for your work and avoid overfitting.
- EXCEPT
  - EXCEPT gives all rows or fields on the left side except the one coming from the right side of the query.

```sql
SELECT * EXCEPT(mylabel) myvalue AS label
-- 
SELECT * except(species)
FROM `bigquery-public-data.ml_datasets.iris`;
```

- ROLLUP
  - it is a group function for subtotals
- UNNEST
  - unnest gives the elements of a structured file
- LAG
  - LAG returns the field value on a preceding row

## Which types of transformations are you not allowed in CSV file
- Allowed
  - Categorical
  - Text
  - Timestamp
  - Number

- Not Allowed
  - Array

With complex data like Arrays and Structs, transformations are available only by using BigQuery, which support them natively.

All other kinds of data are also supported for CSV files, as stated in the referred documentation.


## When you have to avoid multicollinearity and optimize categories. So you need to group some features together and create macro categories. In particular, you have to join country and language in one variable and divide data between 5 income classes. Which one of the following options can you use ?

- FEATURE_CROSS
  - A feature cross is a new feature that joins two or more input features together. (The term cross comes from cross product.) Usually, numeric new features are created by multiplying two or more than other features.
- QUANTILE_BUCKETIZE
  - QuUANTILE_BUCKETIZE groups a continuous numerical feature into categories with the bucket name as the value based on quantiles.

Note:
  - ARRAY_CONCAT 
    - ARRAY_CONCAT joins one or more arrays (number or strings) into a single array.
  - ST_AREA
    - ST_AREA returns the number of square meters covered by a GEOGRAHY area


## You team must create and modify code to directly access BigQuery data for building models in different environment. What are the tools you can use ?
- tf.data.dataset
  - tf.data.dataset reader for BigQuery is the way to connect directly to BigQuery from TensorFlow or Keras

- BigQuery I/O Connector
  - BigQuery I/O Connector is the way to connect directly to BigQuery from Dataflow

- BigQuery Python client library
  - BigQuery Python client library can be used in any other framework

Note:
  - BigQuery Omni
    - BigQuery Omni is a multi-cloud analytics solution
    - You can access from BigQuery data across Google Cloud, AWS, and Azure.
    - BigQuery Omni lets you run BigQuery analytics on data stored in AWS S3 or Azure blob storage

## Which other(Multiclass Logistic Regression model) types of models can you implement with AutoML ?
AutoML on Vertex AI can let you build a code-free model. 
You have to provide training data. 

The types of models that AutoML on Vertex AI can build are created with image data, tabular data, text data and video data.
- Image Data
- Text Data
- Video Data

Note: 
  - Cluster data
    - Cluster Data is related to unsupervised learning, which is not supported by AutoML.

## You have to decide the strategy for implementing an online forecasting model in production. You are concerned that the final system is not efficient and scalable enough. You are looking for the simplest and most managed GCP solution.

- Vertex AI online prediction
  - Vetex AI prediction service is fully managed and automatically scales machine learning models in the cloud
  - The service supports both online prediction and batch prediction
<img src="https://s3.amazonaws.com/media.whizlabs.com/learn/2-37.png">

Note:
  - GKE e TensorFlow and VMs and Autoscaling Groups with Application LB
    - GKE and VMs are not managed service for online prediction.

  - not Kubeflow(ETL and deploy feature)
    - Because Kubeflow is not managed service.
    - It is used in AI platforms and lets you deploy ML systems in various environment

## When you want to maintain both the old and the new version at the same time. The new version should only serve a smaill portion of the traffic.

- Deploy on the same endpont
- Update the Traffic split percentage]
  - Deploy your model to an existing endpoint
  - Update the traffic split percentage in such a way that all of the percentages add up to 100%

Note:
  - Save the model in a Docker container image
    - you don't need to create a docker conatainer image with AutoML
  - Canary Deployment with Cloud Build is a procedure used in CI/CD pipelines. There is no need in such managed environment.

## Which types of storage should you avoid in the managed environment of GCP ML, such as Vertex AI
Google advises avoiding data storage for ML in block storage like persistent disk or NAS like FileStore. They are more difficult to manage than Cloud Storage or BigQuery.
- FileStore
- Block Storage

## You want to leerage Explainable AI to understand which are the most essential features and how they influence the model. For what kind of model may you use Vertex Enplainable AI ?

- AutoML tables
- Image Classification
- DNN(Deep Neural Network)

Deep Learning is known to give little comprehension about how a model works in detail.

Vertex Explainable AI helps to detect it, both for classification  and regression task. So these functions are useful for testing, tuning, finding biases and thus improving the process.

You can get explanations from Vertex Explainable AI both for online and batch inference but only regarding these ML models
- Structured data models (AutoML, classification and regression)
- Custom-Trained models with tabular data and images

In the Evaluate section, you can find these insights in Google Cloud Console(Feature importance graph).
<img src="https://s3.amazonaws.com/media.whizlabs.com/learn/20.png">

Note:
  - Decision Tree Models
    - Decision Tree models are explainable without any sophisticated tool for enlightenment

## When you already use caching and prefetching. so now you want to use GPUs, but in a single machine, for cost reduction and experimentations.
tf.distribute.Strategy is an API for training distribution among different processors and machines

- tf.distribute.MirroredStrategy
  - MirroredStrategy lets you use multiple GPUs in a single VM, with a replica for each CPU.

<img scr="https://s3.amazonaws.com/media.whizlabs.com/learn/2-41.png">

Note:
  - tf.distribute.TPUStrategy
    - TPUStrategy lets you use TPUs, not GPUs
  - tf.distribute.MultiWorkerMirroredStrategy
    - MultiWorkerMirroredStrategy is for multiple machines
  - tf.distribute.OneDeviceStrategy
    - OneDeviceStrategy is the default strategy for a single device, so a single virtual CPU

## When you work with tensorflow in Vertex AI. You deploy a new model in the test env and detected some problems. And you want to get logs. What kind of logs do you need and how do you get them? 

In Vertex AI, you may enable or avoid logs for prediction. When you want to chnage, you must undeploy and redeploy. There two types of logs.

- Container Logging
  - Container Logging, which logs data from the containers hosting your model; so these logs are essenial for problem solving and debugging
- Access Logging
  - Access logging, which logs accesses and latency informationd

## When you avoid deploying the model in eager mode.
When you develp and test a model, the eager mode is really useful because it lets you execute operations one by one and facilitate debugging.

But when in production, it is better to use graphs, which are data structures with Tensors and integrated computations Python independent. In this way, they can be deployed on different devices(like mobiles) and are optimizable.

To do that, you have to use tf.function decoration function for new tf.Graph creation.

- Use graphs
- Use tf.function decoration function
- Create a new tf.Graph

Using graphs instead of eager execution is more complex than that.

## Checking and Updating models create additional difficulties. You are undecided whether to use Vertex Pipeline and Kubeflow Pipelines. You wonder if starting from Kubeflow, you can later switch to a more automated and managed system like Vertex AI.
Vertex AI Pipelines is a managed service in GCP.
Kubeflow Pipelines is an open-source tool based on Kubernetes and Tensorflow for any environment.

Vertex AI support code written with Kubeflow Pipelines SDK v2 domain-specific language(DSL)

- You may use Kubeflow pipelines written with DSL in Vertex AI
- Kubeflow pipelines may work in any environment
- Kubeflow pipelines may use Kubernetes persistent volume claims
- Vertex Pipelines can use Cloud Storage FUSE

Like any workflow in Kubernetes, access to persistent data is performed with Volumnes and Volume Claims.
Vertex Pipelines can use Cloud Storage FUSE. so Vertex AI can leverage Cloud Storage buckets like file systems on Linux or macOS

<img src="https://s3.amazonaws.com/media.whizlabs.com/learn/2-45.png">

## When you want to manage CSV format data with Vertex AI
Vertex AI manages CSV files automatically.
But you need to have headers only with alphanumric characters and underscores with commas as delimiters.
You can import multiple files, each one max 10GB

- You have to setup an header and column names may have only alphanumeric character and underscore
- Delimiter must be a comma

## When you want to check the capabilities of this managed suite of Vertex AI.
Vertex AI covers all the activities and functions listed
- Training Pipelines(so MLOps)
- Data Management(Datasets)
- Custom Model and AutoML models management
  - custom tooling and libraries deployment and monitoring

<img src="https://s3.amazonaws.com/media.whizlabs.com/learn/Q-7.png">

## Which of methods does Vertex AI leverage for feature attributions ?
Deep Learning is known to give little comprehension about how a model works in detail.
Vertex Explainable AI helps to detect it, both for classification and regression tasks.

So, these functions are useful for testing, tuning, finding biases and thus improving the process.

### Sampled Shapley
Sampled Shapley uses scores for each feature and their permutations
### Integrated Gradients
Integrated Gradients computes the gradient of the features at different points, integrates them and computes the relative weights
### XRAI
XRAI is an optimization of the integrated gradients method

Note:
  - Maximum Likelihood
    - Maximum Likelihood is a probabilistic method for determining the parameters of a statistical distribution

## When you need to let others use your Vertex AI dataset in Cloud Storage for a different organization.
You can export a Dataset. When you do that, no additional copies of data are generated.
The result is only JSON files with all the useful information, including the Cloud Storage files URIs.

but you have to grant access to these Cloud Storage files with a Service account or a signed URL, if to be used outside GCP.

- Exporting metadata and annotations in a JSON file
- Give access (Service account or signed URL) to the Cloud Storage file

<img src="https://s3.amazonaws.com/media.whizlabs.com/learn/2-52.png">

## When you have various fields that have no value or report NaN. What kind of procedure that modifies them at the time of acquisition?
The most frequent methodologies have been listed.

In the case of numerical values, substituting the mean generally does not distort the model(it depends on the underlying statistical distribution)
In the case of categories, the most common method is to replace them with the more frequent values.

There are often multiple categories in minimized, but the additional values of the current example are used.
- Compute mean/median for numeric measures 
- Replace categories with the most frequent one
- Use another ML model for missing values guess

## When you want to find a simple method to determine affinities between different products and categories to give sellers and applications a wider range of suitable offerings for customers. Which of the following will give good results even without a great amount of data.
- Cosine Similarity
  - In a recommendation system(like with the Netflix movies), it is important to discover similarities between products so that you may recommend a movie to another user because the different users like similar objects.
  - Cosine Similarity is a method to do so.
    - You take two products and their characteristics(all transformed in numbers) so you have two vector
    - You may compute differences between vectors in the euclidean space
      - Geometrically that means that they have different lengths and different angles.

<img src="https://s3.amazonaws.com/media.whizlabs.com/learn/2-51.3.png">

