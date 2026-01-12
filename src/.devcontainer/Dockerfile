FROM mcr.microsoft.com/devcontainers/python:3.11

# Set working directory
WORKDIR /workspace

# Upgrade pip
RUN pip install --upgrade pip

# Install useful tooling
RUN apt-get update && apt-get install -y \
    git \
    curl \
    openssh-client \
    && rm -rf /var/lib/apt/lists/*
