from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from openai import OpenAI

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    response = client.chat.completions.create(
        model="gpt-4o-mini-2024-07-18",
        messages=data['messages']
    )
    # return jsonify(response.choices[0].message)
    return response.choices[0].message

@app.route('/api/go', methods=['GET'])
def go():
    return 'go, then!' 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
