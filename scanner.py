import re


def extract_endpoints(filepath):

    print("PHANTOM Scanner Started")

    # Read the Python source file
    with open(filepath, "r", encoding="utf-8") as file:
        code = file.read()

    # Store discovered endpoints
    endpoints = []

    # Pattern to identify FastAPI endpoints
    pattern = r'@app\.(get|post|put|delete|patch)\(\s*["\']([^"\']+)["\'][^)]*\)'

    # Find all matching endpoints
    matches = re.findall(pattern, code)

    # Store endpoints in the list
    for method, path in matches:
        endpoints.append((method.upper(), path))

    return endpoints


# Test the scanner
result = extract_endpoints("main.py")

print("\nDiscovered Endpoints:")
print(result)