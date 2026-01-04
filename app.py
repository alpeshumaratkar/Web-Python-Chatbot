from flask import Flask, render_template, request, jsonify
from chatbot import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json(silent=True)

        if not data or "message" not in data:
            return jsonify({"reply": "Invalid request"}), 400

        user_msg = data["message"]

        bot_reply = get_response(user_msg)

        return jsonify({"reply": bot_reply})

    except Exception as e:
        print("ERROR:", e)  # <-- this will appear in Render logs
        return jsonify({"reply": "Internal server error"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
