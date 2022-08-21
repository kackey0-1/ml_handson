# [For AWS Certified Solution Architect Associate] Understanding AWS Lambda

Lambda is a compute service that lets you run code without provisioning or managing servers. Lambda

## AWS Lambda Features

### Lambda Invocations
- Asynchronous Invocation(=Event-Based Invocation)
  - Poll-Based
    - AWS DynamoDB
    - AWS Kinesis Stream
    - AWS SQS
    
  - Pull-Based
    - AWS S3
    - AWS SES
    - AWS SNS
    - AWS CodePipeline
    - AWS IoT(including IoT Events)
    - AWS CloudFormation
    - AWS CloudWatch Log
    - AWS CloudWatch Events
    - AWS CodeCommit
    - AWS Config

- Synchronous Invocation(=Request-Based Invocation)
  - ELB/ALB
  - AWS Cognito
  - AWS Alexa
  - AWS API Gateway
  - AWS CloudFront
    - Viewer Request
      - This event occurs when an end user or a device on the Internet makes HTTP(S) request to CloudFront, and the request arrives at the edge location closest to that user
    - Viewer Response
      - This event occurs when the CloudFront server at the edge is ready to response to the end user or the device that made the request
    - Origin Request
      - This event occurs when that CloudFront server at the edge server does not already have the requested object in its cache, and the viewer request is ready to be sent to your backend origin webserver
    - Origin Response
      - This event occurs when the CloudFront server at the edge receives a response from your backend origin webserver
  - AWS Kinesis Data Firehose
  - AWS Step Functions
  - AWS S3 Batch

### Deployment and Versioning
- Update function code(Deployment)
  - When updating Lambda function, there will be a brief window of time, typically less than a minutes. When requests could be served by either the old or the new version of your function

- Specifying Version
  - Qualified ARN
    - the function ARN with the version suffix
    - `arn:aws:lambda:aws-region:acct-id:function:helloworld:$LATEST`
  - Unqualified ARN
    - the function ARN without the version suffix
    - `arn:aws:lambda:aws-region:acct-id:function:helloworld`
  - Qualified ARN(with using alias(=PROD))
    - `arn:aws:lambda:aws-region:acct-id:function:helloworld:PROD`

- [AWS Lambda Aliases(for deployment)](https://docs.aws.amazon.com/lambda/latest/dg/aliases-intro.html?shortFooter=true)
  - Easier support for promotion of new versions of Lambda functions and rollback when needed
  - Simplify management of event source mappings
![](https://s3.amazonaws.com/media.whizlabs.com/learn/2019/01/22/questions_scmspn.png)

### AWS Lambda Limits
- Memory  allocation range
  - Minimum 128MB
  - Maximum 3008MB
  
  if maximum use is exceeded function invocation will be terminated

- Execution Time
  - 900 seconds(15 minutes) 
    - After 900 seconds, the execution will be terminated
  - Workaround for this
    - Use [Dead-letter Queue Strategy](#Error Handling)

- Batch Size for Event source
  - 10 queue messages per batch For AWS SQS as Event

### Input for Lambda Execution
- Environment Variables
  - User can use environment variables to adjust your function's behavior without updating code
  - AWS_LAMBDA_FUNCTION_VERSION environment variable
    - is used for version info
    - You can also refer to getFunctionVersion from Context Object in process
- Constant Variables
  - User can set the "Constant(JSON text)" option while selecting Lambda Function as a trigger for CloudWatch's scheduled event
 
### AWS X-Ray
Lambda functions send trace data to X-Ray, and X-Ray processes the data to generate a service map and searchable trace summaries.

- Visualize the components of your application
- Identify performance bottlenecks
- Troubleshoot requests that resulted in an error

## Error Handling  
### Dead letter Queue(=DLQ)
If user configure Dead-letter Queue and send a notification to SNS topic/SQS.
Following processes will be taken place when the execution abruptly terminated.
User can use SQS as well as DLQ.

1. The execution abruptly terminated
2. Upon error, Lambda will via DLQ configured(SNS topic here)
3. SNS/SQS invokes to Lambda function for either of purposes
   - For error notification 
   - For re-try

Note: Check for [more implementation details](https://aws.amazon.com/jp/blogs/compute/robust-serverless-application-design-with-aws-lambda-dlq/)
![](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2022/06/09/deadletterqueues-1.jpg)

## Networks
AWS Lambda runs your function code securely within a VPC by default, **However**
- To enable your Lambda function to access resources inside private VPC
  - must provide additional VPC-specific configuration information that includes IDs and security group IDs
- To enable your Lambda function to connect securely to other resources within your private VPC
  - must set up elastic network interfaces(ENIs)

## Potential Use Cases for Lambda
- Periodically check the log files for errors in CloudWatch or CloudTrail and send out notifications through SNS
- Schedule a job and invoke a Lambda function to generate AWS resource usage reports based on certain tags
- A website with scalable schedule backend layer that will persist data into RDS or DynamoDB

## Secure Environment for Lambda
- Configure Lambda functions to use key configuration
  - Lambda key configuration allows you to have your Lambda functions use an encryption key
    1. create the key in AWS KMS
    2. use the created key to encrypt the environment variables that you can use to change your function without deploying any code
- Use encryption helpers
  - Encryption Helpers make your lambda function more secure by allowing you to encrypt your environment variables before they are sent to Lambda

## Logging
- Execution role for CloudWatch
  - logs:CraeateLogGroup
  - logs:CreateLogStream
  - logs:PutLogEvents


