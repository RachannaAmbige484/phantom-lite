# Import Path to work with file paths
from pathlib import Path

# Get the location of this Python file
file_path = Path(__file__)

# Open the file in read mode
with open(file_path, "r", encoding="utf-8") as file:

    # Read the complete file
    content = file.read()

# Display the file contents
print("----- FILE CONTENTS -----")
print(content)