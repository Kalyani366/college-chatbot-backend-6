from intent_classifier import classify_intent
from response_handler import get_response


def process_question(question):
    intent = classify_intent(question)
    response = get_response(intent)

    return {
        "question": question,
        "intent": intent,
        "response": response
    }


if __name__ == "__main__":
    question = input("Enter your question: ")

    result = process_question(question)

    print("Question:", result["question"])
    print("Intent:", result["intent"])
    print("Response:", result["response"])