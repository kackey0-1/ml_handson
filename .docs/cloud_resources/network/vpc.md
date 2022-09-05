# [For AWS Certified Solution Architect Associate] Understanding VPC

## VPC(Virtual Private Cloud) Features
### VPC Flow Log
- VPC flow log captures IP traffic going to and from network interfaces in the VPC
- Flow log is stored using Amazon CloudWatch Logs 

### VPC Peering 
- VPC peering connection is a networking connection between two VPCs that enables you to route traffic VPCs them using private IPv4 addresses or IPv6 addresses
- VPC Peering uses the existing infrastructure of a VPC and this solution is straightforward that facilitates the transfer of data between two VPCs

### Main VPC Route Table
  - For main route table, all implicit associations of subnets will point to newly set main route table
  - Custom route table can be replaced with existing main route table

### CIDR Block 
  - Reserved IP in each CIDR block
    - The first four IP addresses and the last IP address in each subnet CIDR block are reserved by AWS 
    - For example, in a subnet with CIDR block 10.0.0.0/24
      - 10.0.0.0
        - AWS reserves this IP for Network address
      - 10.0.0.1
        - AWS reserves this IP for the VPC router
      - 10.0.0.2
        - AWS reserves this IP for DNS 
      - 10.0.0.3
        - AWS reserves this IP for future use
      - 10.0.0.255
        - AWS reserves this IP for network broadcast address
        - AWS do not support broadcast in VPC, therefore AWS reserves this IP 
  - Primary/Secondary CIDR Block for VPC
    - Can add Secondary CIDR blocks for the VPC when you want to extend existing VPC CIDR range
    - A route is automatically added to the VPC route tables to enable routing when you added & associated secondary CIDR blocks to VPC

### Network Access Control List(NACL)
  - Additional layer of security
  - If you want to set ACL, you must set up Inbound/Outbound rules(To allow inbound/outbound both connection)

### Security Group 
  - By default, rules in security group disallows all incoming
  - By default, outbound traffic is allowed

### MAC Address
  - Use a VPC with an elastic network interface that has a fixed MAC Address
  - For the server to be MAC dependent, you must use VPC with an ENI(Elastic Network Interface)

- [Egress Only Internet Gateways](https://docs.aws.amazon.com/vpc/latest/userguide/egress-only-internet-gateway.html)
  - Egress Only Internet Gateway is a VPC component that allows outbound communication over IPv6 from instances in your VPC to the internet
  - [Details Here](https://qiita.com/miyuki_samitani/items/b1e19f55ff7bce131a9e)
 

## [AWS VPN](https://docs.aws.amazon.com/vpn/index.html) Features
AWS VPN is more cost-effective and based on existing internet connections than AWS Direct Connect introduction.
### [VPN Tunnels](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPNTunnels.html)
  - A Site-to-Site VPN connection offers two VPN tunnels between a virtual private gateway or a transit gateway on the AWS side, and a customer gateway (which represents a VPN device) on the remote (on-premises) side.
  - User cannot modify that AWS Site-to-Site VPN has two tunnels for redundancy
  - When one tunnel becomes unavailable, network traffic is automatically routed to the other available tunnel

#### Advanced Options for Tunnel
The encryption algorithms is configured by users such as:
- AES128
- AES256


### [AWS VPN Cloud Hub](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPN_CloudHub.html)
AWS VPN Cloud Hub requires you to create 

  - A virtual private gateway with multiple customer gateways each with a unique
    - Border Gateway Protocol (BGP)
    - Autonomous System Number (ASN)

## [Direct Connect Gateway](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways-intro.html) Features
Direct Connect Gateway is globally available resource.
You associate an AWS Direct Connect Gateway with either of the following gateways:
- A transit gateway when you have multiple VPCs in the same Region
- A virtual private gateway

You can also use a virtual private gateway to extend your Local Zone
This configuration allows the VPC associated with the Local Zone to connect to a Direct Connect gateway

### Use Cases
- can be used to establish high performance network connections to different AWS Regions 
- can be used to reduce management loads


## [AWS Direct Connect](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect.html)
Using **private VIF(Virtual InterFace)** on AWS Direct Connect, you can establish private connectivity between AWS and your data center, office, or collocation environment
AWS Direct Connect is more highly available than Direct Connect Gateway

### Use Cases
- Used to establish a dedicated connection from an on-premises network to one or more VPCs in the same region
- Used to establish an end-to-end secure IPSec connection

## [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/how-transit-gateways-work.html) Feature
A transit gateway works as Regional virtual router for traffic flowing between VPCs and on-premises networks

![](https://docs.aws.amazon.com/vpc/latest/tgw/images/transit-gateway-overview.png)

## Case Studies
### Connection among private subnets in same VPC network
- VPC  10.10.0.0/16
  - Public Subnet    10.10.1.0/24
  - Private Subnet1  10.10.2.0/24
  - Private Subnet2  10.10.3.0/24

Now public subnet has the main route table,
and thw private subnets have two different route tables respectively.
AWS sysops team reports a problem starting the EC2 instance in private subnet1
cannot communicate to the RDS MySQL database on private subnet2.
What are the possible reasons?

- RDS security group inbound rule is incorrectly configured with 10.10.1.0/24 instead
- 10.10.3.0/24 subnet's NACL(Network Access Control List) is modified to deny inbound on port 3306 from subnet 10.10.2.0/24

### VPC Endpoint for AWS S3
After creating new S3 bucket, sending requests from an EC2 instance via the VPC endpoint,
you found the requests are failing.
What are the possible reasons?

- VPC endpoint contains a policy, currently restricted to certain S3 buckets, and does not contain a new S3 bucket
- AWS IAM role/user does not have access to the new S3 bucket
- EC2 instance security group outbound rules are restricted and does not contain prefix list
- Subnet's Network ACL inbound/outbound rule does not allow traffic from S3

### Connection from Private Subnet to Internet
- VPC
  - Public Subnet
    - NAT Gateway(**Elastic IP is required**)
  - Private Subnet

When you try to download patches from the internet onto the EC2 instance,
the connection gets timed out. What could be the reason ?

- NAT Gateway created in a private subnet without an internet Gateway
- The route table is NOT updated to direct Internet-bound traffic to the NAT Gateway
