from flask import Blueprint, request, jsonify
import requests
import os

api_routes = Blueprint('api_routes', __name__)

PINATA_API_KEY = os.getenv("PINATA_API_KEY")
PINATA_API_SECRET = os.getenv("PINATA_API_SECRET")
PINATA_BASE_URL = "https://api.pinata.cloud/pinning/pinFileToIPFS"

@api_routes.route('/test')
def test():
    return 'Test was successful.'

@api_routes.route('/upload', methods=['POST'])
def upload_to_pinata():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']

    headers = {
        "pinata_api_key": PINATA_API_KEY,
        "pinata_secret_api_key": PINATA_API_SECRET
    }

    files = {
        'file': (file.filename, file)
    }

    response = requests.post(PINATA_BASE_URL, files=files, headers=headers)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Failed to upload to Pinata'}), response.status_code

@api_routes.route('/files', methods=['GET'])
def list_uploaded_files():
    url = "https://api.pinata.cloud/data/pinList"
    headers = {
        "pinata_api_key": PINATA_API_KEY,
        "pinata_secret_api_key": PINATA_API_SECRET
    }

    # Optional: Add query params for filtering
    params = {
        "status": "pinned",  # Only get successfully pinned files
        "pageLimit": 10,    # Number of files per page (increase as needed)
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return jsonify(response.json())  # Send the file list to React
    else:
        return jsonify({'error': 'Failed to retrieve files'}), response.status_code