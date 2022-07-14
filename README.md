## Description
This repository contains code for building an End-to-End solution for training and deploying English-Hindi machine translation model.

## Structure
1. `eda` contains code for exploratory data analysis and data preparation. 
2. `training` contains the code for training the transformer based NMT model.
3. `inference` contains the code for generating predictions and calculating BLEU scores on test datasets.
4. `nmt_grpc_service` contains the routines and instructions to setup NMT server.
5. `nmt_webapp` contains the routines and instructions to launch a simple NMT web application which queries the NMT service.

## Pre-requisites

1. NVIDIA GPU - SM 7+
2. Docker

## Requirements

This repository can be executed in the NVIDIA NeMo 22.04 Docker container. The Docker image for NeMo 1.8.0 is `nvcr.io/nvidia/nemo:22.04`<br>
You can also install [NVIDIA NeMo](https://github.com/NVIDIA/NeMo#installation) using pip.

For the most part, this repository relies on NVIDIA NeMo for training and testing the models. The libraries for tokenization (IndicNLP, iNLTK), EDA (seaborn, wordcloud) and deployment (grpc, flask) are installed as and when needed.

## Setup

1. Clone this repository <br>
`git clone https://github.com/AshishSardana/nmt-en-hi` <br>
`cd nmt-en-hi`

2. Run the Docker container <br>
`docker run -it --rm --gpus "all" --net=host -v /path/to/this/repo:/workspace/translation nvcr.io/nvidia/nemo:22.04`

    Make sure to specify the change the `/path/to/this/repo`.

3. Inside the container, change the directory and start the jupyter server <br>
`cd /workspace/translation` <br>
`jupyter lab --allow-root --port 8888 --NotebookApp.token='' --ip 0.0.0.0`

    If you have a browser installed on your machine, the notebook should automatically open. If you do not have a browser, copy/paste the URL from the command.

4. Follow the instructions in each of the sub-directories in the following order: <br>
`eda` -> `training` -> `inference` -> `nmt_grpc_service` -> `nmt_webapp`