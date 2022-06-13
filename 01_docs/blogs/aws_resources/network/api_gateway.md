# [For AWS Certified Solution Architect Associate] Understanding API Gateway

## About Feature
- API Gateway can integrate with any HTTP-based endpoints available over the internet(or even in private VPC)
- API Gateway caching
  - by Query String Parameter 
    - efficient to use as part of your cache key in most cases
    - this allows you to separate cache responses to equity requests from fixed income request responses
- Integration Type
  - Lambda functions as a backend service
    - Another AWS account's lambda can be used
  - Http 
    - Non-AWS hosted HTTP based operations that are accessible via the public internet
    - AWS Step Functions state machines
    - HTTP endpoints hosted on EC2
    - HTTP endpoints hosted on AWS Elastic Beanstalk
  - Mock
  - AWS Service
    - can integrate API Gateway with other AWS services directly
    - ex: You can expose an API method in API Gateway that sends data directly to Amazon Kinesis
  - VPC Link
    - a way to connect to the resources within a private VPC
- Cache Feature
  - Cache Capacity
    - setting for how much you can set
  - Encrypt Cache
  - Flush entire cache
- Logging
  - CloudWatch access logging
    - allows you to capture which resource accessed an API and the method used to access the API
  - CloudWatch execution logging
    - allows you to capture user request and response payloads as well as error traces

![](https://s3.amazonaws.com/media.whizlabs.com/learn/2019/01/22/questions_uo30kg.png)

## API Gateway Performance
- How can we improve API performance
  - Enable throttling and control the number of requests per second
    - to prevent your API from being overwhelmed by many requests
  - Enable API caching serve frequently requested data from API cache
    - API Gateway can cache endpoint's responses
    - to reduce the number of calls made to your endpoint and improve the latency of requests

- HttpStatus=429 (Too Many Requests)
  - When it happens
    - Lambda function has exceeded the concurrency limit
      - When traffic spikes, Lambda function can exceed the limit set on the number of concurrent instances.
    - API Gateway has exceeded the steady-state request rate and burst limits
      - When API Gateway request volume reaches the steady-state request rate and bursting limit,
        API Gateway throttles your requests to protect your back-end-services

## Security
API Gateway supports multiple mechanisms for controlling access to your API
<!-- TODO fill in all details below -->
- Resource policies
- Standard AWS IAM roles and policies
- Cross-Origin resource sharing(CORS)
- Lambda Authorizer
- Amazon Cognito user pools
- Client-side SSL certificates
- Usage Plans

<p>Please see the Amazon API Gateway developer guide titled<strong> </strong><strong>Throttle API requests for better throughput </strong>(<a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html">https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html</a>), the Towards Data Science article titled<strong> Full Stack Development Tutorial: Integrate AWS Lambda Serverless Service into Angular SPA</strong> (<a href="https://towardsdatascience.com/full-stack-development-tutorial-integrate-aws-lambda-serverless-service-into-angular-spa-abb70bcf417f">https://towardsdatascience.com/full-stack-development-tutorial-integrate-aws-lambda-serverless-service-into-angular-spa-abb70bcf417f</a>), the Amazon API Gateway developer guide titled<strong> Invoking a REST API in Amazon API Gateway </strong>(<a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-call-api.html">https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-call-api.html</a>), the AWS Lambda developer guide titled <strong>Lambda function scaling </strong>(<a href="https://docs.aws.amazon.com/lambda/latest/dg/invocation-scaling.html">https://docs.aws.amazon.com/lambda/latest/dg/invocation-scaling.html</a>), and the Amazon DynamoDB developer guide titled <strong>Error Handling with DynamoDB </strong>(<a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.Errors.html">https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.Errors.html</a>)</p>
