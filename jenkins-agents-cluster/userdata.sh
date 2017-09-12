#!/bin/bash
echo ECS_CLUSTER=jenkins-agents >> /etc/ecs/ecs.config

# Allow child docker containers permissions to use docker.sock
sudo chmod 777 /var/run/docker.sock