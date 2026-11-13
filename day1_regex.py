# Import the regular expression module
import re

# Sample FastAPI code
code = """
@app.get(
    "/users"
)
def get_users():
    return {"users": []}

@app.post("/login")
def login():
    return {"message": "Login"}

@app.delete("/users/{id}")
def delete_user():
    return {"message": "Deleted"}
    @app.put("/students/{student_id}")
def update_student():
    return {"message": "Updated"}
"""

# Create a pattern to identify API decorators
pattern = r'@app\.(get|post|put|delete|patch)\(\s*["\']([^"\']+)["\']\s*\)'

# Search for all matching patterns
matches = re.findall(pattern, code)

# Display the extracted endpoints
print("----- EXTRACTED API ENDPOINTS -----")

for method, path in matches:
    print(method.upper(), path)