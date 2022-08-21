# [For AWS Certified Solution Architect Associate] Understanding EBS (Elastic Block Store)

## EBS Features

- Elastic Block Store
    - EBS provides block level storage volumes(that persist independently) for use with EC2 instances
    - EBS volumes are highly available and reliable storage volumes attached to any running instance in the same AZ
- EC2 Instance Store
    - Instance Store provides temporary block level storage for your instance
    - You can specify instance store volumes for an instance only when you launch it
    - You can't detach an instance store volume from one instance and attach it to a different instance

### Volume Types

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

### EBS Volume Encryption

- Encrypts data at rest inside the volume
- Encrypts all data moving between the volume and the instance
- Encrypts all snapshots created from the volume
- Encrypts all volumes created from those snapshots

### EBS Volume Encryption Support Requirements
- Volume type must be supported
  - Encryption is supported by all EBS volume types
- Instance type must be supported
  - Amazon EBS encryption is available on all [current generation instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#current-gen-instances)
  - Following [previous generation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#previous-gen-instances) instance types: A1, C3, cr1.8xlarge, G2, I2, M3, and R3.
- Permissions for IAM users
  - When you configure a KMS key as the default key for EBS encryption, the default KMS key policy allows any IAM user with access to the required KMS actions to use this KMS key to encrypt or decrypt EBS resources

## Metric in CloudWatch
- I/O Operation in specified period of time 
  - VolumeReadBytes
  - VolumeWriteBytes
- the total number of I/O operations in a specified period of time
  - VolumeReadOps
  - VolumeWriteOps
- the total number of seconds by all operations that completed in a specified period of time
  - VolumeTotalReadTime
  - VolumeTotalWriteTime
- the total number of seconds in a specified period of time when no read or write operations were submitted
  - VolumeIdleTime


## EBS-Optimized Instance
Amazon EBS-optimized instance provides additional, dedicated capacity for Amazon EBS I/O
This optimization provides the best performance for your EBS volumes by minimizing contention between Amazon EBS I/O and other traffic from instance

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html

## Backup Features
### Deleting an Amazon EBS Volume
  - After EBS deletion, data is gone and the volume can't be attached to any instance
  - Before EBS deletion, you can store a snapshot of the volume, which you can use to re-create the volume later

### Snapshot
Available Operation on an EBS snapshot
- Creating Image(AMI) from snapshot, which was taken from root volumea
- Creating EBS volume from snapshot
- Sharing a snapshot with another AWS account

Note: you cannot share a snapshot with another AWS account

### Snapshot Lifecycle
You can use Amazon Data Lifecycle Manager(Amazon DLM) to automate the creation, retention, and deletion of snapshots to back up EBS volume

  - Protect valuable data by enforcing a regular backup schedule
  - Retain backup as required by auditors or internal compliance 
  - Reduce storage costs by deleting outdated backups

### Snapshot Encryption
- You can create encrypted volumes or snapshots from unencrypted volumes or snapshots
- If the source snapshot is encrypted, or if the account is enabled for encryption by default, then the snapshot copy is automatically encrypted
- Without enabling encryption by default, a volume restored from an unencrypted snapshot is unencrypted by default

Note: Encrypted EBS volumes are supported on all current generation instance types
