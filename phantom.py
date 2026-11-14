from scanner import extract_endpoints

from comparator import (
    load_openapi,
    extract_documented_endpoints,
    compare_endpoints
)
# Define input files
source_file = "main.py"
documentation_file = "openapi.json"

print("PHANTOM LITE")
print("==============================")
print("API Documentation Analyser")
print("==============================")
# Discover endpoints from Python source code
discovered_endpoints = extract_endpoints(source_file)

# Load OpenAPI documentation
spec = load_openapi(documentation_file)

# Extract documented endpoints
documented_endpoints = extract_documented_endpoints(spec)

# Compare discovered and documented endpoints
missing_endpoints = compare_endpoints(
    discovered_endpoints,
    documented_endpoints
)

print("\nAnalysis Results")
print("==============================")

print("Discovered Endpoints:", len(discovered_endpoints))
print("Documented Endpoints:", len(documented_endpoints))

print("\nUndocumented Endpoints:")

if missing_endpoints:
    for method, path in missing_endpoints:
        print(method, path)
else:
    print("No undocumented endpoints found.")

print("\nAnalysis Completed!")