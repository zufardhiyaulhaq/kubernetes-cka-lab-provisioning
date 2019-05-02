# Kubernetes CKA Provisioning
Tools build with Ansible to provisioning 3 cluster Kubernetes cluster and single management node to control the cluster.

#### Requirement
- KVM Server
- Routed Network in KVM
- Template Operating System

#### Template Operating System
- Ubuntu 16.04 server
- KVM Server is able to SSH without password into Template Operating System (root and non-root). Example is using public key

## Instalation
- Install Ansible in KVM Server
- Clone Repository
```
git clone
```
- Change variables and hosts
```
hosts/hosts
group_vars/all.yml
```
- Run Ansible
```
ansible-playbook main.yml -i hosts/hosts
```