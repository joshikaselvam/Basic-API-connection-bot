from flask import Flask, request, jsonify, render_template
from groq import Groq
import os
from flask import Flask, request, jsonify, send_from_directory



app = Flask(__name__)

# Initialize Groq client (using API key directly for now)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.route("/")
def home():
    return send_from_directory("static", "index.html")
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message")
    print("User said:", user_message)  # Debug print

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant"

,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )
        bot_message = response.choices[0].message.content
        print("Bot replied:", bot_message)  # Debug print
        return jsonify({"reply": bot_message})

    except Exception as e:
        print("Error from Groq:", str(e))
        return jsonify({"reply": "⚠️ Error: " + str(e)})



if __name__ == "__main__":
    app.run(debug=True)
