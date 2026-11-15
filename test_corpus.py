import json

# Load the RAG knowledge base
with open("corpus.json", "r", encoding="utf-8") as file:
    corpus = json.load(file)

# Display all API examples
print("PHANTOM RAG Knowledge Base")
print("==========================")

for api in corpus:
    print("\nMethod:", api["method"])
    print("Path:", api["path"])
    print("Description:", api["description"])
    print("Response:", api["response"])

print("\nTotal API Examples:", len(corpus))