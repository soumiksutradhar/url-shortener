#!/bin/bash

set -e

echo "--->Running Terraform<---"
terraform apply -auto-approve

echo "--->Fetching instance public IP<---"
public_ip=$(terraform output -raw aws_instance_public_ip)
echo "IP fetched: $public_ip"

echo "--->Updating Ansible inventory<---"
cat > inventory.ini << EOF
[webservers]

$public_ip ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/devops-forge
EOF

echo "--->Waiting to SSH into instance<---"
sleep 15

echo "--->Running Ansible playbook<---"
ansible-playbook -i inventory.ini playbook.yaml

echo "--->Server provisioned and configured!!!<---"
