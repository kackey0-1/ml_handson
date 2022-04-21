# TensorFlow
https://www.tensorflow.org/tfx/guide?hl=en

# TFX Libraries (TensorFlow Extended Libraries)
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


