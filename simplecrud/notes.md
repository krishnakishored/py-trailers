## To run an application in a Kubernetes cluster

, you typically need a set of manifest files. Here's a basic set of manifest files you might need:

1. `deployment.yaml`: This file describes the desired state for your application Deployment. It defines a set of pods running the same application on your cluster.

2. `service.yaml`: This file exposes the Deployment as a network service, potentially making it accessible outside of your cluster.

3. `configmap.yaml`: This file allows you to separate your application code from your configuration. In this case, it could be used to set the `PORT` environment variable.

4. `secret.yaml`: This file allows you to store and manage sensitive information, such as passwords, OAuth tokens, and ssh keys.

Also, replace the secret data in `secret.yaml` with your actual secret data, base64 encoded.

##  To point your shell to minikube's docker-daemon, run:
-  $ eval $(minikube -p minikube docker-env)
