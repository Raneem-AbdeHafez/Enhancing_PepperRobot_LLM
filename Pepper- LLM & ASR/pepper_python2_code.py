# Finally WORKS, it first detects a face and then start the input text dialoge, saves once in the json file 

import qi
import sys
import requests
import time
import paramiko
from scp import SCPClient
import json
import urllib2  # For Python 2 compatibility
from naoqi import ALProxy
import urllib3
from bs4 import BeautifulSoup
import threading
import argparse
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class HumanGreeterAndTextHandler(object):
    def __init__(self, app):
        super(HumanGreeterAndTextHandler, self).__init__()

        self.app = app
        self.got_face_event = threading.Event()
        self.ip = "10.30.0.53"
        self.port = 9559

    def display_text_on_tablet(self, session, text, duration=30):
        tablet_service = session.service("ALTabletService")

        tablet_service.showWebview("data:text/html,<html><body><h1>{}</h1></body></html>".format(text))

        time.sleep(duration)
        tablet_service.hideWebview()

    def handle_text_button(self, input_text):
        print("'Text' button is pressed.")
        print("Input text: " + input_text)
        flask_server_url = "http://ailab.samk.fi:2252/"

        session = qi.Session()
        try:
                        session.connect("tcp://" + self.ip + ":" + str(self.port))
        except RuntimeError:
                        print("Unable to connect to Pepper's robot.")
                        quit()

        display_thread = threading.Thread(target=self.display_text_on_tablet, args=(session, "Generating a Response, Please wait", 30))
        display_thread.start()

        data = {'input_text': input_text}
        data = json.dumps(data)

        try:
            import time
            start_time_generate = time.time()

            response = urllib2.urlopen(urllib2.Request(flask_server_url, data, headers={'Content-Type': 'application/json'}))
            response_data = response.read()
            response_data = json.loads(response_data)
            generated_text = response_data.get('generated_text')
            if generated_text:
                generated_text_utf8 = generated_text.encode('UTF-8')
                end_time_generate = time.time()
                print("Generated Text: ", generated_text_utf8)
                print("Generated Time: ", end_time_generate - start_time_generate)
                print("----------------------")

                session = qi.Session()
                try:
                    session.connect("tcp://" + self.ip + ":" + str(self.port))
                except RuntimeError:
                    print("Unable to connect to Pepper's robot.")
                    quit()

                display_thread = threading.Thread(target=self.display_text_on_tablet, args=(session, generated_text_utf8, 30))
                display_thread.start()
                tts = ALProxy("ALTextToSpeech", self.ip, self.port)
                tts.say(generated_text_utf8)

            else:
                print("Failed to get a valid response from the Flask server.")

        except urllib2.URLError as e:
            print("Failed to retrieve generated text from the Flask server:", e)

    def handle_record_button(self):
        def scp_file_from_remote(server, port, user, password, remote_path, local_path):
            start_time_wav = time.time()
            ssh = self.createSSHClient(server, port, user, password)
            with SCPClient(ssh.get_transport()) as scp:
                scp.get(remote_path, local_path)
            ssh.close()
            end_time_wav = time.time()
            print("WAV FILE SAVED")
            print("Time to save WAV File:", end_time_wav - start_time_wav)
            print ("----------------------")

        def extract_generated_text(response_text):
            generated_text_match = re.search(r'var generatedText = (\[.*?\]);', response_text)
            if generated_text_match:
                generated_text = json.loads(generated_text_match.group(1))
                return ' '.join(generated_text)
            else:
                return None

        # Your audio recording code
        ALAudioRecorder = ALProxy("ALAudioRecorder", "10.30.0.53", 9559)
        audio_recorder = ALAudioRecorder
        ping_result = audio_recorder.ping()
        print("Ping result:", ping_result)

        audio_recorder.stopMicrophonesRecording()
        filename = "/home/nao/audio.wav"
        recording_type = "wav"
        samplerate = 16000
        channels = [0, 0, 1, 0]
        audio_recorder.startMicrophonesRecording(filename, recording_type, samplerate, channels)

        session = qi.Session()
        try:
                    session.connect("tcp://" + self.ip + ":" + str(self.port))
        except RuntimeError:
                    print("Unable to connect to Pepper's robot.")
                    quit()

        display_thread = threading.Thread(target=self.display_text_on_tablet, args=(session, "You have 10 seconds to record", 5))
        display_thread.start()
        time.sleep(3)
        

        if audio_recorder:
            print("Recording Started")
            display_thread = threading.Thread(target=self.display_text_on_tablet, args=(session, "Recording Started", 10))
            display_thread.start()
        else:
            print("Failed to Start Recording")

        time.sleep(10)
        audio_recorder.stopMicrophonesRecording()

        if audio_recorder:
            print("Stopped Recording")
            display_thread = threading.Thread(target=self.display_text_on_tablet, args=(session, "Recording stopped", 10))
            display_thread.start()
        else:
            print("Failed to Stop Recording")

        version_result = audio_recorder.version()
        print("Version result:", version_result)

        # Your SSH and SCP code
        local_file_path = 'C:/Python27/pepper_codes/recordings/audio.wav'
        remote_file_path = '~/audio.wav'
        scp_file_from_remote('10.30.0.53', 22, 'nao', 'nao', remote_file_path, local_file_path)

        # Transcription and text generation code
        filename = 'C:\\Python27\\pepper_codes\\recordings\\audio.wav'
        server_url = 'http://ailab.samk.fi:2252/'

        # Send an API request with the audio file for transcription and text generation

        session = qi.Session()
        try:
                        session.connect("tcp://" + self.ip + ":" + str(self.port))
        except RuntimeError:
                        print("Unable to connect to Pepper's robot.")
                        quit()

        display_thread = threading.Thread(target=self.display_text_on_tablet, args=(session, "Generating a Response, Please wait", 10))
        display_thread.start()      


        files = {'file': open(filename, 'rb')}
        start_time_request = time.time()
        response = requests.post(server_url, files=files, verify=False)  # Disable SSL verification for simplicity
        end_time_request = time.time()
        print("Request Time:", end_time_request - start_time_request)
        print ("----------------------")


        if response.status_code == 200:
            start_time = time.time()
            # Process the response for transcription
            response_text = response.text
            soup = BeautifulSoup(response_text, 'html.parser')

            # Extract transcribed text
            transcribed_section = soup.find('h2', text='Transcribed Text:').find_next('p')
            transcribed_text = transcribed_section.get_text() if transcribed_section else "Transcribed text not found"
            print("Transcribed Text:", transcribed_text)
            end_time = time.time()
            transcription_time = end_time - start_time
            print("Transcription Time after Request:", transcription_time)
            print ("----------------------")

            # Extract and use generated text
            generated_text = extract_generated_text(response_text)

            if generated_text:
                print("Generated Text:", generated_text)
                generated_text_str = str(generated_text)

                session = qi.Session()
                try:
                    session.connect("tcp://" + self.ip + ":" + str(self.port))
                except RuntimeError:
                    print("Unable to connect to Pepper's robot.")
                    quit()

                display_thread = threading.Thread(target=self.display_text_on_tablet, args=(session, generated_text_str, 30))
                display_thread.start()
                # Use Pepper's text-to-speech module to say the generated text
                tts = ALProxy("ALTextToSpeech", "10.30.0.53", 9559)  # Replace with the appropriate IP and port
                tts.say(generated_text_str)

            else:
                print("Generated text not found in the API response.")
        else:
            print("API request for audio transcription failed with status code", response.status_code)

    def createSSHClient(self, server, port, user, password):
        start_time_ssh = time.time()
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(server, port, user, password)
        end_time_ssh = time.time()
        print("Time took to create SSH Client: ", end_time_ssh - start_time_ssh)
        print("----------------------")
        return client

    def on_human_tracked(self, value):
        if value == [] or self.got_face_event.is_set():  # empty value when the face disappears or already detected
            return

        self.got_face_event.set()
        print("I saw a face!")
        self.tts.say("Face Detected!")

        # First Field = TimeStamp.
        timeStamp = value[0]
        print("TimeStamp is: " + str(timeStamp))

        # Second Field = array of face_Info's.
        faceInfoArray = value[1]
        for j in range(len(faceInfoArray) - 1):
            faceInfo = faceInfoArray[j]

            # First Field = Shape info.
            faceShapeInfo = faceInfo[0]

            # Second Field = Extra info (empty for now).
            faceExtraInfo = faceInfo[1]

            print("Face Infos :  alpha %.3f - beta %.3f" % (faceShapeInfo[1], faceShapeInfo[2]))
            print("Face Infos :  width %.3f - height %.3f" % (faceShapeInfo[3], faceShapeInfo[4]))
            #print("Face Extra Infos :" + str(faceExtraInfo))

        # Unsubscribe from face detection to take a break
        self.face_detection.unsubscribe("HumanGreeter")

    def show_input_dialog(self, tablet_service):
       # Show the input text dialog
        tablet_service.showInputTextDialog("Write a Prompt Or Record", "Text", "Record")

        def callback(button_id, input_text):
            if button_id == 1:
                self.handle_text_button(input_text)
            elif button_id == 0:
                self.handle_record_button()

            tablet_service.onInputText.disconnect(signal_id)
            self.app.stop()

        signal_id = tablet_service.onInputText.connect(callback)
        print("Signal ID: {}".format(signal_id))

        self.app.run()

    def main(self):
        try:
            session = self.app.session

            self.tts = session.service("ALTextToSpeech")
            self.face_detection = session.service("ALFaceDetection")
            self.face_detection.subscribe("HumanGreeter")
            self.subscriber = session.service("ALMemory").subscriber("FaceDetected")
            self.subscriber.signal.connect(self.on_human_tracked)

            # Wait for the face detection event
            self.got_face_event.wait()

            # Start a separate thread to show the input text dialog
            dialog_thread = threading.Thread(target=self.show_input_dialog, args=(session.service("ALTabletService"),))
            dialog_thread.start()

        except Exception as e:
            print("Error was: ", e)


if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("--ip", type=str, default="10.30.0.53",
                            help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
        parser.add_argument("--port", type=int, default=9559,
                            help="Naoqi port number")

        args = parser.parse_args()
        try:
            # Initialize qi framework only once.
            connection_url = "tcp://" + args.ip + ":" + str(args.port)
            app = qi.Application(["HumanGreeterAndTextHandler", "--qi-url=" + connection_url])
            app.start()

            human_greeter_and_text_handler = HumanGreeterAndTextHandler(app)
            human_greeter_and_text_handler.main()

        except RuntimeError:
            print("Can't connect to Naoqi.")
            sys.exit(1)

