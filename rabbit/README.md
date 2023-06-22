## 2023-2024 Millinocket pilot world rabbit broker

 - Elastic IP 100.26.91.172
 - DNS hw1-1.electricity.works
  - management console: http://hw1-1.electricity.works:15672/

For self-serve, see hybrid broker instructions below

## Hybrid brokers

The brokers for hybrid worlds start with an "h" and have the pattern "hword-n" where hword is 
alphanumeric and n is an integer. In hybrid worlds, "anything goes" - which means simulated devices may participate 
with physical devices. Some devices may use simulated time while others may use real time. And
financial contracts are all simulated.

Hybrid brokers are expected to run in the cloud. Here are instructions for setting up
an Amazon EC2 instance capable of handling a handful of homes.

 - Log into aws
 - Choose launch Template WorldRabbit, version 3 (recipe below)



### EC2 Launch Template WorldRabbit, version 3 recipe

Make an ec2 instance:
  - AMI ubuntu 22.04 LTS, arm64 architecture (version 2 was ubuntu 20.04)
  - m6g.medium instance type
  - gridworks-hybrid key (version 2 was gridworks-main)
  - RabbitMQ security group
  - 16 GiB storage for root volume

Log into the ec2 instance and then:
   - install snap
     - `sudo apt update`
     - `sudo apt install snapd`
   - install docker using snap
     - `sudo snap install docker`


Instructions for 
jessmillar/dev-rabbit-x86:chaos__53ea3a0__20230622