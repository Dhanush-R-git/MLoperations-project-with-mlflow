# Wine quality analysis and prediction
This project involves building a machine learning model "Elasticnet" to predict the quality of wine based on various chemical properties. The dataset used includes features such as acidity, sugar content, pH level, and alcohol content. The goal is to provide an accurate prediction of wine quality on a scale from 0 to 10.
## End to End MLoperations project with mlflow
This project involves Machine Learning Operations (mlops) building an end to end application i.e from development to deployment. The tools used are 
1. MLflow - used for experiment tracking [Docs](https://mlflow.org/docs/latest/index.html)
2. DagsHub - manage your trained models from the full-fledged MLflow UI built into your DagsHub project.
3. Docker - used to containerization
4. Azure web app - used to deploy the application 
## Project Folder structure
```bash
wine_quality_prediction_system(model developing-to-deployment)/
|
├── environment(python or conda)
|   ├── ml.env.20.6.24
|
├── project template.py
|
├── requirements.txt
|
├── research(.ipynb files)/                    
│   ├── i) data ingestion
│   ├── ii) data validation
│   ├── iii) data transformation
|   ├── iv) model trainer
|   ├── v) model evaluation
|   ├── vi) trails
|
│── sorurce/MLproject            
│   ├── components(.py files)/
|   |   ├── data ingestion
│   |   ├── data validation
│   |   ├── data transformation
|   |   ├── model trainer
|   |   ├── model evaluation
|   |
│   ├── config/
|   |   ├── configuration.py # Manages configuration settings for the project by reading from YAML files and creating necessary directories
|   |
│   ├── constants/(path constants) # yaml file path constants
|   |
|   ├── entity/(.py files) 
|   |   ├── configuration_entity # store configuration settings [config.yaml] file for the components & pipeline process in a structured way
|   |
|   ├── pipelines/(.py files)
|   |   ├── stage1 Data Ingestion
│   |   ├── stage2 Data Validation
│   |   ├── stage3 Data Transformation
|   |   ├── stage4 Model Trainer
|   |   ├── stage5 Model Evaluation
|   |   ├── Prediction pipeline
|   |
|   ├── utils/(.py files)
|   |   ├──common
|
├── yaml files
|   ├── config/config.yaml # artifacts & data sources path
|   ├── params.yaml # model parameters
|   ├── schema.yaml # dataset schema, columns & target
|
├── static/
|   ├── assets
|   ├── css
|   ├── js
|
│── templates/                 
│   ├── index.html
│   ├── results.html
│
├── setup.py
|
├── main.py
|
├── web_app.py
│
├── test.py
|
├── Dockerfile
|
│── logs/
│   ├── stores all running logs
|              
│── README.md                 

```

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py
## How to run?

Clone the repository

```bash
https://github.com/Dhanush-R-git/MLoperations-project-with-mlflow
```
### Create a conda environment after opening the repository

```bash
conda create -n ml.env.0.0.0 python=3.11.7 -y
```

```bash
conda activate ml.env.0.0.0
```

### install the requirements
```bash
pip install -r requirements.txt
```

### run app.py
```bash
python app.py
```

Now,
```bash
open up you local host and port
```

## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)

##### cmd
- mlflow ui

## dagshub
[dagshub](https://dagshub.com/)


MLFLOW_TRACKING_URI=https://dagshub.com/user-name/MLoperations-project-with-mlflow.mlflow \
MLFLOW_TRACKING_USERNAME= user-name \
MLFLOW_TRACKING_PASSWORD= xxxxxxxxxxx \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/user-name/MLoperations-project-with-mlflow.mlflow 
or
$env:MLFLOW_TRACKING_URI = "https://dagshub.com/user-name/MLoperations-project-with-mlflow.mlflow"

export MLFLOW_TRACKING_USERNAME=user-name
or
$env:MLFLOW_TRACKING_USERNAME="user-name"

export MLFLOW_TRACKING_PASSWORD=xxxxxxxxxxxx
or
$env:MLFLOW_TRACKING_PASSWORD="xxxxxxxxxxxxx"

```
To verify

```bash

echo $env:MLFLOW_TRACKING_URI
echo $env:MLFLOW_TRACKING_USERNAME
echo $env:MLFLOW_TRACKING_PASSWORD

```

## AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.ap-south-1.amazonaws.com/mlproj

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
## 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


## 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app

## About MLflow 
MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model

