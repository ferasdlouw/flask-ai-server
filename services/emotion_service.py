from flask import Blueprint, request, jsonify
from deepface import DeepFace
import cv2
import numpy as np
import base64

analyze_emotion_route = Blueprint('emotion', __name__)

@analyze_emotion_route.route('/analyze', methods=['POST'])
def analyze_emotion():
    try:
        data = request.json
        img_data = base64.b64decode(data['image'])
        nparr = np.frombuffer(img_data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        analysis = DeepFace.analyze(img_path=img, actions=['emotion'], enforce_detection=False)
        emotion = analysis[0]['dominant_emotion']
        return jsonify({'emotion': emotion})
    except Exception as e:
        return jsonify({'error': str(e)})
