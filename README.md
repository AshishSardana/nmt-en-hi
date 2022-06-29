## Description
This repository contains code for building an End-to-End solution for training and deploying English-Hindi machine translation models.

## Organisation of the repository
* `./code` contains code for the EDA, Training, Inference and Deployment.
* `./nmt_grpc_service` contains routines and instructions to setup the ASR and NMT services.
* `./nmt_webapp` contains routines and instructions to launch and use the NMT web application.

## Installation 
*Note: The following instructions have been tested on a DGX-Station with NVIDIA V100 and A100 GPU's.*

For the most part, this repository relies on NVIDIA [NeMo](https://github.com/NVIDIA/NeMo) for training, testing and validating models. NeMo inturn uses [PyTorch Lightning](https://www.pytorchlightning.ai/).

For the server and webapp, follow the `ReadME.md` file in `./server` and `./webapp` respectively. For all the other routines, use the NeMo docker image and run the cells at the top of the notebook to install the libraries using `pip`.
