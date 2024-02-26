# SAMK AI LAB Webserver LLModel

This readme file provides an overview and instructions for using the webserver application that utilizes a Language Model (LLM) to generate text based on user prompts. The application is built using Flask framework and integrates with the Hugging Face Transformers library for natural language processing tasks.

## Installation and Setup

To set up and run the webserver application, follow these steps:

1. Clone the repository or download the source code files.
2. Install the required dependencies:
    ```bash
    pip install flask transformers torch
    ```
    Versions Used:
    ```
    Flask: 2.0.1
    Transformers: 4.29.0.dev0
    Torch: 2.0.1
    ```
3. Make sure you have a compatible version of Python (3.6 or higher) installed.
4. Obtain the required pre-trained language model by using Hugging Face's model hub. The model name used in the code is `"tiiuae/falcon-7b"`. You can replace this with another model if desired.
5. Make sure you have an internet connection for downloading the model and any additional packages required.
6. Run the following command to start the webserver:
    ```bash
    python app7b.py
    ```
   Please note that it might take around 10 seconds for the webserver to start initially as it loads the language model checkpoints. Subsequent requests will not have this delay.

By default, the webserver will be accessible at http://localhost:8888/.

## Functionality

The webserver application allows users to generate text by entering prompts through a web interface. The entered prompt is then processed by the language model to generate corresponding text.

The application provides two main ways to interact with the webserver:

1. Web Interface: Users can access the web interface by navigating to `http://localhost:8888/` in their web browser. They can enter a prompt in the provided textarea and click the "Generate" button to trigger the text generation process. The generated text will be displayed on the page along with the generation time. The text is displayed token by token using JavaScript to provide a visually appealing and interactive experience.

2. API Endpoint: The application also exposes an API endpoint for programmatic access. Users can make a POST request to `/api/generate` with a JSON payload containing the "input_text" field, which represents the prompt. The API will respond with a JSON object containing the generated text, generation time, and other relevant information.

Please note that the text generation on the web interface is done using JavaScript in conjunction with server-side code. This allows for a smoother and more interactive token-by-token display of the generated text. The JavaScript code retrieves the generated text from the server-side code and sequentially displays the tokens on the webpage.

## Webserver Implementation with Distil Whisper and GPT4ALL Integration

The webserver application utilizes Flask to handle requests and integrates the Distil Whisper model from Hugging Face along with GPT4ALL for text generation based on user prompts. Below is an overview of the implementation:

The application defines a route accessible via both GET and POST requests at the root ("/") URL. 

In the POST section of the code:
- It checks for input text, uploaded files, or JSON data in the request.
- If input text is provided, the server generates additional text based on the input using GPT4ALL.
- If an audio file is uploaded, the server transcribes the audio content using a pre-trained speech recognition model from Distil Whisper, processes the text, generates additional text based on the input, and records relevant information.
- The generated text, along with associated metadata such as model used, input text, generation time, and timestamp, is stored in a list called `generated_texts`. This information is then saved to a JSON file for persistence.

In the GET section of the code:
- It renders an HTML template (`index-whis.html`) to display the user interface.
- If accessed via a GET request, it returns the HTML template to the client for rendering.

This implementation enables users to interact with the webserver through a web interface or programmatically, triggering text generation based on their input prompts. The integration of Distil Whisper for speech recognition and GPT4ALL for text generation enhances the capabilities of the webserver, enabling more versatile and responsive interactions with users.

Please ensure that you have the necessary dependencies installed and configured to run the webserver successfully, as described in the installation and setup instructions provided earlier in this README.

## Parameter Tuning and Text Generation Time

The webserver application allows for parameter tuning to control the text generation process. Specifically, the `top_k` and `max_length` parameters can be adjusted to influence the generated text and the time it takes to generate it.

The `top_k` parameter determines the number of top probable tokens considered during generation. By increasing the value of `top_k`, the generated text is more likely to be composed of higher probability words. Conversely, a lower value of `top_k` allows for more diversity in the generated text but may include less probable words. It is essential to strike a balance between coherence and diversity based on your specific use case.

The `max_length` parameter sets an upper limit on the length of the generated text. Increasing the value of `max_length` can result in longer generated texts, but it may also require more time for generation.

To analyze the impact of different parameter settings on text generation time, multiple runs were conducted with varying values of `top_k` and `max_length`. The approximate time taken for each setting was recorded and analyzed. The provided **Falcon- parameters test.csv** file contains the results of these experiments, highlighting the relationship between the parameters and the corresponding generation times. It demonstrates a pattern where higher values of `top_k` and `max_length` tend to increase the generation time.

Feel free to experiment with different parameter values based on your requirements, striking a balance between the desired quality, length, and generation time of the text.

## File Structure

The webserver application consists of the following files:

- `app7b.py`: This is the main Flask application file that handles web requests and integrates with the language model.
- `index7b.html`: This HTML template file defines the structure and layout of the web interface.
- `generated_texts.json`: This JSON file stores the generated texts along with relevant metadata, such as the model name, input prompt, and generation timestamp.

## Customization

If you wish to customize the application, you can modify the following aspects:

- **Model Selection**: To use a different language model, change the `model_name` variable in `app7b.py` to the desired model name.
- **Generation Parameters**: Adjust the generation parameters in the `generate_text` function to control the length and quality of the generated text. Parameters such as `max_length`, `do_sample`, `top_k`, and `num_return_sequences` can be modified based on your requirements.

Please note that the generation times mentioned in the CSV file are approximate and may vary depending on the system's hardware specifications, network conditions, and other environmental factors.

## Data Persistence

The generated texts are stored in the `generated_texts.json` file, which allows for persistent storage across application restarts. The `load_generated_texts` and `save_generated_texts` functions handle the loading and saving of generated texts from and to the file, respectively. This ensures that previously generated texts are not lost when the application restarts.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Hugging Face for providing access to the Transformers library and pre-trained language models.
- The Python and Flask communities for their valuable contributions to open-source software development.

