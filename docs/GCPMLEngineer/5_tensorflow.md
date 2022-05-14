# TensorFlow
https://www.tensorflow.org/tfx/guide?hl=en

## TensorFlow I/O
TensorFlow I/O is a set of useful file formats, Dataset, streaming, and file system types management not available in TensorFlow's built-in support, like Parquet.

Apache Parquet is an open-source column-oriented data storage format both in the Apache Hadoop environment but supported in many tools and used for data analysis.

TensorFlow I/O is an extension package to Tensorflow, which encompasses io support for a collection of file systems and file formats that are not available in TensorFlow's built-in support. Integrations with many systems and cloud vendors include (but not limited to):
- Prometheus
- Apache Kafka
- Apache Ignite
- Google Cloud BigQuery
- Google Cloud PubSub
- AWS Kinesis
- Microsoft Azure Storage
- Alibaba Cloud OSS etc...

## TensorBoard
TensorFlow provides the visualization and tooling needed for machine learning experimentation.
- Tracking and visualizing metrics such as loss and accuracy
- Visualizing the model graph(ops and layers)
- Viewing histograms of weights, biases, or other tensors as they change over time
- Projecting embeddings to lower dimensional space
- Displaying images, text, and audio data
- Profiting TensorFlow programs
- ...etc

## TenforFlow Probability
TensorFlow Probability is a Python library for statistical analysis and probability, which can be processed on TPU and GPU.
- Main features of TensorFlow Probability
  - Probability distributions and differetiable and injective(one to one) functions
  - Tools for deep probabilistic models building
  - Inference and Simulation methods support: Markov chain, Monte Carlo
  - Optimizers such as Nelder-Mead, BFGS, and SGLD

# TFX Libraries (TensorFlow Extended Libraries)
TensorFlow Extended(TFX) is a platform that allows you to create scalable production ML pipelines for TensorFlow projects.

## TensorFlow Data Validation(TFDV)
https://github.com/tensorflow/data-validation
- Training-Serving Skew Detection
  - Distribution skew between training and serving data
- Drift Detection
  - L-infinity distance for categorical features 
  - Approximate Jensen-Shannon divergence for numeric features

## TensorFlow Transform(TFT)
https://github.com/tensorflow/transform
## TensorFlow
https://github.com/tensorflow/tensorflow
## TensorFlow Model Analysis(TFMA)
https://github.com/tensorflow/model-analysis
## TensorFlow Metadata(TFMD)
https://github.com/tensorflow/metadata
## ML Metadata(MLMD)
https://github.com/google/ml-metadata

# TFX Supporting Technologies
## [Required] Apache Beam
https://github.com/apache/beam

TFX uses Apache Beam to implement data-parallel pipelines. The pipeline is then executed by one of Beam's supported distributed processing back-ends, which include Apache Flink, Apache Spark, Google Could Dataflow, and others.
## [Optional] Apache Airflow
https://github.com/apache/airflow

## [Optional] Kubeflow
https://github.com/kubeflow/kubeflow

<img src="https://www.tensorflow.org/tfx/guide/images/libraries_components.png">

# TFX Deployment
## TensorFlow Serving(TFS)
https://github.com/tensorflow/serving

- TensorFlow Serving is a flexible, high-performance serving system for machine learning models, designed for production environments.
- TensorFlow Serving makes it easy to deploy new algorithms and experiments, while keeping the same server architecture and APIs.
- TensorFlow Serving provides out-of-box integration with TensorFlow models, but can be easily extended to serve other types of models and data.
## TensorFlow Lite
## TensorFlow JS

