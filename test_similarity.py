from sentence_transformers import SentenceTransformer
import numpy as np

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# API examples
sentences = [
    "Retrieve all registered users",
    "Get a list of customers",
    "Delete a user account"
]

# Convert sentences into embeddings
embeddings = model.encode(sentences)

# New API description
query = "Retrieve all customers"

query_embedding = model.encode([query])[0]

# Calculate cosine similarity
similarities = np.dot(embeddings, query_embedding) / (
    np.linalg.norm(embeddings, axis=1) *
    np.linalg.norm(query_embedding)
)

# Get indexes sorted by similarity (highest first)
top_indices = np.argsort(similarities)[::-1][:3]

print("\nTop 3 Similar API Examples:")

for index in top_indices:
    print(sentences[index], ":", round(similarities[index], 4))