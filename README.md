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
NAME          STATUS   ROLES    AGE   VERSION
k8s-master    Ready    master   22m   v1.18.0
k8s-worker1   Ready    <none>   20m   v1.18.0
k8s-worker2   Ready    <none>   19m   v1.18.0

root@management:~# kubectl config use-context ek8s
Switched to context "ek8s".
root@management:~# kubectl get nodes
NAME           STATUS   ROLES    AGE     VERSION
ek8s-master    Ready    master   8m17s   v1.18.0
ek8s-worker1   Ready    <none>   7m7s    v1.18.0
ek8s-worker2   Ready    <none>   6m5s    v1.18.0

root@management:~# kubectl config use-context hk8s
Switched to context "hk8s".
root@management:~# kubectl get nodes
NAME           STATUS   ROLES    AGE   VERSION
hk8s-master    Ready    master   18m   v1.18.0
hk8s-worker1   Ready    <none>   17m   v1.18.0
hk8s-worker2   Ready    <none>   16m   v1.18.0

root@management:~# kubectl config use-context ik8s
Switched to context "ik8s".
root@management:~# kubectl get nodes
NAME          STATUS     ROLES    AGE     VERSION
ik8s-master   NotReady   master   4m54s   v1.18.0
root@management:~# kubectl config use-context bk8s
Switched to context "bk8s".
root@management:~# kubectl get nodes
NAME           STATUS   ROLES    AGE   VERSION
bk8s-master    Ready    master   15m   v1.18.0
bk8s-worker1   Ready    <none>   14m   v1.18.0

root@management:~# kubectl config use-context wk8s
Switched to context "wk8s".
root@management:~# kubectl get nodes
NAME           STATUS   ROLES    AGE   VERSION
wk8s-master    Ready    master   12m   v1.18.0
wk8s-worker1   Ready    <none>   11m   v1.18.0
wk8s-worker2   Ready    <none>   10m   v1.18.0
```

## Management Node
Adding some plugin and auto-complete kubectl in the installation
- kubectl completion
- kubectl krew
- kube-ps1

install some plugin
```
curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash
curl -L https://istio.io/downloadIstio | sh -

kubectl krew install ctx
kubectl krew install ns
```

