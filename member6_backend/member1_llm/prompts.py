SYSTEM_PROMPT = """You are an official College Assistant.

Rules:
1. Answer the student's question using ONLY the provided College Information context.
2. Give short, clear, and accurate answers.
3. Do not use outside knowledge, guess, or make up facts.
4. If the provided context does not contain enough information, state:
   "I don't have enough information in the provided college documents to answer this question."
5. Be polite and professional.
"""


def build_prompt_payload(query: str, context_chunks: list[str]) -> list[dict]:
    """
    Formats the system prompt, retrieved context chunks,
    and user query into standard messages format.
    """

    context_text = "\n\n".join(context_chunks) if context_chunks else "No relevant context found."

    user_payload = (
        f"College Information Context:\n{context_text}\n\n"
        f"Student Question:\n{query}"
    )

    return [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": user_payload
        }
    ]