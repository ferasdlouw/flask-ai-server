from flask import Blueprint, request, jsonify
import whisper, os, tempfile

transcribe_audio_route = Blueprint('whisper', __name__)
model = whisper.load_model("tiny")

@transcribe_audio_route.route('/transcribe', methods=['POST'])
def transcribe_audio():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400

        file = request.files['file']
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
            file.save(temp_file.name)
            temp_filename = temp_file.name

        result = model.transcribe(temp_filename, language='ar')
        text = result['text']

        os.remove(temp_filename)
        return jsonify({'text': text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
