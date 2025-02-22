# file_sorter.py
import os
import shutil

# Set the directory to organize (current folder for simplicity)
source_dir = "."

# Dictionary to map extensions to folder names
file_types = {
    ".txt": "TextFiles",
    ".jpg": "Images",
    ".png": "Images",
    ".pdf": "Documents",
    ".py": "CodeFiles"
}

# Create folders if they don’t exist
for folder in file_types.values():
    if not os.path.exists(folder):
        os.makedirs(folder)

# Loop through files in the directory
for filename in os.listdir(source_dir):
    # Skip directories and this script itself
    if os.path.isfile(filename) and filename != "file_sorter.py":
        # Get the file extension (e.g., ".txt")
        file_ext = os.path.splitext(filename)[1].lower()
        
        # Check if extension is in our dictionary
        if file_ext in file_types:
            dest_folder = file_types[file_ext]
            # Move the file to its folder
            shutil.move(filename, os.path.join(dest_folder, filename))
            print(f"Moved {filename} to {dest_folder}")
        else:
            print(f"Skipped {filename} - unknown type")

print("File sorting complete!")