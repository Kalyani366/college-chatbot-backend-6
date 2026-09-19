from sentence_transformers import SentenceTransformer


MODEL_NAME = "all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_NAME)


def create_embeddings(texts):
    embeddings = model.encode(
        texts,
        convert_to_numpy=True,
        show_progress_bar=True
    )

    return embeddings


if __name__ == "__main__":
    test_texts = [
        "What courses are available in CSE?",
        "What is the minimum attendance requirement?"
    ]

    embeddings = create_embeddings(test_texts)

    print("\n==============================")
    print("Embedding shape:", embeddings.shape)
    print("==============================")