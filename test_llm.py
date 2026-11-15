from llm import generate_response

# Create a test prompt
prompt = """
Explain what an API endpoint is
in simple words with one example.
"""

# Get response from Groq AI
response = generate_response(prompt)

# Display AI response
print("\nPHANTOM AI RESPONSE")
print("===================")
print(response)