[For AWS Certified Solution Architect Associate] Understanding Application/Elastic Load Balancer(ALB/ELB)

## ALB(Application Load Balancer)/ELB(Elastic Load Balancer) Features
### Launch Configuration
A launch configuration is a template that is an Auto Scaling group uses to launch EC2 instances
When you create a launch configuration, you specify information for the instances

- AMI ID
- Instance Type
- Key Pair
- Security Groups
- Block device mapping

### [Auto Scaling Group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html)
An Auto Scaling group contains a collection of Amazon EC2 instances that are treated as a logical grouping for the purposes of automatic scaling and management
Before getting started, take the time to review your application thoroughly as it runs in the AWS Cloud

AWS recommends the use of Launch Templates while configuring your ASG(Launch templates can be updated to create new versions)

- How long it takes to launch and configure a server
- What metrics have the most relevance to your application's performance
- How many Availability Zones you want the Auto Scaling group to span
- Do you want to scale to increase or decrease capacity? Do you just want to ensure that a specific number of servers are always running?
- What existing resources you can use

#### Auto Scaling Group Policy
- Scale-In(termination policy)
  - OldestInstance
    - Terminate the oldest instance in the group
    - This option is useful when you're upgrading the instances in the Auto Scaling group to a new EC2 instance type
  - NewestInstance
    - Terminate the newest instance in the group
  - OldestLaunchConfiguration
    - Terminate instances that have the oldest launch configuration
  - ClosestToNextInstanceHour
    - Terminate instances that have the oldest launch configuration
    - This policy is useful when you're updating a group and phasing out the instances from a previous configuration
  - Default
    - Terminate instances according to the default termination policy
    - This policy is useful when you have more than one scaling policy for the group
- Scale-Out(scaling policy)

#### Instance Health Status
By default, EC2 Auto Scaling health checks use the results of the EC2 status checks to determine the health status of an instance
EC2 Auto Scaling determines the health status of an instance using one or more of following

- Status checks provided by EC2(system status checks and instance status check)
- Health checks provided by ELB/ALB
- Custom health checks

Health Check Grace Period
Metric types for Auto Scaling Group Policy

#### Termination flow
1. Scale In
2. Are these instances in multiple availability zones ?
   - When Yes, Select the availability zones with the most instances
   - When No, Got to Step 3
3. Select the instances with the oldest launch configuration
4. Are there multiple instances using the oldest launch configuration ?
   - When No, **Terminate instance**
   - When Yes, Go to Step 5 
5. Select the instances closest to the next billing hour
6. Are there multiple instances closest to the next billing hour ?
   - When No, **Terminate instance**
   - When Yes, Go to Step 7
7. Select an instance at random 
   - Terminate instance

### [Cross-zone Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html#availability-zones)
The nodes for your load balancer distribute requests from clients to registered targets
When cross-zone load balancing is enabled, each load balancer node distributes traffic across the registered targets in all enabled Availability Zones
When cross-zone load balancing is disabled, each load balancer node distributes traffic only across the registered targets in its Availability Zone

![](https://s3.amazonaws.com/media.whizlabs.com/learn/CSAA-efs-7-1.PNG)

### Sticky sessions
[//]: # (TODO)
https://docs.aws.amazon.com/elasticloadbalancing/latest/application/sticky-sessions.html

### X-Forwarded headers
[//]: # (TODO)
https://docs.aws.amazon.com/elasticloadbalancing/latest/application/x-forwarded-headers.html

### [Monitor Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-monitoring.html)
- CloudWatch Metrics
  - You can use Amazon CloudWatch to retrieve statistics about data points for your load balancers and targets as an ordered set of time-series data
- Access Log
  - You can use access logs to capture detailed information about the requests made to your load balancer and store them as log files in Amazon S3
- Request tracing 
  - You can use request tracing to track HTTP requests
- CloudTrail Logs
  - You can use AWS CloudTrail to capture detailed information about the calls made to the ALB/ELB API and store them as log files in Amazon S3

