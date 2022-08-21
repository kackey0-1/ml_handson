# Create a streaming pipeline using one of [Google's Cloud Dataflow templates](https://cloud.google.com/dataflow/docs/templates/provided-templates)

## Create a Cloud BigQuery Dataset and Table Using Cloud Shell

1. Create `taxirides` BigQuery dataset
   ```shell
   bq mk taxirides
   ```
2. Create `realtime` BigQuery table in `taxirides` dataset
   ```shell
   bq mk \
     --time_partitioning_field timestamp \
     --schema ride_id:string,point_idx:integer,latitude:float,longitude:float,\
     timestamp:timestamp,meter_reading:float,meter_increment:float,ride_status:string,\
     passenger_count:integer -t taxirides.realtime
   ```

## Create a storage bucket

```shell
export BUCKET_NAME=<your-unique-name>
gsutil mb gs://$BUCKET_NAME/
```

## Run the Pipeline

1. From the Navigation menu, find the Analytics section and click on Dataflow. 
2. Click on + Create job from template at the top of the screen. 
3. Enter iotflow as Job name for your Cloud Dataflow job. 
4. Under Dataflow Template, select the Pub/Sub Topic to BigQuery template. 
5. Under Input Pub/Sub topic, enter:
  ```shell
  projects/pubsub-public-data/topics/taxirides-realtime
  ```
6. Under BigQuery output table, enter the name of the table that was created:
  ```shell
  <myprojectid>:taxirides.realtime
  ```
7. Add your bucket as Temporary Location:
  ```shell
  gs://Your_Bucket_Name/temp
  ```



