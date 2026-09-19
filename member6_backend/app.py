from flask import Flask, request, jsonify
from flask_cors import CORS
import sys

# =====================================
# Member 4 folder path
# =====================================
sys.path.append(r"C:\Users\DELL\Documents\member4_intent")

# =====================================
# Member 4 imports
# =====================================
from intent_classifier import classify_intent
from response_handler import get_response

# =====================================
# Member 2 RAG import
# =====================================
from member2_rag.retrieval import retrieve_documents

# =====================================
# Member 1 LLM import
# =====================================
from member1_llm.response_generator import generate_final_response

# =====================================
# Member 6 Admin API
# =====================================
from admin_api import admin_api


app = Flask(__name__)

CORS(app)

# Register Admin API
app.register_blueprint(admin_api)


# =====================================
# Home API
# =====================================
@app.route("/")
def home():
    return jsonify({
        "message": "College Chatbot Backend API is running"
    })


# =====================================
# Chat API
# =====================================
@app.route("/api/chat", methods=["POST"])
def chat():

    data = request.get_json()

    question = data.get("question", "").strip()

    if not question:
        return jsonify({
            "error": "Question is required"
        }), 400

    # =====================================
    # Member 4: Intent Classification
    # =====================================
    intent = classify_intent(question)

    # =====================================
    # Member 4: Response Handling
    # =====================================
    response = get_response(intent)

    # =====================================
    # Member 2: RAG Retrieval
    # =====================================
    documents = retrieve_documents(question)

    # =====================================
    # Convert Member 2 documents
    # into context for Member 1
    # =====================================
    context_chunks = [
        f"Source: {doc['source']}\n"
        f"Page: {doc.get('page', 'N/A')}\n"
        f"{doc['text']}"
        for doc in documents
    ]

    # =====================================
    # Convert Member 4 intent
    # for Member 1
    # =====================================
    llm_intent = (
        "out_of_domain"
        if intent == "OUT_OF_DOMAIN"
        else "in_domain"
    )

    # =====================================
    # Member 1: Final LLM Response
    # =====================================
    final_response = generate_final_response(
        query=question,
        context_chunks=context_chunks,
        intent=llm_intent
    )

    # =====================================
    # Return Combined Response
    # =====================================
    return jsonify({
        "question": question,
        "intent": intent,
        "response": final_response,
        "documents": documents
    })


# =====================================
# Run Flask server
# =====================================
if __name__ == "__main__":
    app.run(debug=True)