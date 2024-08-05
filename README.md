# Hyle teeML Setup

## Pre-requisites
### Install Docker
To install visit the Docker [website](https://www.docker.com/).

# CPU Architecture
This setup is for [`amd64` architecture](https://https://en.wikipedia.org/wiki/X86-64). If you want to setup on a arm-based machine then change `amd64` to `arm64` at all the places.

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