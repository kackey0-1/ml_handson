# [For AWS Certified Solution Architect Associate] Understanding Route53

## AWS Route53 Features
AWS Route53 is a highly available and scalable Domain Name System(DNS) web service

### Register domain names
Your website needs a name, such as example.com Route53 lets you register a name for your website or web application

- For an overview, see [How Domain Registration Works](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/welcome-domain-registration.html)
- For a procedure, see [Registering a New Domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-register.html)
- For a tutorial that takes you through registering a domain and creating a simple website in S3 bucket, see [Getting stated with Amazon Route53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/getting-started.html)

### Route internet traffic to the resources for domains
When a user opens a web browser and enters your domain name(example.com) or subdomain name(apex.example.com) in the address bar , Route53 helps connect the browser with your website or web application

- For an overview, see [How Internet Traffic Is Routed to Your Website or Web Application](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/welcome-dns-service.html)
- For procedures, see [Configuring Amazon Route53 as your DNS Service](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring.html)

### Check the health of resources
Route53 sends automated requests over the internet to a resource for health check

- Health checks that monitor an endpoint
  - You can configure a health check that monitors an endpoint that you specify either IP address or by domain name
- Health checks that monitor other health checks(calculated health checks)
  - You can create health check that monitors whether Route53 considers other health checks healthy or unhealthy
- Health checks that monitor CloudWatch alarms
  - You can create CloudWatch alarms that monitor the status of CloudWatch metrics

- For an overview, see [How Internet Traffic is Routed to Your Website or Web Application](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/welcome-dns-service.html)
- For procedures, see [Creating Amazon Route53 Health Checks Configuring DNS Failover](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html)

## [DNS Record Type](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html)
1. Alias record
   - Alias record to route traffic to AWS resources
   - Route53 automatically recognizes the change in the resource
2. CNAME record
   - CNAME record redirects DNS queries for a record name regardless of the record type specified in DNS query, such as A or AAAA

## Routing Traffic to Other AWS Resources
- A - IPv4 Address with Alias=YES
  - Amazon S3
  - Elastic Load Balancer
  - Amazon EC2
  - AWS Elastic Beanstalk
  
- CNAME - Canonical Name with ALIAS=NO
  - Amazon CloudFront
  - Amazon RDS
  - Amazon SES
  - Amazon WorkMail

## Routing Policy
- Simple routing policy
  - Use for a single resource that performs a given function for your domain
- Failover routing policy
  - Use when you want to configure active-passive failover
- Geolocation routing policy
  - Use when you want to route traffic based on the location of your users
- Geoproximity routing policy
  - Use when you want to route traffic based on the location of your resources
- Latency routing policy
  - Use when you have resources in multiple AWS Regions and you want to route traffic to the region that provides the best latency
- Multivalue answer routing policy
  - Use when you want Route53 to respond to DNS queries with up to eight healthy records selected at random
- Weighted routing policy
  - Use to route traffic to multiple resources in proportions that you specify(like 25% to A, 25% to B, 50% to C)
