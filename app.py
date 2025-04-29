from flask import Flask, request, jsonify
from services.emotion_service import analyze_emotion_route
from services.whisper_service import transcribe_audio_route

app = Flask(__name__)

app.register_blueprint(analyze_emotion_route)
app.register_blueprint(transcribe_audio_route)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
