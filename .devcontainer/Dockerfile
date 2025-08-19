FROM mcr.microsoft.com/devcontainers/base:ubuntu-22.04

# Install system dependencies (match Virtualmin's typical setup)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    python3-dev \
    mariadb-client \
    && rm -rf /var/lib/apt/lists/*
