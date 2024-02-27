# USES DISTIL WHISPER from hugging face and GPT4ALL for pepper requests route 

from flask import Flask, render_template, request, jsonify
from gpt4all import GPT4All  
import time
import json
from datetime import datetime
import pytz
import whisper
import os
import GPUtil
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import time

app = Flask(__name__)

model_name = "gpt4all-falcon-q4_0.gguf"
port_num = 8888
max_token_num = 100
say = whisper.load_model("base")

# Create an empty list to store the generated texts
generated_texts = []

def load_generated_texts():
    try:
        with open('generated_texts.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_generated_texts():
    with open('generated_texts.json', 'w') as file:
        json.dump(generated_texts, file, indent=4)

def generate_text(input_text):
    model = GPT4All(model_name)  # Initialize the GPT4All model
    start_time = time.time()  # Start measuring the time
    output = model.generate(input_text, max_tokens=max_token_num)  # Generate text
    end_time = time.time()  # End measuring the time
    generated_time = end_time - start_time  # Calculate the generation time

    generated_text = [output]
    generated_text = output.split() # to generate word by word
    generated_text1 = output  # Get the generated text as a string

    return generated_text, generated_time, generated_text1  # Return the generated text and generation time

@app.before_first_request
def setup():
    global generated_texts
    generated_texts = load_generated_texts()


@app.route('/', methods=['GET', 'POST'])
def combined_route():
    transcribed_text = None
    transcription_time = 0

    if request.method == 'POST':
        if 'input_text' in request.form:
            input_text = request.form['input_text']
            print("form")
        elif 'file' in request.files:
            # If a file is uploaded, transcribe it and use the text
            file = request.files['file']
            if file.filename != '':
                start_transcription_time = time.time()

                # Save the uploaded audio file to a temporary location
                temp_audio_path = "temp_audio.mp3"
                file.save(temp_audio_path)
                
                device = "cuda:0" if torch.cuda.is_available() else "cpu"
                torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
                model_id = "distil-whisper/distil-large-v2"

                model = AutoModelForSpeechSeq2Seq.from_pretrained(
                    model_id,
                    torch_dtype=torch_dtype,
                    low_cpu_mem_usage=True,
                    use_safetensors=True,
                    use_flash_attention_2=True,
                )
                model.to(device)

                processor = AutoProcessor.from_pretrained(model_id)

                transcribed_text = pipeline(
                    "automatic-speech-recognition",
                    model=model,
                    tokenizer=processor.tokenizer,
                    feature_extractor=processor.feature_extractor,
                    max_new_tokens=128,
                    chunk_length_s=15,
                    batch_size=16,
                    torch_dtype=torch_dtype,
                    device=device,
                )
                result = transcribed_text(temp_audio_path)
                transcribed_text = result["text"]
                end_transcription_time = time.time()
                transcription_time = end_transcription_time - start_transcription_time
                os.remove(temp_audio_path)
                input_text = transcribed_text

                generated_text, generated_time, generated_text1 = generate_text(input_text)
            else:
                return "No selected file"
        else:
            input_text = request.json['input_text']
            print("json")

        generated_text, generated_time, generated_text1 = generate_text(input_text)

        input_text = input_text.lstrip()
        local_tz = pytz.timezone('Europe/Helsinki')
        text_entry = {
            'model': model_name,
            'input_text': input_text,
            'generated_text': generated_text1,
            'generatedAt': datetime.now(tz=local_tz).isoformat(),
            'generatedTime': generated_time,
        }
        generated_texts.append(text_entry)
        save_generated_texts()

        if request.content_type == 'application/json':
            return jsonify(text_entry), 200
        else:
            return render_template('index-whis.html', transcribed_text=transcribed_text,
                                   generated_text=generated_text, generated_time=generated_time,
                                   transcription_time=transcription_time)

    return render_template('index-whis.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port_num)


"""
This code defines a route in a web application using Flask. The route is accessed via both GET and POST requests to the root ("/") URL. 

In the POST section, the code checks whether the request contains input text, a file, or JSON data. If input text is provided, it prints "form"; if a file is uploaded, it transcribes the audio content using a pre-trained speech recognition model, processes the text, generates additional text based on the input, and records relevant information. If JSON data is provided, it prints "json."

The generated text, along with associated metadata, is added to a list called `generated_texts`. The information is then saved, and the response is formatted based on the request content type. If it's JSON, the data is returned as JSON; otherwise, it renders an HTML template, passing relevant information to be displayed on the webpage.

The GET section renders the HTML template when the route is accessed via a GET request.
"""
