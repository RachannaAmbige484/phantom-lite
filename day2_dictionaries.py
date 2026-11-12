# Create a dictionary containing student information

student = {
    "name": "Rachanna",
    "age": 20,
    "department": "CSE",
    "year": 3
}

# Display the complete dictionary
print("Student Information:")
print(student)

# Access individual values using keys
print("\nStudent Name:", student["name"])
print("Department:", student["department"])

# Add a new key-value pair
student["college"] = "Engineering College"

# Update an existing value
student["age"] = 21

# Display the updated dictionary
print("\nUpdated Student Information:")
print(student)