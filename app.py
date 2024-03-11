import subprocess
import whisper

def install_ffmpeg():
    try:
        # Check if ffmpeg is installed
        subprocess.run(["ffmpeg", "-version"], check=True)
    except FileNotFoundError:
        # If ffmpeg is not installed, install it
        subprocess.run(["sudo", "apt", "update"])
        subprocess.run(["sudo", "apt", "install", "ffmpeg", "-y"])

# Call the install_ffmpeg function to ensure ffmpeg is installed
install_ffmpeg()

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configured route to /message
@app.route('/message')
def get_data():
    data = "Hello, World from Rikin Zala!"
    response_data = {"message": data}
    return jsonify(response_data)

# Route for uploading audio files
@app.route('/get_audio_transcription')
def get_audio_transcription():
    file = "ebmp-test-audio.mp3"
    
    loaded_model = whisper.load_model('tiny.en')

    transcriptions = loaded_model.transcribe(file)['text']
    
    # Return a response indicating successful file upload
    return jsonify({"text":transcriptions})

if __name__ == '__main__':
    app.run()
