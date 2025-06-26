import os

# The folder where you want to create your files
target = input("Where should I create the folders? (e.g., project2):\n").strip()

# Ask for file names (space-separated)
files_input = input("Enter file names (without .py), separated by spaces:\n").strip()
files = files_input.split()

# Create folders and .py files
for name in files:
    folder_path = os.path.join(target, name)
    os.makedirs(folder_path, exist_ok=True)
    with open(os.path.join(folder_path, f"{name}.py"), "w") as f:
        f.write("\n")  # Write a blank line at the start
        f.write("\n")  # Write a blank line at the start

print("Folders and files created!")
