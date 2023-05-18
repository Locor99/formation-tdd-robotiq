FROM ubuntu:18.04

# Install awscli while dodging the interactive steps for tzdata's installation
RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get update && apt-get install -y -q --no-install-recommends \
    python3 \
    python3-pip \
    python3-setuptools \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
