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

To configure Pepper for seamless interaction with the server, ensure you have all the required Pepper dependencies, such as NAOqi. Follow these steps:
Here's the combined Pepper configuration section with the steps for integrating web server interaction and setting up Paramiko:

1. **Install NAOqi SDK**: Download and install the NAOqi SDK provided by SoftBank Robotics. Ensure that the SDK version is compatible with your Pepper robot.

2. **Set Up Connection**: Establish a connection to Pepper's robot by specifying the IP address and port number. Use the appropriate connection method supported by the NAOqi SDK.

3. **Load Necessary Modules**: Load the necessary NAOqi modules for speech recognition, audio recording, and text-to-speech functionalities. These modules are essential for Pepper's communication capabilities.

4. **Integrate Web Server Interaction with Paramiko**:

   a. **Ensure Necessary Pepper Dependencies**:
      Make sure Pepper's dependencies, such as NAOqi, are installed and configured correctly.

   b. **Install Paramiko**:
      Install Paramiko in your Python environment. You can install it using pip:
      ```bash
      pip install paramiko
      ```

   c. **Set Up SSH Connection**:
      Use Paramiko to establish an SSH connection from Pepper's code to the web server. Provide the IP address, port number, username, and password (or SSH key) of the server.

   d. **Send Requests**:
      Once the SSH connection is established, send requests to the web server using Paramiko's SSH client. These requests may include user prompts or recorded audio data for processing by the server.

   e. **Receive Responses**:
      After sending a request, wait for the response from the web server. Paramiko provides methods to receive data from the server once it's available. This response will typically contain the generated text or any other relevant information.

   f. **Process Responses**:
      Once the response is received, process it as needed within Pepper's code. This may involve displaying the generated text, speaking it aloud using Pepper's text-to-speech capabilities, or taking other actions based on the response.

   g. **Handle Errors**:
      Implement error-handling mechanisms in case of connection issues, timeouts, or other potential problems when communicating with the web server via Paramiko.

Pepper's configuration for interaction with the web server is managed by `pepper_python2_code.py`, a Python 2 compatible file. Ensure this file is located in the same folder as Pepper's SDK for proper execution.

### Usage

To run the entire program, follow these steps:

1. **Start the Web Server**:
   - Ensure that the web server application, `webserver_Flask_Code.py`, is running.
   - Navigate to the directory containing `webserver_Flask_Code.py` in your terminal or command prompt.
   - Run the following command to start the web server:
     ```bash
     python webserver_Flask_Code.py
     ```
   - Keep the web server running throughout the interaction with Pepper.

2. **Run the Pepper Python 2 Code**:
   - Once the web server is running, you can execute the Pepper interaction code, `pepper_python2_code.py`.
   - Ensure that Pepper's dependencies, such as NAOqi, are properly installed and configured.
   - Run the `pepper_python2_code.py` script on Pepper's platform. This script will establish a connection with the web server and interact with it to generate text based on user prompts or recorded audio.
   - Follow any additional instructions prompted by the Pepper Python 2 code to initiate interactions.

By following these steps, you can successfully run the entire program, enabling communication between the web server and Pepper for text generation, speech recognition, and interaction.

Remember to keep the web server running while interacting with Pepper to ensure seamless communication and functionality.

## Evaluation

Qualitative assessments and quantitative analyses of response time and performance metrics are conducted to identify the most optimal LLM and ASR for Pepper's communication needs.

---

### License

This project is licensed under the terms of the MIT license.

```
MIT License

Copyright (c) [2024] [Raneem Abdel Hafez]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
``` 

This README file provides a comprehensive overview of the methodology, setup instructions for the web server, and configuration guidelines for Pepper. Feel free to reach out if you have any questions or need further assistance.
