import json

# Open the actual OpenAPI JSON file
with open("openapi.json", "r") as file:
    data = json.load(file)

# Extract all documented paths
paths = data["paths"]

print("----- ACTUAL DOCUMENTED API ENDPOINTS -----")

for path, methods in paths.items():

    for method in methods:
        print(method.upper(), path)