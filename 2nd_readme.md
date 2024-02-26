# Pepper Language Model and ASR Integration

This README file provides an overview of the methodology involving the integration of Language Models (LLMs) into Pepper's architecture, alongside Automatic Speech Recognition (ASR) for accurate speech recognition. Through the utilization of ASR and evaluation of various LLMs, Pepper demonstrates commendable transcription capabilities and generates responses that are deemed sufficiently human-like for users to understand and engage with. Evaluation of the implemented models reveals notable differences in speed, with some models exhibiting faster response times than others.

## Methodology Overview

The integration methodology consists of two primary phases:

1. **Establishing Web Server Infrastructure**: This phase involves setting up a web server infrastructure to facilitate communication between Pepper and the language model server. Python code in `webserver_Flask_Code.py` handles the web server functionality, providing an interface for users to interact with Pepper and trigger text generation.

2. **Configuring Pepper for Interaction**: Pepper is configured to seamlessly interact with the web server. Python 2 code in `pepper_python2_code.py` is compatible with Pepper's SDK and needs to be located in the same folder as the Pepper SDK for proper execution.

## Web Server Setup (Python 3)

To set up and run the web server application, follow these steps:

1. Clone the repository or download the source code files.
2. Install the required dependencies:
   ```bash
   pip install flask==2.0.1 transformers==4.29.0.dev0 torch==2.0.1
   ```
   Versions Used:
   ```bash
   Flask: 2.0.1
   Transformers: 4.29.0.dev0
   Torch: 2.0.1
   ```
   
   ```bash
   pip install gpt4all
   pip install flask==2.0.1
   pip install -U openai-whisper pip install openai
   ```
   
   ```bash
   sudo apt-get update
   sudo apt-get install ffmpeg
   pip install transformers --upgrade
   ```
   
   For Flash Attention:
   ```bash
   git clone https://github.com/Dao-AILab/flash-attention
   cd flash-attention
   pip install -r requirements.txt
   ```
   
   ```bash
   pip install packaging ninja
   pip uninstall -y ninja && pip install ninja
   ```
   
   ```bash
   sudo apt-get install git
   pip install flash-attn --no-build-isolation
   ```
   
   ```bash
   pip install --upgrade pip
   pip install --upgrade transformers accelerate optimum
   ```

These commands will install the necessary dependencies and ensure that the specified versions of Flask, Transformers, and Torch are used. Additionally, it updates packages and installs required system dependencies like ffmpeg. Finally, it upgrades pip and installs additional packages required for optimization.

3. Make sure you have a compatible version of Python (3.6 or higher) installed.
4. Obtain the required pre-trained language model from the Hugging Face model hub. The model name used in the code is "gpt4all-falcon-q4_0.gguf". You can replace this with another model if desired.
5. Make sure you have an internet connection for downloading the model and any additional packages required.
6. Run the following command to start the web server:
   ```bash
   python webserver_Flask_Code.py
   ```
   The web server will be accessible at http://localhost:8888/ by default.

## Pepper Configuration (Python 2)

Pepper's configuration for interaction with the web server is managed by `pepper_python2_code.py`, a Python 2 compatible file. Ensure this file is located in the same folder as Pepper's SDK for proper execution.

## Evaluation

Qualitative assessments and quantitative analyses of response time and performance metrics are conducted to identify the most optimal LLM and ASR for Pepper's communication needs.

---

This README file provides a comprehensive overview of the methodology, setup instructions for the web server, and configuration guidelines for Pepper. Feel free to reach out if you have any questions or need further assistance.
