# [For AWS Certified Solution Architect Associate] Understanding RDS

## RDS Features

### [Multi-Availability Zone](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html)
Multi-AZ deployments can have one standby or two standby DB instances
A Multi-AZ DB instance deployment has one standby DB instance that provides failover support, but doesn't serve read traffic.

- A Multi-AZ DB instance deployment characteristics
  - There is only one row for the DB instance
  - The value of Role is Instance or Primary
  - The value of Multi-AZ is Yes

- A Multi-AZ DB cluster deployment characteristics
  - There is a cluster-level row with three DB instance rows under it
  - For the cluster-level row, the value of Role is Multi-AZ DB cluster
  - For each instance-level row, the value of Role is Writer instance or Reader instance
  - For each instance-level row, the value of Multi-AZ is 3 Zones

### Amazon Aurora
Amazon Aurora is a modern relational database service offering 

- High performance and availability with up to 15 low-latency read replicas
- point-in-time recovery
- Auto-scales up to 128 TB per database instance
- A range of developer tools for building serverless and machine learning (ML)-driven applications
- A distributed, fault-tolerant, and self-healing storage system that is decoupled from compute resources
- Continuous backup to Amazon Simple Storage Service (Amazon S3)
- Replication across three Availability Zones (AZs).
- Fully open source MySQL- and PostgreSQL-compatible editions

#### PostgreSQL/MySQL compatible
Amazon Aurora is drop-in compatible with existing PostgreSQL/MySQL open source databases and adds support for new releases regularly



