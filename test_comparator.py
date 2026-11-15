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
    # Test whether HTTP methods are compared correctly

test_discovered = [("GET", "/students")]

test_documented = [("POST", "/students")]

test_missing = compare_endpoints(
    test_discovered,
    test_documented
)

print("\nHTTP Method Test:")
print(test_missing)
# Test missing OpenAPI file
print("\nTesting Missing OpenAPI File:")

result = load_openapi("unknown.json")

print("Result:", result)
# Test invalid JSON file
print("\nTesting Invalid JSON:")

result = load_openapi("invalid.json")

print("Result:", result)