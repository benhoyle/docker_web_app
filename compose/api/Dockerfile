# Docker file to get spacy and pytorch playing nicely with GPU

# Get Ubuntu server image - CUDA version needs to be lower than the local CUDA version
FROM nvidia/cuda:11.4.0-cudnn8-runtime-ubuntu20.04

# Set time zone parameters for tzdata
ARG DEBIAN_FRONTEND="noninteractive"
ENV TZ="Europe/London"

# Update & install an ssh client
RUN apt-get update
RUN apt-get install --yes --no-install-recommends \
    openssh-client \
    git \
    wget \
    ca-certificates \
    python3.9 \
    python3.9-dev \
    python3.9-distutils \
    python3.9-venv \
    build-essential
RUN apt-get clean

# Create virtual environment so we use the right pip etc
RUN python3.9 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip3 --version

# Install pip and python tools
RUN pip3 install -U pip setuptools wheel

# ----- Things to get the GPU support working properly ----

# Install Pytorch separately to avoid an issue with GPU - use CUDA 11.3 to keep below host installed 11.4
RUN pip3 install torch==1.12.1+cu113 torchvision==0.13.1+cu113  \
    \ torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113

# Install Spacy - Specify a CUDA version that matches the docker image
RUN pip3 install spacy[cuda113] \
    && python3.9 -m spacy download en_core_web_trf

# ----- End of GPU support things ----

# Set working directory
WORKDIR /nlp_app

# Install remaining requirements
COPY requirements_for_docker.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install other files
COPY . .

# Run tests to check everything passes before spinning up
RUN pytest
