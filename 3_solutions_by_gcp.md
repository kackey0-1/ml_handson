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





