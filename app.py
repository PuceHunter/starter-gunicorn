import subprocess

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

if __name__ == '__main__':
    app.run()

# def app(environ, start_response):
#     data = b"Hello, World from Rikin Zala!\n"
#     start_response("200 OK", [
#         ("Content-Type", "text/plain"),
#         ("Content-Length", str(len(data)))
#     ])
#     return iter([data])
