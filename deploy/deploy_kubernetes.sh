#!/bin/bash

# Deploy the downstream application
echo "Deploying downstream application..."
kubectl apply -f downstream-deployment.yaml
kubectl apply -f downstream-service.yaml

# Deploy the upstream application
echo "Deploying upstream application..."
kubectl apply -f upstream-deployment.yaml
kubectl apply -f upstream-service.yaml

echo "Deployment completed!"

