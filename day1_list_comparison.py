# List of endpoints found in Python code
code_endpoints = [
    ("GET", "/users"),
    ("POST", "/login"),
    ("DELETE", "/users/{id}")
]

# List of endpoints documented in OpenAPI
documented_endpoints = [
    ("GET", "/users"),
    ("POST", "/login")
]

# Create an empty list for missing endpoints
missing_endpoints = []

# Check each endpoint found in the code
for endpoint in code_endpoints:

    # Check whether the endpoint exists in documentation
    if endpoint not in documented_endpoints:

        # Add missing endpoint to the list
        missing_endpoints.append(endpoint)

# Display the missing endpoints
print("----- UNDOCUMENTED ENDPOINTS -----")

for method, path in missing_endpoints:
    print(method, path)