# Digital Forensics Analysis Tool

This tool is designed to perform digital forensics analysis on audio files. It transcribes audio, performs sentiment analysis, identifies speakers, and extracts keywords. The results are compiled into a comprehensive report in PDF format.

## Prerequisites

- Python 3.x
- `pip` (Python package installer)

## Setup

### Automated Setup

You can run the provided `setup.sh` script to automatically install all required packages and dependencies:

```bash
#!/bin/bash

# Update package list
sudo apt-get update

# Install build-essential and python3-dev
sudo apt-get install -y build-essential python3-dev

# Install PortAudio development libraries
sudo apt-get install -y portaudio19-dev

# Install wkhtmltopdf
sudo apt-get install wkhtmltopdf

# Upgrade pip, setuptools, and wheel
pip install --upgrade pip setuptools wheel

# Install packages from requirements.txt
pip install -r requirements.txt
```

# Project Structure
The project has the following structure:
```
.
├── audiofiles/          # Folder for storing audio files to be analyzed
├── main.py              # Main script to run the application
├── requirements.txt     # Python dependencies for the project
├── reports/             # Folder where generated PDF reports are saved
└── secrets/             # Folder for storing secret keys or configuration

```
# Example
Here's an example command to analyze an audio file named example.wav located in the audiofiles directory:
```
- python3 main.py audiofiles/example.wav
```
