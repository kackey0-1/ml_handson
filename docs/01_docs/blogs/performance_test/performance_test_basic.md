# Understanding Performance Test Basic for Cloud Environment

## Objectives for Performance Test

### Objectives for On-Premise environment
1. Assumes various use cases and estimates the response performance of the system in each case
  - Cases where a large number of users register immediately after the start of service use
  - Cases where a large amount of data has accumulated after the service has been running smoothly.
  - Cases where rapid user access is expected due to campaign announcements, etc.
  - ...etc

2. Improve system performance under heavy loads
  - When requests increase due to an increase in access, the system may behave in a way that did not occur before.
    - Decrease in response time
    - System locking conflicts
    - Application and server errors under heavy load
    - Inconsistency or damage to data

3. Pre-select the hardware required to provide the desired performance

### Objectives for Cloud environment
1. Assumes various use cases and estimates the response performance of the system in each case
2. Improve system performance under heavy loads
3. Pre-select the hardware required to provide the desired performance
  - In cloud environment, this objective is less important since we can easily procure hardware
4. **Ensure that the system is scalable**
5. **Understand the scalability characteristics of the system**
  - Optimal infrastructure configuration to handle several throughput levels (e.g. 100rps, 500rps, 1000rps, 2000rps, 5000rps, etc.)
  - Approximate maximum throughput that the web system can handle beyond the target value (marginal performance)

## Performance Indicators for Performance Test
### Throughput
In general, we simply say throughput, we mean RPS.

- Amount of Processing in unit time(RPS(=Request Per Second))
- Transfer rate through network

### Latency
- Processing Time in System
- In general, system latency is often defined as the processing time observed by the user, but usually it is the system processing time that can be controlled in a Web system.

<!-- TODO create pic to explain throughput and latency -->
<!-- https://cdn.comparitech.com/wp-content/uploads/2019/01/DiagramLatency-vs-throughput-2-768x320.jpg -->

## How to Improve each performance indicators
When system performance indicators are throughput and latency,
system performance improvement is nothing more than increasing overall system throughput and decreasing latency

### Throughput Improvement
In general, Web system is a system in which each subsystem is processed in a streamlined process.
The overall throughput is limited by the subsystem with the lowest throughput in this process.

### Latency Improvement
Latency is "the sum of the processing time of each subsystem, including the waiting time".
To improve latency, it is common practice to start with "processes that take the most time" and see if there is anything that can be done to improve latency.

## Good Performance Test Factors
- Load is heavily concentrated on the system under performance test
- Bottleneck areas have been identified
