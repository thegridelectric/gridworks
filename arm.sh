#!/bin/bash
# Use this script to start a local rabbit broker for dev purposes if 
# your computer has an arm architecture. Otherwise use x86.sh
docker stop gw-dev-rabbit
cp for_docker/arm.yml arm.yml
docker-compose -f arm.yml up -d
rm arm.yml
