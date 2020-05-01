# Kubernetes CKA Provisioning
Tools build with Ansible to provisioning multiple cluster Kubernetes cluster and single management node to control the cluster. The cluster is based on CKA Curriculum and Exam tips and create this following cluster:

| Cluster | Members | CNI      | Description |
|---------|---------|----------|-------------|
| k8s     | 1 master, 2 worker        | Flannel  | k8s cluster            |
| hk8s    | 1 master, 2 worker        | Calico   | k8s cluster            |
| bk8s    | 1 master, 1 worker        | Flannel  | k8s cluster            |
| wk8s    | 1 master, 2 worker        | Flannel  | k8s cluster            |
| ek8s    | 1 master, 2 worker        | Flannel  | k8s cluster            |
| ik8s    | 1 master, 1 base node        | Loopback | k8s cluster - missing worker node            |

#### Requirement
- Virtualbox
- Vagrant
- Ansible

## Instalation
- Clone Repository
```
git clone https://github.com/zufardhiyaulhaq/kubernetes-cka-lab-provisioning.git
```
- Change variables
```
group_vars/all.yml
```
- Update Instalation
```
python install.py
```
- Start vagrant
```
vagrant up
```
- provision the cluster
```
vagrant provision --provision-with deploy
```

## Result
```
root@management:~# kubectl config get-contexts
CURRENT   NAME   CLUSTER           AUTHINFO                NAMESPACE
          bk8s   kubernetes-bk8s   kubernetes-admin-bk8s   
          ek8s   kubernetes-ek8s   kubernetes-admin-ek8s   
          hk8s   kubernetes-hk8s   kubernetes-admin-hk8s   
          ik8s   kubernetes-ik8s   kubernetes-admin-ik8s   
          k8s    kubernetes-k8s    kubernetes-admin-k8s    
          wk8s   kubernetes-wk8s   kubernetes-admin-wk8s
          
root@management:~# kubectl config use-context k8s
Switched to context "k8s".
root@management:~# kubectl get nodes
NAME             STATUS   ROLES    AGE   VERSION
k8s-master    Ready    master   37m   v1.14.1
k8s-worker0   Ready    <none>   19m   v1.14.1
k8s-worker1   Ready    <none>   19m   v1.14.1

root@management:~# kubectl config use-context ek8s
Switched to context "ek8s".
root@management:~# kubectl get nodes
NAME              STATUS   ROLES    AGE   VERSION
ek8s-master    Ready    master   34m   v1.14.1
ek8s-worker0   Ready    <none>   19m   v1.14.1
ek8s-worker1   Ready    <none>   18m   v1.14.1

root@management:~# kubectl config use-context hk8s
Switched to context "hk8s".
root@management:~# kubectl get nodes
NAME              STATUS   ROLES    AGE   VERSION
hk8s-master    Ready    master   37m   v1.14.1
hk8s-worker0   Ready    <none>   19m   v1.14.1
hk8s-worker1   Ready    <none>   19m   v1.14.1

root@management:~# kubectl config use-context ik8s
Switched to context "ik8s".
root@management:~# kubectl get nodes
NAME             STATUS     ROLES    AGE   VERSION
ik8s-master   NotReady   master   34m   v1.14.1

root@management:~# kubectl config use-context bk8s
Switched to context "bk8s".
root@management:~# kubectl get nodes
NAME              STATUS   ROLES    AGE   VERSION
bk8s-master    Ready    master   36m   v1.14.1
bk8s-worker0   Ready    <none>   19m   v1.14.1

root@management:~# kubectl config use-context wk8s
Switched to context "wk8s".
root@management:~# kubectl get nodes
NAME              STATUS   ROLES    AGE   VERSION
wk8s-master    Ready    master   36m   v1.14.1
wk8s-worker0   Ready    <none>   19m   v1.14.1
wk8s-worker1   Ready    <none>   19m   v1.14.1
```
