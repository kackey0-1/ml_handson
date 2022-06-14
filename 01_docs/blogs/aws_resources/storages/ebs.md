# [For AWS Certified Solution Architect Associate] Understanding EBS (Elastic Block Store)

## EBS Features

- Elastic Block Store
    - EBS provides block level storage volumes(that persist independently) for use with EC2 instances
    - EBS volumes are highly available and reliable storage volumes attached to any running instance in the same AZ
- EC2 Instance Store
    - Instance Store provides temporary block level storage for your instance
    - You can specify instance store volumes for an instance only when you launch it
    - You can't detach an instance store volume from one instance and attach it to a different instance

## Volume Types

- SSD backed volumes
  - optimized for transactional workloads involving frequent read/write operations with small I/O size, where the dominant performance attribute is IOPS
- HDD backed volumes
  - optimized for large streaming workloads where throughput(measured in MiB/s) is a better performance measure that IOPS

### HDD(Hard Disk Drive)

|                           | Throughput Optimized HDD                              | Cold HDD                                                                                |
|---------------------------|-------------------------------------------------------|-----------------------------------------------------------------------------------------|
| Volume Type               | st1                                                   | sc1                                                                                     |
| Durability                | 99.8% - 99.9% durability                              | 99.8% - 99.9% durability                                                                |
| Use Cases                 | - Big data<br/>- Data warehouses<br/>- Log processing | - Throughput-oriented storage for data that is frequently accessed<br/>- Scenario where |
| Volume Size               | 1 GiB - 16 TiB                                        | 1 GiB - 16 TiB                                                                          |
| Max IOPS per volume       | 500                                                   | 250                                                                                     |
| Max Throughput per volume | 500 MiB/s                                             | 250 MiB/s                                                                               |
| Amazon EBS Multi-attach   | Not Supported                                         | Not Supported                                                                           |
| Boot volume               | Not Supported                                         | Not Supported                                                                           |

### SSD(Solid State Drive)

|                           | General Purpose SSD                                                                           | Provisioned IOPS SSD                                                                                                                                                                                            |
|---------------------------|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Volume Type               | gp2                                                                                           | io1                                                                                                                                                                                                             |
| Durability                | 99.999% durability                                                                            | 99.999% durability                                                                                                                                                                                              |
| Use Cases                 | - Recommended for most workloads<br/>- System boot volumes<br/>- Low latency interactive apps | - Critical business applications that require sustained IOPS performance, or more than 10,000IOPS or 160 MiB/s of throughput per volume<br/>- Large database workloads such as MongoDB,Cassandra, MySQL, ...etc |
| Volume Size               | 4 GiB - 16 TiB                                                                                | 4 GiB - 16 TiB                                                                                                                                                                                                  |
| Max IOPS per volume       | 256,000                                                                                       | 64,000†                                                                                                                                                                                                         |
| Max Throughput per volume | 4,000 MiB/s                                                                                   | 1,000 MiB/s †                                                                                                                                                                                                   |
| Amazon EBS Multi-attach   | Not Supported                                                                                 | Supported                                                                                                                                                                                                       |
| Boot volume               | Supported                                                                                     | Supported                                                                                                                                                                                                       |

Note: 
† To achieve maximum throughput of 1,000 MiB/s, the volume must be provisioned with 64,000 IOPS, and it must be attached to an instance built on the Nitro System.
io1 volumes created before December 6, 2017 and that have not been modified since creation, might not reach full performance unless you modify the volume.

### Backup Features
- Deleting an Amazon EBS Volume
- Snapshot Lifecycle

Question 3
