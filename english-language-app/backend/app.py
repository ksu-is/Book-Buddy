
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/vocab', methods=['POST'])
def vocab():
    word = request.json.get('word', '')
    prompt = f"Define and explain the word '{word}' in simple English with examples."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return jsonify(response=response.choices[0].message["content"])

@app.route('/conversation', methods=['POST'])
def conversation():
    message = request.json.get('message', '')
    prompt = f"Continue this English conversation naturally: '{message}'"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return jsonify(response=response.choices[0].message["content"])

@app.route('/comprehension', methods=['POST'])
def comprehension():
    text = request.json.get('text', '')
    prompt = f"Read and analyze this text for comprehension: '{text}'. Summarize and provide 2 questions."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return jsonify(response=response.choices[0].message["content"])

if __name__ == '__main__':
    app.run(debug=True)
