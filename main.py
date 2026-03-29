from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key)

messages = [
    {"role": "system", "content": "You are name is ORION 5."}
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-5-nano",
        messages=messages
    )

    reply = response.choices[0].message.content

    messages.append({"role": "assistant", "content": reply})

    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
