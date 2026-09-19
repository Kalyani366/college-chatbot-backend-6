from openai import OpenAI
from .prompts import build_prompt_payload


# Connect to local LM Studio server
client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"
)


def generate_final_response(
    query: str,
    context_chunks: list[str],
    intent: str = "in_domain"
) -> str:

    # Handle out-of-domain questions
    if intent == "out_of_domain":
        return (
            "I can only answer questions related to college admissions, "
            "courses, facilities, and academic policies."
        )

    # Build prompt
    messages = build_prompt_payload(
        query,
        context_chunks
    )

    try:
        response = client.chat.completions.create(
            model="llama-3.2-3b-instruct",
            messages=messages,
            temperature=0
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error connecting to local LLM: {str(e)}"