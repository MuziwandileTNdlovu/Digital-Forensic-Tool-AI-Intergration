#!/bin/bash

# Update package list
sudo apt-get update

# Install build-essential and python3-dev
sudo apt-get install -y build-essential python3-dev

# Install PortAudio development libraries
sudo apt-get install -y portaudio19-dev

sudo apt-get install wkhtmltopdf

# Upgrade pip, setuptools, and wheel
pip install --upgrade pip setuptools wheel

# Install packages from requirements.txt
pip install -r requirements.txt