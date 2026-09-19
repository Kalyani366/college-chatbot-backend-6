import faiss
import json
import numpy as np
from pathlib import Path

from embeddings import create_embeddings


# Paths
BASE_DIR = Path(__file__).parent
INDEX_DIR = BASE_DIR / "data" / "faiss_index"

METADATA_FILE = INDEX_DIR / "metadata.json"
INDEX_FILE = INDEX_DIR / "college.index"


def build_index():

    # Load metadata
    with open(METADATA_FILE, "r", encoding="utf-8") as file:
        chunks = json.load(file)

    # Get text from chunks
    texts = [chunk["text"] for chunk in chunks]

    print("Creating embeddings...")
    embeddings = create_embeddings(texts)

    # Convert to float32 for FAISS
    embeddings = np.asarray(embeddings, dtype="float32")

    # Create FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)

    # Add embeddings
    index.add(embeddings)

    # Save FAISS index
    faiss.write_index(index, str(INDEX_FILE))

    print("\n==============================")
    print("FAISS index created successfully")
    print("Chunks:", len(chunks))
    print("Embedding dimension:", dimension)
    print("Index:", INDEX_FILE)
    print("==============================")


if __name__ == "__main__":
    build_index()