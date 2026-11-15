import json
import numpy as np
from sentence_transformers import SentenceTransformer
# Load API examples from the knowledge base
def load_corpus(filepath):

    with open(filepath, "r", encoding="utf-8") as file:
        corpus = json.load(file)

    return corpus
# Load the sentence embedding model
def load_model():

    model = SentenceTransformer("all-MiniLM-L6-v2")

    return model
# Generate embeddings for API descriptions
def generate_embeddings(model, corpus):

    descriptions = []

    for api in corpus:
        text = (
            api["method"] + " " +
            api["path"] + " " +
            api["description"]
        )

        descriptions.append(text)

    embeddings = model.encode(descriptions)

    return descriptions, embeddings
# Retrieve the most similar API examples
def retrieve_similar(query, model, descriptions, embeddings, top_k=3):

    # Convert the query into an embedding
    query_embedding = model.encode([query])[0]

    # Calculate cosine similarity
    similarities = np.dot(embeddings, query_embedding) / (
        np.linalg.norm(embeddings, axis=1) *
        np.linalg.norm(query_embedding)
    )

    # Get the indexes of the top similar examples
    top_indices = np.argsort(similarities)[::-1][:top_k]

    # Store the retrieved examples
    results = []

    for index in top_indices:
        results.append({
            "description": descriptions[index],
            "similarity": float(similarities[index])
        })

    return results
# Test the RAG retrieval system
if __name__ == "__main__":

    # Load knowledge base
    corpus = load_corpus("corpus.json")

    # Load embedding model
    model = load_model()

    # Generate embeddings
    descriptions, embeddings = generate_embeddings(model, corpus)

    # New API query
    query = "GET /customers Retrieve all customers"

    # Retrieve similar API examples
    results = retrieve_similar(
        query,
        model,
        descriptions,
        embeddings
    )

    # Display results
    print("\nTop 3 Similar API Examples:")

    for result in results:
        print("\nDescription:", result["description"])
        print("Similarity:", round(result["similarity"], 4))