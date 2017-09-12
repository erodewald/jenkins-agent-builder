#!/bin/bash
echo ECS_CLUSTER=jenkins >> /etc/ecs/ecs.config

# Allow child docker containers permissions to use docker.sock
sudo chmod 777 /var/run/docker.sock

# Mount Jenkins EFS
sudo yum install -y nfs-utils
sudo mkdir -p /var/jenkins_home
sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2 fs-0ec0b747.efs.us-east-1.amazonaws.com:/ /var/jenkins_home