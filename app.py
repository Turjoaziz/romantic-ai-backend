from flask import Flask, request, jsonify
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/")
def index():
    return "Romantic AI Backend is running"

@app.route("/romantic-reply", methods=["POST"])
def romantic_reply():
    data = request.get_json()
    user_input = data.get("message", "")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a romantic, poetic, affectionate AI boyfriend. Always reply with deep love, tenderness, and care."},
            {"role": "user", "content": user_input}
        ],
        temperature=0.9,
        max_tokens=100
    )

    reply = response['choices'][0]['message']['content']
    return jsonify({"reply": reply})

# 🛠️ THIS PART IS MANDATORY FOR RENDER
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
