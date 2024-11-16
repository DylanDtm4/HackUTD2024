import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from routes import api_routes  # Import the routes module

load_dotenv()

app = Flask(__name__)
CORS(app)

# Register the Blueprint
app.register_blueprint(api_routes, url_prefix='/api')  # All routes prefixed with '/api'

if __name__ == '__main__':
    app.run(debug=True)
