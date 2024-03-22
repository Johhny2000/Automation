import os

# Get the user's desktop directory
desktop_path = os.path.expanduser("~/Desktop")

# Get file name
name_files = str(input("Base file name: "))

# Get file type
type_files = str(input("File extension: "))

# Get the number of files to create
num_files = int(input("Enter number of files to create: "))

# Create the files on the desktop
for i in range(1, num_files+1):
    file_name = f"{name_files}{i}.{type_files}"
    file_path = os.path.join(desktop_path, file_name)
    try:
        with open(file_path, "w") as file:
            pass  # This creates an empty file
        print(f"*Created {file_name} on {file_path}*")
    except Exception as e:
        print(f"An error occurred while creating {file_name}: {str(e)}")
