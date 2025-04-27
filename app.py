from flask import Flask, request, jsonify
from deepface import DeepFace
import cv2
import numpy as np
import base64

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_emotion():
    try:
        data = request.json
        img_data = base64.b64decode(data['image'])
        nparr = np.frombuffer(img_data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # تحليل المشاعر
        analysis = DeepFace.analyze(img_path=img, actions=['emotion'], enforce_detection=False)
        emotion = analysis[0]['dominant_emotion']

        return jsonify({'emotion': emotion})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)

