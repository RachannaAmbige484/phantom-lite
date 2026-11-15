import json
from scanner import extract_endpoints


def load_openapi(filepath):

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data

    except FileNotFoundError:
        print(f"Error: OpenAPI file '{filepath}' not found.")
        return {}

    except json.JSONDecodeError:
        print(f"Error: OpenAPI file '{filepath}' contains invalid JSON.")
        return {}


def extract_documented_endpoints(spec):

    endpoints = []

    paths = spec["paths"]

    # Allowed HTTP methods
    allowed_methods = [
        "get",
        "post",
        "put",
        "delete",
        "patch",
        "options",
        "head",
        "trace"
    ]

    for path, methods in paths.items():

        for method in methods:

            if method.lower() in allowed_methods:
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