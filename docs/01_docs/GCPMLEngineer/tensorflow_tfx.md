# TensorFlow Extended(TFX)
Google's production Machine Learning platform based on TensorFlow ecosystem.

![pic](https://drive.google.com/uc?id=1xmExKYvjEQRCQntL-RDWVgnpn4at4x1v)
![pic](https://drive.google.com/uc?id=13U1X5jcQDPSX2wMCSWd1nH9kamPal0Qb)

## TFX Components
TFX Component implements a machine learning task.

### Component specification
A configuration protobuf defines how components communicate with each other via input and output artifact channels and runtime parameters.

### Component driver
A driver candidates job execution.

### Component executor 
Code to perform ML workflow step such as data preprocessing or TensorFlow model training.

### Component publisher
Updates ML metadata store

### Component interface
packages component specification and executor for use in pipeline

![pic](https://drive.google.com/uc?id=1CuTtMn6OWf8iEr_kZl5M68rhnizN-9iR)
![pic](https://drive.google.com/uc?id=1yRlwyPWL6gg-ZVhAXd-Li02fAOWSePCc)
![pic](https://drive.google.com/uc?id=1PbwnjtrbcuQlCpaUMm6cFmeGheA9vRfI)

## TFX Standard data components

### Component: ExampleGen
- Configureable and reproducible data partitioning and shuffling
- Support for external CSV, Avro, Parquet, BigQuery, and TFRecord integration
- Apache Beam supported for scalable data ingestion
- Customizable to new input data formats and ingestion methods

![pic](https://drive.google.com/uc?id=1wV2y13aWqkrjaEXGEuknqtcL9hKTodGR)

### Component: StatisticsGen
- TensorFlow Data Validation(TFDV) library for calculationg feature statistics
- Scalable full-pass dataset feature statistics processing with Apache Beam

![pic](https://drive.google.com/uc?id=1YYg3Qq4BIXPdusutQdiNNYfkg8KgB9Tg)

### Component: SchemaGen
- TensorFlow Data Validation(TFDV) creates common data description for pipeline components
- A Schema enables continuous ata monitoring and validation during pipeline training

![pic](https://drive.google.com/uc?id=1_3dL6iL_9XD9fPYhXn4iA0zXcSDe2skb)

### Component: Example Validator
- Data monitoring for detection of anomalies, train-serving skew and data drift

![pic](https://drive.google.com/uc?id=1YPeS4BoyZu_3t-gYAGd0FPQ82k_QmK3r)

### Component: Transform
- Generates SavedModel for consistent training and serving feature engineering
- Backed by Apache Beam for scalable distributed data processing to large datasets

![pic](https://drive.google.com/uc?id=1zg7JRzVVMXPpZOWQ4AAJvUWZEhiiLoDR)
![pic](https://drive.google.com/uc?id=1y4IH3ODI5mzUqHwcKp8qm2rL4GY9wd2D)

## TFX standard model components
### Component: Trainier
- Produces standardized TensorFlow SavedModel model artifact for sharing and easier deployment
- Configurable with Generic Trainer for any TensorFlow model API such Estimator, tf.Keras, and TFLite

![pic](https://drive.google.com/uc?id=12gax_R1VJcrIv-UQFgQ6P0avTEFCTz34)
![pic](https://drive.google.com/uc?id=1TWnKX8LQ_Ci8kzDdv-jG_FS2oDAiPaWh)

### Component: Tuner
- Supports Keras Tuner library for hyperparameter tuning and integration with TensorFlow Trainer
- Can use Google Cloud AI Platform Optimizer for distributed tuning

![pic](https://drive.google.com/uc?id=1EVSK01HjrUV7DcYztjEiwiugOQiBXsE-)

### Component: Evaluator
- Uses TensorFlow Model Analysis(TFMA) and Apache Beam for scalable model evaluation across data splits and slices
- Validate model performance "good enough" to be pushed to production

![pic](https://drive.google.com/uc?id=1yOwCyuO1wwG2lh0MR2QvTFFj509pZI05)

### Component: InfraValidator
- Validate model in model serving environment before pushing to production
- Configurable to mirror different model serving environments such as Kubernetes and TF Serving

![pic](https://drive.google.com/uc?id=1ENFRwFPyciXOUhw6nKg3VZu1Y-Jpp1tp)

### Component: Pusher
- Validation checks on model performance and serving ability before pushing to production
- Reusable model export code that is configurable for different push destinations
  - Filesystem (TensorFlow Lite, TensorFlow JS)
  - Model Server (TensorFlow Serving)

![pic](https://drive.google.com/uc?id=1SvL5eq1r2Jy4DbU4HrpQROWbIBJZT5Ym)

### Component: BulkInfere
- Task and data-driven inference directly in your TFX pipeline

![pic](https://drive.google.com/uc?id=1MZn9EKK3bP-lfZ6dOQXnKNx-GFWxexIL)

## TFX pipeline nodes
Pipeline nodes are special purpose classes for performing advanced metadata operations, such as 
- importing external artifacts into ML metadata
- performing queries of current ML metadata based on artifacts properties and their history. 

### ImporterNode
- ImporterNode imports an external data object into ML Metadata.

![pic](https://drive.google.com/uc?id=1nxpuMPLosyIVKAHY9ywdrxrsEG0NJ8uk)

### ResolverNode
- ResoleverNode performs metadata queries.

![pic](https://drive.google.com/uc?id=1hB28Foy1L8Irt6g9Ti8z0bxxG_FDcdQW)

## TFX Libraries
### TFDV(TensorFlow Data Validation)
- TFDV for analyzing and validating data
- There is integration with a viewer for data distributions and statistics

### TensorFlow Transform(TFT)
- TFT library is for preprocessing data and feature engineering with TensorFlow
- Analyzers: max, min, mean, sum, sum, var, covariance, quantiles, size, vocabulary, pca
- Mappers: bucketize, apply_buckets, hash_string, ngram, scale_0+1, scale_z_score, Scale_max_min, tfidf, compute_and_apply_vocabulary

### TensorFlow
TensorFlow for model trainig and tuning.

### TensorBoard
TensorBoard is visualization and tooling for ML experimentation integrated with TFX.

![pic](https://drive.google.com/uc?id=1Y159O4slG_TpKpy3-0z-GAlr6fzi5hJn)

### TensorFlow Model Analysis(TFMA)
TFMA is library for model evaluation


TensorBoard visualizes streaming whole model metrics that are computed from checkpoints during training. 

![pic](https://drive.google.com/uc?id=1hWWqYk3dCDZuoligFRg2AJnzz7iwIJhJ)

On the other hand, TFMA computes and visualizes metrics using an exported eval saved model format in batch to give you a much deeper granularity on your model's performance across slices.

![pic](https://drive.google.com/uc?id=1qinZRrm8jF_wYwrtFxNWPZgGNZG5t8y_)



