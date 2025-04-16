from flask import Flask, request, jsonify
from apk_generator import generate_apk

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": "Backend is working!"})

@app.route('/generate-apk', methods=['POST'])
def generate():
    data = request.get_json()
    user_text = data.get('text')
    
    if not user_text:
        return jsonify({"error": "No text provided"}), 400

    apk_url = generate_apk(user_text)
    return jsonify({"apk_url": apk_url})

if __name__ == '__main__':
    app.run(debug=True)
