# Filename: app.py
from flask import Flask, request, jsonify
import os
from openai import OpenAI

app = Flask(__name__)

# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=data['messages']
    )
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)