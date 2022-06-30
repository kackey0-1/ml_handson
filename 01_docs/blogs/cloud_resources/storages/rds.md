# [For AWS Certified Solution Architect Associate] Understanding RDS

## RDS Features

### [Replication Functionality](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html#USER_ReadRepl.Create)
Amazon RDS uses the MariaDB, Microsoft SQL Server, MySQL, Oracle, and PostgreSQL DB engines' built-in replication functionality
to create a special type of DB instance called a read replica from a source DB instance
The source DB instance becomes the primary DB instance

Updates made to the primary DB instance are asynchronously copied to the read replica
You can reduce the load on your primary DB instance by routing read queries from your applications to the read replica

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

### DeletionPolicy
Retain option keeps the resource in the event of a stack deletion
The snapshot option creates a snapshot of the resource before that resource is deleted

### Auto Scaling
RDS Storage Auto Scaling continuously monitors actual storage consumption, 
and scales capacity up automatically when actual utilization approaches provisioned storage capacity

## Amazon Aurora
Amazon Aurora is a modern relational database service offering 

- High performance and availability with up to 15 low-latency read replicas
- point-in-time recovery
- Auto-scales up to 128 TB per database instance
- A range of developer tools for building serverless and machine learning (ML)-driven applications
- A distributed, fault-tolerant, and self-healing storage system that is decoupled from compute resources
- Continuous backup to Amazon Simple Storage Service (Amazon S3)
- Replication across three Availability Zones (AZs).
- Fully open source MySQL- and PostgreSQL-compatible editions

### PostgreSQL/MySQL compatible
Amazon Aurora is drop-in compatible with existing PostgreSQL/MySQL open source databases and adds support for new releases regularly



