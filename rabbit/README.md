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
an Amazon EC2 instance for the Millinocket rabbit broker.

- Log into aws
- Choose launch Template WorldRabbit, version 3 (recipe below)

### EC2 Launch Template WorldRabbit, version 3 recipe

We are likely going to go with a managed Rabbit service. However, these instructions are primarily about getting
docker-compose files running under systemctl on an ubuntu 22.04 machine - which is how we will run most of the agents

Make an ec2 instance:

- AMI ubuntu 22.04 LTS, arm64 architecture (version 2 was ubuntu 20.04)
- m6g.medium instance type
- gridworks-hybrid key (version 2 was gridworks-main)
- RabbitMQ security group
- 16 GiB storage for root volume

Log into the ec2 instance and then:

- Install docker from source (in order to use docker-compose in systemctl)
  - Update package list: `sudo apt update`
  - Install dependencies: `sudo apt install apt-transport-https ca-certificates curl software-properties-common`
  - Add Docker GPG key: `curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg`
  - Add Docker repo: `echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null`
  - Update package list agin: `sudo apt update`
  - Install Docker: `sudo apt install docker.io`
  - Put docker under systemctl, starting on boot:
    - `sudo systemctl start docker`
    - `sudo systemctl enable docker`
  - Test that docker is running: `sudo reboot` and then `sudo docker ps`
- Install docker compose:
  - `sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`
  - `sudo chmod +x /usr/local/bin/docker-compose`
- install this repo:
  - `git clone git@github.com:thegridelectric/gridworks.git`
- change password for rabbit
  - nano gridworks/rabbit/rabbitconfig/rabbitmq.conf
  - replace both occurences of THE_PASSWORD with password in shared location
    - GridWorks: 1password, look up rabbit
- set up docker-compose under systemctl
  - Make a new service unit file:
    `sudo cp gridworks/rabbit/docker-compose.service /etc/systemd/system/broker.service`
  - reload the daemon: `sudo systemctl daemon-reload`
  - Enable the service to start on boot: `sudo systemctl enable broker`

PROBLEM:

```
ubuntu@rabbit-template:~/gridworks/rabbit$ sudo docker-compose -f broker_arm.yml up -d
[+] Running 0/0
 ⠋ Container rabbit  Starting                                                                                                                                                                 0.0s
Error response from daemon: mkdir /var/lib/docker/overlay2/05ac3165a2f4c4e9dd936d53c24cf8e18f17e5aeaef827838de25ee00a87f97c/merged: no space left on device
```

and indeed,

```angular2html
df -h
Filesystem       Size  Used Avail Use% Mounted on
/dev/root         16G   16G     0 100% /
```

As soon as the docker rabbit starts, the remaining 14 disk fills up in about 2 minutes.

## Dev Brokers

Various GridWorks repositories -- for example [gridworks-atn](https://github.com/thegridelectric/gridworks-atn/tree/dev)
-- use local docker images for developers to set up a dev rabbit broker on the dev machines. These docker images
are loaded with exchange and binding declarations maintained in this repo at
[gridworks/rabbit/rabbitconfig/rabbit_definitions_dev.json](https://github.com/thegridelectric/gridworks/blob/dev/rabbit/rabbitconfig/rabbit_definitions_dev.json).

In order to have a single location (above) with the bindings and exchanges, other dev repos are expected to use
these docker images in their docker-compose files instead of loading local bindings/exchanges.

LATEST VERSIONS:

- For arm machines: **jessmillar/dev-rabbit-arm:chaos**53ea3a0**20230622**
- For x86 machines **jessmillar/dev-rabbit-x86:chaos**53ea3a0**20230622**

This directory is where new tags for the docker images with name patterns `jessmillar/dev-rabbit-x86:TAG` and
`jessmillar/dev-rabbit-arm:TAG` are built. In order to push to docker, you need credentials for the docker account
jessmillar (in GridWorks 1Password). Build the arm version on an arm machine and the x86 version on an x86 machine.
