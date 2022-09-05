# [For AWS Certified Solution Architect Associate] Understanding ECS(Elastic Container Service)

## ECS Features
Note: Check out details [here](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html#welcome-features)
### Infrastructure to run container
  - Amazon EC2
  - Fargate
  - External Resources

### Containers and Images
  - Push&Pull images using Amazon Elastic Container Registry

### Task Definitions
  - a service is a configuration that you can use to run and maintain a specified number of tasks simultaneously in a cluster
  - used to run an individual task or task within a service
  - JSON format template is used to form the application
    - Parameters
      - Docker Image
      - CPU/Memory to use with each container
      - Launch type to use(EC2/Fargate)
      - Whether containers are linked together in a task
      - Docker networking mode to use for the containers in your task
      - (Optional) The ports from the container to map to the host container instance
      - Whether the task should continue to run if the container finishes or fails
      - The command to start up container service
      - (Optional) The environment variables that should be passed to the container when it starts
      - Any data volumes that should be used with the containers in the task
      - (Optional) The IAM role that your tasks should use for permissions

### Service Definitions
  - service definitions defines
    - Which task definition to use with your service
    - How many instantiations of that to run
    - Which load balancers (if any) associate with your tasks
  - Service Definition template(JSON format)
    - Parameters
      - Cluster
      - [Capacity provider strategy](https://dev.classmethod.jp/articles/regrwoth-capacity-provider/)
        - The capacity provider strategy to use for the service
      - Client token
        - Unique, case-sensitive identifier you provide to ensure the idempotency of the request
### Tasks and Scheduling
Editing

### Clusters
Editing

### [Amazon ECS Container Agent](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html)
The Amazon ECS container agent supports a number of configuration options, most of which should be set through environment variables.
When you launch as ECS container instance, you have the option of passing user data to the instance.
The data can be used to perform common automated configuration tasks and even run scripts when the instance boots.
The most common use cases for user data are to pass configuration information to the Docker daemon and the Amazon ECS container agent

## ECS Networking
For accessing the AES ECS service endpoint

- Create an interface VPC Endpoint for ECS service and attach to VPC subnet's route table in which ECS instances are running
  <!-- 
    TODO check out more detail
    https://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/vpc-endpoints.html
  -->
- Container instance have public IP addresses
- Create ECS services in VPC private subnet, and use ALB as gateway

## ECS Monitoring
Users have control over AWS ECS container instances and can set up monitoring like a normal EC2
Since user have root access to the operating system of container instance, you can even install 3rd party software on ECS.

Of course, we can use AWS CloudTrail, to captures all API calls for Amazon ECS as events.

## ECS Permission
- `ecs:Poll` policy (**required**)
  - used to grant the agent permission to connect with the Amazon ECS service to report status and get commands
- `ecs:CreateCluster` policy (optional)
  - provided that the cluster you intend to register your container instance into already exists
  - if the cluster does not already exist, the agent must have permission to create it
  - (or you can create the cluster with `create-cluster` command 
