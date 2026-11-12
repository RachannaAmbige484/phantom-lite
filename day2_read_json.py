# Import Python's built-in JSON module
import json

# Open the JSON file
with open("day2_json_practice.json", "r") as file:

    # Convert JSON data into a Python dictionary
    data = json.load(file)

# Display complete JSON data
print("Complete JSON Data:")
print(data)

# Access individual values
print("\nProject Name:", data["project"])
print("Developer:", data["developer"])
print("Language:", data["language"])

# Access the technologies list
print("\nTechnologies:")

for technology in data["technologies"]:
    print(technology)