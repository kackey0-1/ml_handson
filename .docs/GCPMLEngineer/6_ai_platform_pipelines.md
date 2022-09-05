# AI Platform Pipeline
![picture](https://drive.google.com/uc?id=1ddiY-AzzK_Mf7i7uH1V_B8tjcELbokg3)

## AI Platform Pipelines implementation strategy
- AI Platform pipelines will enable 
  - Workflow orchestration
  - Rapid, reliable, repeatable experimentation
  - Share, re-use, and compose

- Supported SDK
  - Kubeflow pipelines
    - Lower-level ML framework-agnostic implementation
    - Enables direct control of Kubernetes resource control
    - Simple sharing of containerized components
    - Use it for fully custom pipelines
  - TensorFlow Extended(TFX)
    - Higher-level abstraction
    - Prescriptive but customizable components with pre-defined ML types
    - Bring Google best practices for robust/scalable ML workloads
    - Use it for E2E TF-Based pipeline with customizable data pre-processing and training code

![pic](https://drive.google.com/uc?id=1oO-oXhTjmez0PHGK-meMizt7EaP33N-z)
![pic](https://drive.google.com/uc?id=1mfa51YGGNT0BBl_-6gJE4K2-A-toP9Bt)
![pic](https://drive.google.com/uc?id=1z1bgeNKiHRzOlUJcDmmOXYxYsGWhiEQ5)
![pic](https://drive.google.com/uc?id=15hJA09YwWvHyytE_js0jKqCT_D4SbLHx)

## AI Platform Pipelines Ecosystem
AI problems today
- Talent: Lack of expertise in ML
- Ecosystem: Difficult to find and leverage exsisting solutions
- Flexibility: Brittle, opinionated infrastructure that breaks between cloud and on-premises


## Training, Tuning and Serving your model on AI Platform
### Building and operationalizing the model
1. Implement a tunable training application(train.py)
2. Containerize your traininng application(Dockerfile)
3. Configure and start an AI Platform job(config.yaml)

### MLOps building blocks on Google Cloud
![pic](https://drive.google.com/uc?id=1tTc_QBZME5gJ9TX2Us05vvj0XGqMv9Nf)
![pic](https://drive.google.com/uc?id=1eU50VeDGEiISetWMiS_Z6lK04FGSg3wv)

We need to automate all the process to achieve MLOps
![pic](https://drive.google.com/uc?id=1rj0BzhY3lvsd2BhQ3Yfxp8MV9a_Mt0WN)

### Create a reproducible dataset
- Split the dataset and expeiment with models
  - Experimentation requires repeatability
  - Solution: Use hashing and modulo operators to split a dataset into training/validation
    - Not correlated to label
    - Granular enough for your desired module split

### Implement a tunable model
ML models are functions with parameters ad hpyerparameters
- Parameters
  - Changed during model training
- Hyperparamters
  - Set before training
    - learning rate
    - classifier_alpha
    - classifier_max_iter

![pic](https://drive.google.com/uc?id=131mkcnDSYwGq48X6qhtlK_-cLjfs1H2u)
![pic](https://drive.google.com/uc?id=1zzzgnztR_ueUtME-lBkq6vk_z9nv6wgv)

How to use AI Platform for hyperparameter tuning
1. Make the hyperparameter a command-line argument
  ![pic](https://drive.google.com/uc?id=1Sq96pciKl0HvoPcokTPXk54ywufAaaSv)
2. Set up cloudml-hypertune to record training metrics
  ![pic](https://drive.google.com/uc?id=1kOdx1dIZUTWxpJSoJtHKqWHpjtDgULQL)
3. Export the final trained model
  ![pic](https://drive.google.com/uc?id=1uXBd3ES5wEXbPVYGRGIrAVwh2xF0SBjO)
4. Supply hyperparameters to the training job
  ![pic](https://drive.google.com/uc?id=1VfWdvhxBKtoRM8YQPMnTDnrZLVZXErOe)

### Build and Push a training container
1. Create a Dockerfile for the training Docker container 
![pic](https://drive.google.com/uc?id=1NbgFBU_ZH5zJd8-WtewI6R2BBnBhdUeK)

### Train and Tune the model
1. Start the hyper tuning job on AI Platform by CLI
  ```bash
  gcloud ai-platform jobs submit training $JOB_NAME \
    --region=$REGION \
    --job-dir=$JOB_DIR \
    --master-image-uri=$IMAGE_URI \
    --scale-tier=$SCALE_TIER \
    --config $TRAINING_APP_FOLDER/hptuning_config.yaml \
    -- \
    --traning_datset_path=$TRAINING_FILE_PATH \
    --validation_dataset_path=$VALIDATION_FILE_PATH \
    --hptune
  ```
2. Query AI Platform Training for the best hyperparameters
  ```python
  from googleapiclient import discovery
  ml = discovery.build('ml', 'v1')
  job_id = 'projects/{}/jobs/{}'.format(PROJECT_ID, JOB_NAME)
  request = ml.projects().jobs().get(name=job_id)

  response = request.execute()
  alpha = response['trainingOutput']['trials'][0]['hyperparameters']['alpha']
  max_iter = response['trainingOutput']['trials'][0]['hyperparameters']['max_iter']
  ```
3. Retain with the best hyperparamters and export
  ```bash
  gcloud ai-platform jobs submit training $JOB_NAME \
    --region=$REGION \
    --job-dir=$JOB_DIR \
    --master-image-uri=$IMAGE_URI \
    --scale-tier=$SCALE_TIER \
    -- \
    --training_dataset_path=$TRAINING_FILE_PATH \
    --validation_dataset_path=$VALIDATION_FILE_PATH \
    --alpha=$alpha \
    --max_iter=$max_iter \
    --nohptune
  ```

### Serve and Query the model
1. Create a model resource
  ```bash
  gcloud ai-platform models create $model_name \
    --region=$REGION \
    --labels=$labels
  ```
2. Create a model version
  $JOB_DIR is where model.pkl is exported
  ```bash
  gcloud ai-platform version create {model_version} \
    --model={model_name} \
    --origin=$JOB_DIR \
    --runtime-version=1.15 \
    --framework=scikit-learn \
    --python-version=3.7
  ```
3. Query the model
  ```bash
  gcloud ai-platform predict \
    --model $model_name \
    --version $model_version \
    --json-instances $input_file
  ```
