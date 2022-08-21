# Create a streaming pipeline using Python
Dataflow is a distribution of Apache Beam

## Create a Cloud Storage bucket

```shell
export BUCKET_NAME=qwiklabs-gcp-04-ee8e5648d59c
gsutil mb -l us-central1 gs://$BUCKET_NAME/
```

## Install pip and the Cloud Dataflow SDK

1. The Cloud Dataflow SDK for Python requires Python version 3.7.
  ```shell
  docker run -it -e DEVSHELL_PROJECT_ID=$DEVSHELL_PROJECT_ID python:3.7 /bin/bash
  ```
2. After the container is running, install the latest version of the Apache Beam for Python by running the following command from a virtual environment:
  ```shell
  pip install apache-beam[gcp]
  ```
3. Run the wordcount.py example locally by running the following command:
  ```shell
  python -m apache_beam.examples.wordcount --output OUTPUT_FILE
  ```

## Run an Example Pipeline Remotely
```shell
BUCKET=gs://qwiklabs-gcp-04-ee8e5648d59c
python -m apache_beam.examples.wordcount --project $DEVSHELL_PROJECT_ID \
  --runner DataflowRunner \
  --staging_location $BUCKET/staging \
  --temp_location $BUCKET/temp \
  --output $BUCKET/results/output \
  --region us-central1
```

