from scanner import extract_endpoints

# Call the scanner function
endpoints = extract_endpoints("main.py")

# Display the returned list
print("\nEndpoints received from scanner:")

for method, path in endpoints:
    print(method, path)