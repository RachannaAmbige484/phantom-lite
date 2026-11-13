import re


def extract_endpoints(filepath):

    print("PHANTOM Scanner Started")

    # Read the Python source file
    with open(filepath, "r", encoding="utf-8") as file:
        code = file.read()

    # Store discovered endpoints
    endpoints = []

    # Pattern to identify FastAPI endpoints
    pattern = r'@app\.(get|post|put|delete|patch)\(\s*["\']([^"\']+)["\']\s*\)'

    # Find all matching endpoints
    matches = re.findall(pattern, code)

    for method, path in matches:
        print(method.upper(), path)


# Test the scanner
extract_endpoints("main.py")