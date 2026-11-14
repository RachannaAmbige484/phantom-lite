from fastapi import FastAPI

# Create a FastAPI application
app = FastAPI()

# Create our first API endpoint
@app.get("/")
def home():
    return {"message": "Welcome to PHANTOM Lite"}
# Get all students
@app.get("/students")
def get_students():
    return {"students": ["Rachanna", "Sumeet", "Veeresh"]}


# Create a student
@app.post("/students")
def create_student():
    return {"message": "Student created successfully"}


# Delete a student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    return {"message": f"Student {student_id} deleted successfully"}
# Secret endpoint - intentionally undocumented
@app.get("/secret", include_in_schema=False)
def secret_endpoint():
    return {"message": "This endpoint is hidden from documentation"}
# Another hidden endpoint for testing
@app.get("/health")
def health_check():
    return {"status": "healthy"}