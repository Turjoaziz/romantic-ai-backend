from flask import Flask, request, jsonify
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route('/')
def hello():
    return "Romantic AI Backend Running"

@app.route('/romantic-reply', methods=['POST'])
def romantic_reply():
    data = request.get_json()
    user_input = data.get("message", "")
    
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a romantic, loving AI boyfriend."},
            {"role": "user", "content": user_input}
        ],
        max_tokens=100,
        temperature=0.9
    )
    
    return jsonify({"reply": response['choices'][0]['message']['content']})
