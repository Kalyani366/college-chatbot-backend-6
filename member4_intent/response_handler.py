from intents import INTENTS
def get_response(intent):
    if intent == "AMBIGUOUS":
        return "Could you please provide more details about your college-related question?"

    elif intent == "OUT_OF_DOMAIN":
        return "Sorry, I can only answer questions related to college information."

    elif intent == "EXAM":
        return "I can help you with exam-related information."

    elif intent == "TIMETABLE":
        return "I can help you with the college timetable."

    elif intent == "SYLLABUS":
        return "I can help you with syllabus information."

    elif intent == "ATTENDANCE":
        return "I can help you with attendance-related information."

    elif intent == "FEES":
        return "I can help you with college fee information."

    elif intent == "FACULTY":
        return "I can help you with faculty information."

    elif intent == "ADMISSION":
        return "I can help you with admission information."

    elif intent == "EVENTS":
        return "I can help you with college events information."

    elif intent == "CLUBS":
        return "I can help you with college club information."

    elif intent == "ACADEMIC_REGULATIONS":
        return "I can help you with academic regulations."

    elif intent == "COURSE":
        return "I can help you with course information."

    elif intent == "GENERAL_COLLEGE":
        return "I can help you with general college information."

    else:
        return "Sorry, I could not understand your question."