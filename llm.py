import os
from groq import Groq
from dotenv import load_dotenv


# Load API key from .env file
load_dotenv()


# Create Groq connection
def get_groq_client():

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("Groq API key not found!")

    client = Groq(api_key=api_key)

    return client


# Generate AI response
def generate_response(prompt):

    client = get_groq_client()

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": "You are an expert API documentation assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

# Generate API documentation using retrieved RAG examples
def generate_documentation(method, path, similar_examples):

    # Prepare similar examples as context
    context = ""

    for example in similar_examples:
        context += (
            f"\nExample: {example['description']}"
            f"\nSimilarity: {example['similarity']}\n"
        )

    # Create prompt for the AI
    prompt = f"""
    You are an expert API documentation assistant.

    An undocumented API endpoint was discovered:

    HTTP Method: {method}
    API Path: {path}

    Similar documented API examples:
    {context}

    Based on these examples, suggest documentation for this endpoint.

    Include:
    1. API description
    2. Expected purpose
    3. Possible response description

    Do not invent implementation details.
    Clearly mention when information is uncertain.
    """

    # Generate documentation using Groq
    return generate_response(prompt)