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

## When you want to automate entire process of train to production start-up from static deep
Vertex AI Pipelines can run pipelines built by using TFX(=TensorFlow Extended)
<img src="https://s3.amazonaws.com/media.whizlabs.com/learn/ml19.png" />

## When you want to automate the re-development and distribution process every time it recieves a new file
1. Could Storage to recieve new files
2. Trigger process
    - Could Functions
    - Pub/Sub
3. Other services like Dataflow

<img src="https://s3.amazonaws.com/media.whizlabs.com/learn/ml21.png">

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

## When you train your DNN with TensorFlow, your input data does not fit into RAM memory. Which can you do in the simplest way ?

tf.data.Dataset allows you to manage a set of complex elements made up of several inner components.
It is designed to create efficient input pipelines and to iterate over the data for their processing.
These iterations happen in streaming. So they work even if the input matrix is very large and doesn't fit in memory.

- Use a queue with tf.train.shuffle_batch
  - it is far more complex, even if it is feasible.

- pandas.DataFrame
- NumPy
  - these  are work in real memory. so they don't solve the problem

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

## When Your model is complex, and you work with huge datasets with complex matrix computations. You have a big problem: your training jobs last for weeks. You are not going to deliver your project in time.
Cloud TPU is the best solution for this use case, which requires following requirements.

- Use TensorFlow
- Need training for weeks or months
- Have huge matrix computations
- Have deals with big datasets and effective batch size

## When you want to use TPUs instead of CPUs with Vertex AI. Since you are not using Docker images or custom containers.

Use scale-tier to BASIC_TPU is the best solution.
- Vertex AI lets you perform distributed training and serving with accelerations (GPUs and TPUs)
- You usually must specify the number and types of machines you need for your need for master and worker VMs. But you can also use scale-tiers that are predefined cluster specification.

Note 
- Set Master-machine-type
- Set Worker-machine-type
- Set parameterServerType

workerType, parameterSererType, evaluatorType, workerCount, parameterServerCount and evaluatorCount for jobs use custom concontainer and for TensorFlow jobs