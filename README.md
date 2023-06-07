# Python OpenTelemetry Auto Instrumentation
This is a Python application with two different application. One will be deployed as an Upstream application and another will be deployed as Downstream application.
There will be a call from Upstream application to Downstream.
We will also have deployment files so you can deploy it directly to Kubernetes.
Follow these steps to deploy and access the Application.

```
git clone https://github.com/mithun100/python-upstream-downstream.git
```
```
cd deploy 
```

To deploy all manifest in the Kubernetes
```
./deploy_kubernetes.sh
```
To undeploy all the manifest from the Kuberenetes 

```
./undeploy_kubernetes.sh

```
If you have already have the All the necessary AppDynamics Kuberenetes deploy then you may expect to see the data in the AppD Cloud https://docs.appdynamics.com/appd-cloud/en 


