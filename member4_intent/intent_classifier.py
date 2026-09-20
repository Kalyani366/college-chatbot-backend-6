from intents import INTENTS

COLLEGE_KEYWORDS = [
    "college", "campus",
    "exam", "examination", "test", "tests",
    "timetable", "time table", "schedule",
    "syllabus", "syllabi", "curriculum",
    "course", "courses", "subject", "subjects",
    "attendance",
    "fee", "fees", "payment",
    "faculty", "professor", "hod", "teacher",
    "admission", "eligibility",
    "event", "fest", "function",
    "club", "clubs",
    "regulation", "regulations", "rule", "rules",
    "notice",
    "department",
    "cse",
    "btech",
    "degree",
    "program",
    "branch"
]


def classify_intent(question):
    question = question.lower().strip()

    # 1. Empty or very short question
    if not question or len(question) < 5:
        return "AMBIGUOUS"

    # 2. Check whether the question is college-related
    if not any(word in question for word in COLLEGE_KEYWORDS):
        return "OUT_OF_DOMAIN"

    # 3. Exam-related questions
    if any(word in question for word in [
        "exam",
        "examination",
        "exams",
        "tests",
        "test",
        "semester exam",
        "mid exam",
        "midterm",
        "internal exam",
        "final exam"
    ]):
        return "EXAM"

    # 4. Timetable-related questions
    elif any(word in question for word in [
        "timetable",
        "time table",
        "schedule",
        "class schedule",
        "class timing",
        "class timings",
        "lecture schedule",
        "periods"
    ]):
        return "TIMETABLE"

    # 5. Syllabus-related questions
    elif any(word in question for word in [
        "syllabus",
        "syllabi",
        "curriculum",
        "course content",
        "subjects list"
    ]):
        return "SYLLABUS"

    # 6. Course-related questions
    elif any(word in question for word in [
        "course",
        "courses",
        "subject",
        "subjects",
        "btech",
        "degree",
        "program",
        "programs",
        "branch",
        "branches",
        "department"
    ]):
        return "COURSE"

    # 7. Attendance-related questions
    elif any(word in question for word in [
        "attendance",
        "absent",
        "present",
        "attendance percentage"
    ]):
        return "ATTENDANCE"

    # 8. Fee-related questions
    elif any(word in question for word in [
        "fee",
        "fees",
        "payment",
        "tuition fee",
        "college fee"
    ]):
        return "FEES"

    # 9. Academic regulations
    elif any(word in question for word in [
        "rule",
        "rules",
        "regulation",
        "regulations",
        "academic rule"
    ]):
        return "ACADEMIC_REGULATIONS"

    # 10. Faculty-related questions
    elif any(word in question for word in [
        "faculty",
        "professor",
        "hod",
        "teacher",
        "lecturer"
    ]):
        return "FACULTY"

    # 11. Admission-related questions
    elif any(word in question for word in [
        "admission",
        "eligibility",
        "apply",
        "application",
        "joining"
    ]):
        return "ADMISSION"

    # 12. Events-related questions
    elif any(word in question for word in [
        "event",
        "events",
        "fest",
        "function",
        "celebration"
    ]):
        return "EVENTS"

    # 13. Clubs-related questions
    elif any(word in question for word in [
        "club",
        "clubs",
        "student club",
        "student clubs"
    ]):
        return "CLUBS"

    # 14. General college questions
    elif any(word in question for word in [
        "college",
        "campus"
    ]):
        return "GENERAL_COLLEGE"

    # 15. Unknown
    else:
        return "UNKNOWN"


