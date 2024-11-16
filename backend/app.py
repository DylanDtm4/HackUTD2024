import os
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from routes import api_routes

# Load environment variables
load_dotenv()

# Setup Flask app
app = Flask(__name__)
CORS(app)

app.register_blueprint(api_routes, url_prefix='/api')

# PINATA_API_KEY = os.getenv("PINATA_API_KEY")
# PINATA_API_SECRET = os.getenv("PINATA_API_SECRET")
# PINATA_BASE_URL = "https://api.pinata.cloud/pinning/pinFileToIPFS"

# @app.route('/api/upload', methods=['POST'])
# def upload_to_pinata():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file provided'}), 400

#     file = request.files['file']

#     headers = {
#         "pinata_api_key": PINATA_API_KEY,
#         "pinata_secret_api_key": PINATA_API_SECRET
#     }

#     files = {
#         'file': (file.filename, file)
#     }

#     response = requests.post(PINATA_BASE_URL, files=files, headers=headers)

#     if response.status_code == 200:
#         return jsonify(response.json())
#     else:
#         return jsonify({'error': 'Failed to upload to Pinata'}), response.status_code

# @app.route('/api/files', methods=['GET'])
# def list_uploaded_files():
#     url = "https://api.pinata.cloud/data/pinList"
#     headers = {
#         "pinata_api_key": PINATA_API_KEY,
#         "pinata_secret_api_key": PINATA_API_SECRET
#     }

#     # Optional: Add query params for filtering
#     params = {
#         "status": "pinned",  # Only get successfully pinned files
#         "pageLimit": 10,    # Number of files per page (increase as needed)
#     }

#     response = requests.get(url, headers=headers, params=params)

#     if response.status_code == 200:
#         return jsonify(response.json())  # Send the file list to React
#     else:
#         return jsonify({'error': 'Failed to retrieve files'}), response.status_code

@app.route('/api/delete-file/<hash>', methods=['DELETE'])
def delete_file(hash):
    logger.debug(f"Delete request received for hash: {hash}")
    headers = {
        "pinata_api_key": PINATA_API_KEY,
        "pinata_secret_api_key": PINATA_API_SECRET,
        "Content-Type": "application/json",
    }
    url = DELETE_URL
    data = {"ipfs_pin_hash": hash}

    try:
        # Send POST request to Pinata API
        response = requests.post(url, headers=headers, json=data)
        logger.debug(f"Pinata response status: {response.status_code}")

        if response.status_code == 200:
            # Handle empty response gracefully
            try:
                # If there's no body, return success
                response.json()
            except ValueError:
                pass  # Empty body, no error

            return jsonify({'message': 'File deleted successfully'}), 200
        else:
            # Attempt to parse error details if available
            try:
                error_details = response.json()
            except ValueError:
                error_details = {"error": "Invalid response from Pinata API"}

            logger.error(f"Failed to delete file: {error_details}")
            return jsonify({'error': 'Failed to delete file', 'details': error_details}), response.status_code
    except Exception as e:
        logger.error(f"Error during deletion: {str(e)}")
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
