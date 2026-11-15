from sentence_transformers import SentenceTransformer

# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Sample API descriptions
sentences = [
    "Retrieve all registered users",
    "Get a list of customers",
    "Delete a user account"
]

# Convert descriptions into embeddings
embeddings = model.encode(sentences)

# Display results
print("Embedding Generation Successful!")

print("\nNumber of sentences:", len(sentences))
print("Embedding dimensions:", embeddings.shape)

print("\nFirst embedding:")
print(embeddings[0])