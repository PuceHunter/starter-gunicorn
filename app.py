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
@app.route('/upload_audio', methods=['POST'])
def upload_audio():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"})
    
    # Save the uploaded file to a specific location
    file.save('uploads/' + file.filename)

    loaded_model = whisper.load_model('tiny.en')

    transcriptions = loaded_model.transcribe(file)['text']
    
    # Return a response indicating successful file upload
    return jsonify({"message": "File uploaded successfully", "filename": file.filename, "text":transcriptions})

if __name__ == '__main__':
    app.run()
