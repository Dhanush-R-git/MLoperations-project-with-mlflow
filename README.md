# mlops-project-with-mlflow

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



# How to run?

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

[Documentation]-->(https://mlflow.org/docs/latest/index.html)

##### cmd
- mlflow ui

### dagshub
[dagshub]-->(https://dagshub.com/)


MLFLOW_TRACKING_URI=https://dagshub.com/Dhanush-R5/mlops-project-with-mlflow.mlflow \
MLFLOW_TRACKING_USERNAME= Dhanush-R5 \
MLFLOW_TRACKING_PASSWORD= PfpmJcTM5DJS7@9 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/Dhanush-R5/mlops-project-with-mlflow.mlflow 
or
$env:MLFLOW_TRACKING_URI = "https://dagshub.com/Dhanush-R5/mlops-project-with-mlflow.mlflow"

export MLFLOW_TRACKING_USERNAME=Dhanush-R5
or
$env:MLFLOW_TRACKING_USERNAME="Dhanush-R5"

export MLFLOW_TRACKING_PASSWORD=PfpmJcTM5DJS7@9
or
$env:MLFLOW_TRACKING_PASSWORD="PfpmJcTM5DJS7@9"

```
To verify

```bash

echo $env:MLFLOW_TRACKING_URI
echo $env:MLFLOW_TRACKING_USERNAME
echo $env:MLFLOW_TRACKING_PASSWORD

```


