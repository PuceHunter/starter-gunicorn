from flask import Flask, jsonify
from flask_cors import CORS
import assemblyai as aai

aai.settings.api_key = "0fce9e03ad9e46868c892e1b1b69b48f"

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
    
    transcriber = aai.Transcriber()
    
    # Return a response indicating successful file upload
    return jsonify({"text": transcriber.transcribe(file).text})

if __name__ == '__main__':
    app.run()
