# [For AWS Certified Solution Architect Associate] Understanding Cost Management

## Computing
- AWS Savings Plan
  - Savings Plan is a flexible pricing model that provides low prices in exchanges for a commitment to a specific instance family in a chosen AWS Region (for example, M5 in Virginia).
  - You can save up to 72 percent on your AWS compute workloads
  - Compute Savings Plans provide lower prices on Amazon EC2 instance usage regardless of instance family, size, OS, tenancy, or AWS Region

Note: This also applies to AWS Fargate and AWS Lambda usage

### Lambda Function
#### Direct factors of cost in Lambda
- The memory allocated to the Lambda Function
- The total number of requests for the Lambda Function

### EC2
- Instance Type
  - Spot Instance
    - A Spot Instance is an instance that uses spare EC2 capacity that is available for less than the On-Demand price
    - Because Spot Instances enable you to request unused EC2 instances at steep discounts
    - Spot Instances are a cost-effective choice if you can be flexible about when your applications run and if your applications can be interrupted
  - OnDemand Instance
  - Reserved Instance
  - Dedicated Instance

- c5 Instance Family
  - C5 instance type is covered by new Saving Plan

- To use SpotInstance in non-prod env
  - in the CloudFormation tempalte, use a parameter to set the OnDemandPercentageAboveBaseCapacity property
  - Set the parameter to be 0 for non production, but set the parameter to be 100 in production

## Networking
### S3
- To reduce network cost
  - you can create VPC Gateway Endpoint for private subnet group(no need to create NAT Gateway)

### CloudFront
- Free service in CloudFront
  - Data transfer from origin to CloudFront edge location(Amazon CloudFront origin fetches)
  - if the CloudFront origin is hosted in AWS like EC2, the origin fetches are free
- To increase cache duration
  - Modify the application to add a Cache-Control header to control how long the objects stay in the CloudFront cache

