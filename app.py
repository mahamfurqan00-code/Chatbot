from flask import Flask, jsonify, render_template, request
from chatbot_engine import get_answer, suggested_questions

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024  # Keep request bodies small.


@app.get("/")
def home():
    return render_template("index.html", suggestions=suggested_questions())


@app.get("/api/health")
def health():
    return jsonify({"status": "ok", "service": "Hospital FAQ Assistant"})


@app.post("/api/chat")
def chat():
    payload = request.get_json(silent=True) or {}
    message = payload.get("message", "")

    if not isinstance(message, str):
        return jsonify({"error": "Message must be text."}), 400

    message = message.strip()
    if not message:
        return jsonify({"error": "Please type a question first."}), 400
    if len(message) > 500:
        return jsonify({"error": "Please keep your question under 500 characters."}), 400

    answer, matched_question, confidence = get_answer(message)
    return jsonify({
        "reply": answer,
        "matched_question": matched_question,
        "confidence": round(confidence, 2),
    })


@app.errorhandler(413)
def request_too_large(_error):
    return jsonify({"error": "Your message is too large. Please shorten it."}), 413


if __name__ == "__main__":
    # Local development only. Use a production WSGI server when deploying.
    app.run(debug=True)
