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





