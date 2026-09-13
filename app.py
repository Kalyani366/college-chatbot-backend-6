from flask import Flask, request, jsonify
from flask_cors import CORS
import sys

# Member 4 folder path
sys.path.append(r"C:\Users\DELL\Documents\member4_intent")

from intent_classifier import classify_intent
from response_handler import get_response
from admin_api import admin_api


app = Flask(__name__)
CORS(app)

app.register_blueprint(admin_api)


@app.route("/")
def home():
    return jsonify({
        "message": "College Chatbot Backend API is running"
    })


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()

    question = data.get("question", "").strip()

    if not question:
        return jsonify({
            "error": "Question is required"
        }), 400

    # Member 4: Intent Classification
    intent = classify_intent(question)

    # Member 4: Response Handling
    response = get_response(intent)

    return jsonify({
        "question": question,
        "intent": intent,
        "response": response
    })


if __name__ == "__main__":
    app.run(debug=True)