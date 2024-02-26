# Integration of Language Models with Pepper Robot

This README file provides comprehensive information about the integration of Language Models (LMs) with the Pepper robot, outlining the experimental design and setup process. The integration aims to facilitate seamless interaction between users and the Pepper robot through the establishment of a web server and configuration of the robot.

## Experimental Design

The integration process unfolds in two primary phases:

### 1. Setting up the Server

#### 1.1 Setting up the Web Server

The initial phase involves the development of a web server to enable communication between the language models and the Pepper robot. Flask, a lightweight micro-framework for Python, is chosen for its flexibility and minimalistic design. Flask's support for creating RESTful APIs enhances its suitability for client-server communication.

The web server serves as a crucial component for establishing efficient communication exchange between the server and the Pepper robot. It facilitates seamless interaction and response generation. The selection of GP4ALL as the preferred LLM is based on its cost-effectiveness, delivery of high-quality responses, and efficient performance. Integration with the Whisper ASR model further enhances the server's capabilities, ensuring smooth interaction between users and the Pepper robot.

**Note:** Refer to the provided `requirements.txt` for installing the necessary dependencies.

### 2. Setting up Pepper Robot

The second phase involves configuring the Pepper robot to seamlessly interact with the web server. Initial steps include downloading the required software and installing essential software development kits (SDKs) and modules. Visual Studio Code with Python 2.7 is utilized for coding purposes.

Integration with the web server is a pivotal aspect of the experimental design, enabling Pepper's seamless connection to the server. Python 2.7, along with the request library, aligns perfectly with the compatibility requirements of Pepper's NAOqi extension modules.

As the experiment progresses, attention is directed towards Pepper’s speech recognition module, revealing its limitations. This necessitates the integration of an ASR model, influencing the integration strategy accordingly.

## Installation

To install the required dependencies for the integration process, follow these steps:

1. Install Flask, Whisper, GP4ALL, and other dependencies using pip:

    ```
    pip install flask==2.0.1
    pip install openai-whisper gpt4all
    ```

2. Additionally, ensure you have the necessary system dependencies such as `ffmpeg`:

    ```
    sudo apt-get update
    sudo apt-get install ffmpeg
    ```

3. Upgrade and install any required Python packages:

    ```
    pip install transformers --upgrade
    pip install packaging
    pip uninstall -y ninja && pip install ninja
    ```

4. Install the required packages for Flash Attention:

    ```
    pip install flash-attn --no-build-isolation
    ```

5. Ensure you have the latest version of `pip`:

    ```
    pip install --upgrade pip
    ```

6. Finally, install `transformers`, `accelerate`, and `optimum`:

    ```
    pip install --upgrade transformers accelerate optimum
    ```

## Conclusion

This experimental design provides a comprehensive roadmap for integrating language models with the Pepper robot, emphasizing the importance of establishing a robust communication framework and configuring Pepper's software components accordingly. By following the outlined steps, users can effectively set up the integration environment and facilitate seamless interaction between users and the Pepper robot.

For further details and code implementations, please refer to the repository files.
