import os
import numpy as np
import librosa
import whisper
import pyttsx3
import pyaudio
import wave
import keyboard
import re
import json
from tensorflow.keras.models import load_model

# Load the voice activation model
voice_activation_model = load_model('ahoy_navigator/ahoy_navigator_model.h5')

# Function to extract features
def extract_features(file_path):
    try:
        audio, sample_rate = librosa.load(file_path, res_type='kaiser_fast')
        mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
        mfccs_processed = np.mean(mfccs.T, axis=0)
    except Exception as e:
        print(f"Error encountered while parsing file: {file_path}, Error: {e}")
        return None
    return mfccs_processed

# Function to check if the voice is recognized
def is_voice_recognized(audio_path):
    mfccs = extract_features(audio_path)
    if mfccs is not None:
        mfccs = np.array([mfccs])
        mfccs = np.reshape(mfccs, (mfccs.shape[0], mfccs.shape[1], 1))
        prediction = voice_activation_model.predict(mfccs)
        # Assuming a threshold for recognition, you might need to adjust this
        return np.max(prediction) > 0.5
    return False

# Load Whisper model
model = whisper.load_model("small")

# Initialize PyAudio
p = pyaudio.PyAudio()

# Audio settings
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 1024

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to record audio
def record_audio():
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    print("Recording... Press 'Q' to stop recording.")

    frames = []
    is_recording = True

    while is_recording:
        data = stream.read(CHUNK)
        frames.append(data)
        if keyboard.is_pressed('q'):
            is_recording = False

    print("Finished recording.")
    stream.stop_stream()
    stream.close()

    with wave.open(OUTPUT_PATH, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

# Main loop
while True:
    OUTPUT_PATH = "microphone_audio.wav"
    record_audio()

    if is_voice_recognized(OUTPUT_PATH):
        result = model.transcribe(OUTPUT_PATH)
        user_input = result["text"]
        json_object = {"##USER": user_input}

        new_json_object = {
            "INPUT": json_object["##USER"],
            "RESPONSE": None,
            "COMMAND": None,
            "SYSTEM": None
        }

        json_string = json.dumps(new_json_object, indent=4)
        print(json_string)

        normalized_input = user_input.upper()
        responses = {
            " GET SPEED.": "Our velocity at this moment is 28 knots. A fast-paced journey!",
            " TURN ON LIGHTS.": "lights turned on",
            " GET WEATHER.": "Weather is goood",
            " TURN ON NAV LIGHTS": "Nav Lights on",
            " TURN OFF NAV LIGHTS.": "Nav lights off",
            " GET FUEL INFO.": "tank has 75% of its capacity",
            " GET DESTINATION INFO.": "Our destination is something and something",
            " GET COURSE.": "We are going Norteast from Hamburg port",
            " PREPARE FOR DEPARTURE.": "everything ready",
            " PLAY SONG.": "The song is being played",
            " PLAY ARTIST LED ZEPPELIN.": "test test test testq",

        }

        # Use regular expressions to extract the command more accurately
        match = re.search(r'##COMMAND:(.*?)', normalized_input)
        command = match.group(1).strip() if match else None

        # Debugging output
        print("Normalized Input:", normalized_input)
        print("Command:", command)

        # Check if a valid command is found
        if normalized_input is not None and normalized_input in responses:
            response = responses[normalized_input]
        else:
            response = "I'm not sure how to respond to that command."

        # Print and speak the response
        print("Response:", response)
        engine.say(response)
        engine.runAndWait()

        # Speak the prompt for the next command
        engine.say("I am ready for the next command.")
        engine.runAndWait()