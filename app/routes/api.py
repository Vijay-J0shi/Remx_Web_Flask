from flask import Blueprint, jsonify, request
from app.utils.image_processing import call_aws_api

api_bp = Blueprint('api', __name__)

@api_bp.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    result = call_aws_api(file)
    return jsonify(result)