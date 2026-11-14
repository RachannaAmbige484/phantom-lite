from comparator import (
    load_openapi,
    extract_documented_endpoints,
    compare_endpoints
)

from scanner import extract_endpoints


# Load OpenAPI documentation
spec = load_openapi("openapi.json")

# Get documented endpoints
documented = extract_documented_endpoints(spec)

# Discover endpoints from Python source
discovered = extract_endpoints("main.py")

# Compare both lists
missing = compare_endpoints(discovered, documented)


print("\nUndocumented Endpoints:")

for method, path in missing:
    print(method, path)