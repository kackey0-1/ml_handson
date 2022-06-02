# Dataproc

Cloud Dataproc is a fast, easy-to-use, fully-managed cloud service for running Apache Spark and Apache Hadoop clusters
in a simpler, more cost-efficient way

## Create Dataproc Cluster

1. Set the Region

  ```shell
  gcloud config set dataproc/region us-central1
  ```

2. Create a cluster

  ```shell
  gcloud dataproc clusters create example-cluster --worker-boot-disk-size 500
  ```

## Submit a Job

- That you want to run a spark job on the example-cluster cluster
- The class containing the main method for the job's pi-calculating application
- The location of the jar file containing your job's code
- The parameters you want to pass to the job—in this case, the number of tasks, which is 1000

```shell
gcloud dataproc jobs submit spark --cluster example-cluster \
  --class org.apache.spark.examples.SparkPi \
  --jars file:///usr/lib/spark/examples/jars/spark-examples.jar -- 1000
```

## Update a cluster

```shell
# scale out
gcloud dataproc clusters update example-cluster --num-workers 4
# scale in
gcloud dataproc clusters update example-cluster --num-workers 2
```

