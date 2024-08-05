# Hyle teeML Setup

## Pre-requisites
### Install Docker
To install visit the Docker [website](https://www.docker.com/).

## Build the Enclave Builder image
Run these commands in the `/hyle-teeML-setup` directory.
```bash!
docker build -t enclave .
```
## Run the docker container
```
docker run -it --privileged -v `pwd`:/app/mount enclave
```

This will generate the enclave image `.eif` file in the `/enclave` folder.

# ML Model
The model used is XGBoost as done here: https://github.com/Hyle-org/onnx_cairo