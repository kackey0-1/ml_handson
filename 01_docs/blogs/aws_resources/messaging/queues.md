# [For AWS Certified Solution Architect Associate] Understanding SNS/SQS

## Amazon SNS
### SNS Features
- Valid Delivery Protocols
  - HTTP
  - HTTPS
  - Email
  - Email-JSON
  - Amazon SQS
  - AWS Lambda
  - SMS

- Amazon SNS Message Filtering
  - by default, a subscriber of an Amazon SNS topic receives every message published to the topic
  - a subscriber assigns a filter policy to the topic subscription to receive only a subset of the messages

- Message Attribute Items and Validation
  - Name
    - the message attribute name can contain the following characters: [A-Za-z0-9_-.]
  - Type
    - the supported message attribute data types are String,String.Array,Number and Binary
  - Value
    - the user specified message attribute value

## Amazon SQS(Simple Queue Service)
### SQS Features
Amazon SQS offers a secure, durable, and available hosted queue that lets you integrate and decouple distributed software systems and components

- Message Basic States
    - Sent to a queue by a producer
    - Received from the queue by a consumer
    - Deleted from the queue

- [Amazon SQS visibility timeout](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html)
  - When a consumer receives and processes a message from a queue, the message remains in the queue
  - To prevent other consumers from processing the message again, Amazon SQS sets a visibility timeout, a period of time during which Amazon SQS prevents other consumers from receiving and processing the message
  - Amazon SQS doesn't automatically delete the message
    - Because Amazon SQS is a distributed system, there's no guarantee that the consumer actually receives the message (for example, due to a connectivity issue, or due to an issue in the consumer application)
    - Thus, the consumer must delete the message from the queue after receiving and processing it

![](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/images/sqs-visibility-timeout-diagram.png)

- [Amazon SQS Short and Long Polling](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-short-and-long-polling.html#sqs-long-polling)
  - Short Polling
    - default setting
  - Long Polling
    - Long Polling helps reduce the cost of using SQS 
      - eliminate empty responses by allowing AWS SQS to wait until a message is available in a queue before sending a response
      - eliminate false responses by querying all rather than a subset of AWS SQS servers
        - by eliminating the number of empty response and false empty response

- Amazon SQS Batch Actions
  - to reduce costs for manipulate up to 10 messages with a single action, you can use following actions
    - SendMessageBatch
    - DeleteMessageBatch
    - ChangeMessageVisibilityBatch


## Amazon Security Token Service(STS)

- AWS STS enables user to request temporary, limited-privilege credentials
  - GetFederationToken returns a set of temporary security credentials
    - https://docs.aws.amazon.com/STS/latest/APIReference/API_GetFederationToken.html
- AWS STS enables users to assume role(= AssumeRole)
  - AssumeRole return a set oof temporary security credentials 
    - https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html
- AWS STS is available as a global service







