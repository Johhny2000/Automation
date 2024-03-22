import os


def create_folders(path, name_folders, num_folders):
    try:
        # Check if the path exists
        if not os.path.exists(path):
            raise FileNotFoundError(f"The specified path '{path}' does not exist.")

        # Create folders
        for i in range(1, num_folders + 1):
            folder_name = f"{name_folders}{i}"
            folder_path = os.path.join(path, folder_name)

            # Check if the folder already exists
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                print(f"Folder '{folder_name}' created successfully in {path}")
            else:
                print(f"Folder '{folder_name}' already exists in {path}. Skipping.")

        print(f"{num_folders} folders created or skipped successfully in {path}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Get input from the user
    path = input("Enter the path where you want to create folders from Desktop: ")
    desktop_path = os.path.expanduser("~/Desktop")
    path = os.path.join(desktop_path, path)
    name_folders = input("Enter the base name of the folders: ")
    num_folders = int(input("Enter the number of folders to create: "))

    # Call the function to create folders
    create_folders(path, name_folders, num_folders)
