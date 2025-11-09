from flask import Flask, jsonify, send_file
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Permite que el HTML acceda a la API desde cualquier origen

@app.route('/')
def index():
    html_file = '5f822cb6-316e-49b9-9a1b-70ec38c7942f.htm'
    if os.path.exists(html_file):
        return send_file(html_file)
    return "HTML file not found", 404

@app.route('/languages', methods=['GET'])
def get_languages():
    languages = [
        {"id": 1, "name": "Python"},
        {"id": 2, "name": "JavaScript"},
        {"id": 3, "name": "Java"},
        {"id": 4, "name": "C#"},
        {"id": 5, "name": "C++"},
    ]
    return jsonify(languages)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

