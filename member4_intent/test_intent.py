from intent_classifier import classify_intent
from response_handler import get_response


test_questions = [
    "What is the exam date?",
    "Show my class schedule",
    "Tell me about BTech",
    "Show the curriculum",
    "What is the attendance percentage?",
    "How much is the college fee?",
    "Who is the CSE HOD?",
    "How can I apply for admission?",
    "What are the college events?",
    "What clubs are available?",
    "What are the academic rules?",
    "Tell me about the college",
    "Tell me about cricket",
    "Hi"
]


for question in test_questions:
    intent = classify_intent(question)
    response = get_response(intent)

    print("----------------------------------------")
    print("Question:", question)
    print("Intent:", intent)
    print("Response:", response)