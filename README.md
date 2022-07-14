## Description
This repository contains code for building an End-to-End solution for training and deploying English-Hindi machine translation model.

## Structure
1. `eda` contains code for exploratory data analysis and data preparation. 
2. `training` contains the code for training the transformer based NMT model.
3. `inference` contains the code for generating predictions and calculating BLEU scores on test datasets.
4. `nmt_grpc_service` contains the routines and instructions to setup NMT server.
5. `nmt_webapp` contains the routines and instructions to launch a simple NMT web application which queries the NMT service.

## Pre-requisites
