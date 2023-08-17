# deploying_in_EkS
<summary>
Welcome to the Projects Memory System Utilization Project repository! 
This project focuses on optimizing memory system utilization using Docker, Amazon Elastic Container Registry (ECR), and
Amazon Elastic Kubernetes Service (EKS). In today's dynamic computing landscape, efficient resource management is paramount, and 
that's where our project comes in. By harnessing the power of Docker containers, we encapsulate applications and their dependencies, ensuring consistency across various environments. 
The Docker images are seamlessly pushed to Amazon ECR, providing a secure and scalable container image registry.
Leveraging the capabilities of Amazon EKS, we achieve efficient orchestration and deployment of these containers into a Kubernetes cluster. 
This repository serves as a comprehensive guide, offering step-by-step instructions, configuration templates, and 
best practices for achieving optimal memory utilization while streamlining the deployment process. Whether you're a seasoned DevOps professional or
just stepping into the world of containerization and orchestration, this project will provide valuable insights and hands-on experience. 
Join us on this journey towards mastering memory-efficient system utilization with Docker, ECR, and EKS
</summary>

## 🛠 Skills
Basic knowlegde of Docker, AWS, ECR,EKS,python ...

## **Projects Memory System Utilization Project**

Welcome to the Projects Memory System Utilization Project repository! 

## Step 1: Clone the Repository

```http
git clone https://github.com/your-username/your-repo.git
```

```http
cd your-repo
```

## **Step 2: Dockerize Your Application**

Containerization is key to achieving consistent application behavior across different environments.
Dockerize your application by creating a Dockerfile in your project's root directory. Define the required dependencies, configurations, and runtime environment.

## **Step 3: Build and Test Locally**

Build your Docker image locally to ensure everything is working as expected. Run the following commands:
#### Docker Commands

```http
   docker build -t my-app .
```
```http
  docker run -d -p 8080:80 my-app
```

## **Step 4: Push Image to Amazon ECR**

Amazon ECR provides a secure and scalable container image registry. Push your Docker image to ECR for easy deployment later:

```http
aws ecr create-repository --repository-name my-app-repo
```
```http
docker tag my-app:latest <your-account-id>.dkr.ecr.<your-region>.amazonaws.com/my-app-repo:latest
```
```http
docker push <your-account-id>.dkr.ecr.<your-region>.amazonaws.com/my-app-repo:latest
```

## **Step 5: Set Up Amazon EKS Cluster**

Amazon EKS simplifies Kubernetes cluster management. Create an EKS cluster through the AWS Management Console or using the AWS CLI.
Utilize Kubernetes manifests to define how your application should run in the cluster. Create deployment and service boto3 files, specifying the Docker image from ECR and any required configurations.


## Documentation

[Documentation] ([https://linktodocumentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)


## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https:linkedin.com/in/thanikai-chandran-400486227)


## 🚀 About Me
I'm a Cloud and devops Engineer...

