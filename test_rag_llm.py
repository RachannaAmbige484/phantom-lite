from rag import (
    load_corpus,
    load_model,
    generate_embeddings,
    retrieve_similar
)

from llm import generate_documentation


# Load the RAG knowledge base
corpus = load_corpus("corpus.json")

# Load embedding model
model = load_model()

# Generate embeddings
descriptions, embeddings = generate_embeddings(model, corpus)

# Undocumented API endpoint
method = "GET"
path = "/secret"

# Retrieve similar API examples
query = method + " " + path + " retrieve information"

similar_examples = retrieve_similar(
    query,
    model,
    descriptions,
    embeddings
)

# Generate documentation using Groq
result = generate_documentation(
    method,
    path,
    similar_examples
)

# Display result
print("\nPHANTOM GENERATED DOCUMENTATION")
print("================================")
print(result)