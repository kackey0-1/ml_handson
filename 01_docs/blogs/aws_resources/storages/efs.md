# EFS (Elastic File Service)
- Typical EFS Use Case
  - Data is stored redundantly in a single AZ
  - Up to thousands of Amazon EC2 instances from multiple AZs, can connect concurrently to a file system
  - Big data and analytics, media processing workflows, content management, web serving, and home directories that do not require Multi-AZ resilience

- Modes
  - Performance Mode
    - Max I/O Performance Mode
      - Max I/O mode supports 500,000+ IOPS and has higher per-operation latencies when compared to General Purpose mode
      - File system in the Max I/O mode can scale to higher levels of aggregate throughput and operations per second
      - There is tradeoff of slightly higher latencies for file operations
      - Usages:
        - big data analysis
        - media processing
        - genomics analysis
    - General Purpose Performance Mode
      - General Purpose mode supports up to 35,000 IOPS
      - AWS recommends the General Purpose performance mode for the majority of EFS file systems
      - General Purpose is ideal for latency-sensitive use cases
  - Throughput Mode
    - Bursting Throughput Mode
      - <!-- TODO https://docs.aws.amazon.com/efs/latest/ug/efs-ug.pdf -->
      - Bursting Throughput mode is the default Amazon EFS throughput mode.
      - With requirements greater than high throughput to storage(MiB/s per TiB) ratios allowed by Bursting Throughput mode
    - Provisioned Throughput Mode
      - Provisioned Throughput mode is available for applications with high throughput to storage(MiB/s per TiB) ratios
      - For applications that have a relatively constant throughput, we recommend Provisioned Throughput mode
      - <!-- TODO https://docs.aws.amazon.com/efs/latest/ug/efs-ug.pdf -->

- Protocol for to enable SSH access between EC2 and EFS
  1. Open port 22(SSH) on EC2 security group
  2. Open port 2049(NFS(which is not secured by default)) on EFS security group

- Encryption Support
  - Encryption at rest
    - Encryption at rest is enabled by default when creating EFS console
    - EFS uses an industry standard AES-256 encryption algorithm to encrypt EFS data
  - Encryption of data in transit
    - Encryption of data in transit can be enabled when mounting the file system using EFS mount helper
    - mount helper uses TLS version 1.2 to communicate with the file system
    ![](https://s3.amazonaws.com/media.whizlabs.com/learn/CSAA-efs-6.PNG)

- Work with VPC Peering
  1. Establish VPC connection between VPCs
  2. Use the instances that are created in the new VPC to access the already existing EFS with mount targets


Note: 
IOPS: Input/Output Per Second