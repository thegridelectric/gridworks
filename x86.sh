#!/bin/bash
# Use this script to start a local rabbit broker for dev purposes if 
# your computer has an x86 architecture. Otherwise use arm.sh
docker stop gw-dev-rabbit
cp for_docker/x86.yml x86.yml
docker-compose -f x86.yml up -d
rm x86.yml
