import faiss
import numpy as np
import json
from pathlib import Path

from .embeddings import model


INDEX_FILE = (
    Path(__file__).parent
    / "data"
    / "faiss_index"
    / "college.index"
)

METADATA_FILE = (
    Path(__file__).parent
    / "data"
    / "faiss_index"
    / "metadata.json"
)


def retrieve_documents(question, top_k=3):

    index = faiss.read_index(str(INDEX_FILE))

    with open(METADATA_FILE, "r", encoding="utf-8") as file:
        chunks = json.load(file)

    question_embedding = model.encode(
        [question],
        convert_to_numpy=True
    )

    question_embedding = np.asarray(
        question_embedding,
        dtype="float32"
    )

    distances, indices = index.search(
        question_embedding,
        top_k
    )

    results = []

    for distance, index_number in zip(
        distances[0],
        indices[0]
    ):
        if 0 <= index_number < len(chunks):

            chunk = chunks[index_number]

            results.append({
                "text": chunk["text"],
                "source": chunk["source"],
                "page": chunk["page"],
                "score": float(distance)
            })

    return results


if __name__ == "__main__":

    question = "What is the minimum attendance requirement?"

    results = retrieve_documents(question)

    print("\n==============================")
    print("Retrieved Documents")
    print("==============================")

    for result in results:
        print("\nSource:", result["source"])
        print("Page:", result["page"])
        print("Score:", result["score"])
        print("Text:", result["text"][:500])