import json
from scanner import extract_endpoints


# Load OpenAPI documentation
def load_openapi(filepath):

    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data


# Extract documented endpoints
def extract_documented_endpoints(spec):

    endpoints = []

    paths = spec["paths"]

    for path, methods in paths.items():

        for method in methods:

            endpoints.append((method.upper(), path))

    return endpoints


# Compare discovered and documented endpoints
def compare_endpoints(discovered, documented):

    missing_endpoints = []

    for endpoint in discovered:

        if endpoint not in documented:
            missing_endpoints.append(endpoint)

    return missing_endpoints


# Run testing only when this file is executed directly
if __name__ == "__main__":

    spec = load_openapi("openapi.json")

    documented_endpoints = extract_documented_endpoints(spec)

    discovered_endpoints = extract_endpoints("main.py")

    missing_endpoints = compare_endpoints(
        discovered_endpoints,
        documented_endpoints
    )

    print("\nUndocumented Endpoints:")

    for method, path in missing_endpoints:
        print(method, path)