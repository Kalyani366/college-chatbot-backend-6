from member1_llm.response_generator import generate_final_response


print("--- Running Test 1: In-Domain Query with Context ---")

sample_context = [
    "The last date for mini project submission is 20 September 2026.",
    "Students must submit the project report to the department coordinator."
]

query_1 = "Who should receive the project report?"

response_1 = generate_final_response(
    query=query_1,
    context_chunks=sample_context,
    intent="in_domain"
)

print("Query:", query_1)
print("Response:\n", response_1)
print("-" * 50)


print("\n--- Running Test 2: Missing Information Context ---")

query_2 = "What is the fee for late submission?"

response_2 = generate_final_response(
    query=query_2,
    context_chunks=sample_context,
    intent="in_domain"
)

print("Query:", query_2)
print("Response:\n", response_2)
print("-" * 50)


print("\n--- Running Test 3: Out-Of-Domain Intent ---")

query_3 = "How do I make chocolate cake?"

response_3 = generate_final_response(
    query=query_3,
    context_chunks=sample_context,
    intent="out_of_domain"
)

print("Query:", query_3)
print("Response:\n", response_3)
print("-" * 50)