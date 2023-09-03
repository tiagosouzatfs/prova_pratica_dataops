#!/bin/bash

curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64

sudo install minikube-linux-amd64 /usr/local/bin/minikube

#como eu não sei qual máquina será a execução desse script com relação aos recursos, então 
#vou iniciar o minikube com 1, apenas o Master Node
minikube start
#minikube start --nodes 3 -p k8sCluster

#minikube kubectl -- get nodes

#kubectl label node <node_name> node-role.kubernetes.io/worker=worker

#minikube status

#minikube kubectl --help

#alias kubectl="minikube kubectl --"

echo 'alias kubectl="minikube kubectl --"' >> /home/$USER/.bashrc

kubectl get nodes

source /home/$USER/.bashrc

#minikube dashboard

#minikube stop

curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3

chmod 700 get_helm.sh

./get_helm.sh

#helm search hub apache-airflow

helm repo add apache-airflow https://airflow.apache.org

#helm search repo apache-airflow

kubectl apply -f namespace_pv_pvc_airflow.yaml

#mkdir dags
#mkdir logs
#mkdir data

#Temos que iniciar por fora, pq ocupa um terminal por comando
#minikube mount ./dags/:/data/dags
#minikube mount ./data/:/data/data
#minikube mount ./logs/:/data/logs

#minikube ssh

#ll /data/dags

#exit

eval $(minikube -p minikube docker-env)

docker build -t airflow .

helm upgrade --install airflow apache-airflow/airflow --namespace airflow -f k8s_executor_airflow_config.yaml

kubectl port-forward svc/airflow-webserver 8080:8080 --namespace airflow

minikube kubectl -- port-forward svc/airflow-webserver 8080:8080 --namespace airflow