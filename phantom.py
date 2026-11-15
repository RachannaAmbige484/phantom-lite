from scanner import extract_endpoints

from comparator import (
    load_openapi,
    extract_documented_endpoints,
    compare_endpoints
)
from rag import (
    load_corpus,
    load_model,
    generate_embeddings,
    retrieve_similar
)

from llm import generate_documentation
# Define input files
source_file = "main.py"
documentation_file = "openapi.json"

print("PHANTOM LITE")
print("==============================")
print("API Documentation Analyser")
print("==============================")
# Discover endpoints from Python source code
discovered_endpoints = extract_endpoints(source_file)

# Load OpenAPI documentation
spec = load_openapi(documentation_file)

# Stop analysis if documentation cannot be loaded
if not spec:
    print("\nAnalysis stopped due to an OpenAPI file error.")
    exit()

# Extract documented endpoints
documented_endpoints = extract_documented_endpoints(spec)

# Compare discovered and documented endpoints
missing_endpoints = compare_endpoints(
    discovered_endpoints,
    documented_endpoints
)

print("\nAnalysis Results")
print("==============================")

print("Discovered Endpoints:", len(discovered_endpoints))
print("Documented Endpoints:", len(documented_endpoints))

print("\nUndocumented Endpoints:")

if missing_endpoints:
    for method, path in missing_endpoints:
        print(method, path)
else:
    print("No undocumented endpoints found.")

# Generate documentation suggestions for missing endpoints

if missing_endpoints:

    print("\nPHANTOM AI DOCUMENTATION")
    print("==============================")

    # Load RAG knowledge base
    corpus = load_corpus("corpus.json")

    # Load embedding model
    model = load_model()

    # Generate embeddings for API examples
    descriptions, embeddings = generate_embeddings(model, corpus)

    # Process each undocumented endpoint
    for method, path in missing_endpoints:

        print(f"\nAnalyzing: {method} {path}")

        # Create search query
        query = f"{method} {path} API endpoint"

        # Retrieve similar API examples
        similar_examples = retrieve_similar(
            query,
            model,
            descriptions,
            embeddings
        )

        # Generate documentation using Groq
        suggestion = generate_documentation(
            method,
            path,
            similar_examples
        )

        print("\nSuggested Documentation:")
        print(suggestion)
        print("\n------------------------------")

print("\nAnalysis Completed!")