import os
from tkinter import *
from tkinter import filedialog
# auto-py-to-exe


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")


def open_path_selector():
    selected_path = filedialog.askdirectory()
    textbox1.delete(0, END)  # Clear any previous content
    textbox1.insert(0, selected_path)


def create_folders_from_gui():
    try:
        path = textbox1.get()
        name_folders = textbox2.get()
        num_folders = int(textbox3.get())

        # Call the function to create folders
        create_folders(path, name_folders, num_folders)
    except Exception as e:
        print(f"An error occurred: {e}")


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


# Create the main window
root = Tk()
root.title("Create files/folders")

# Set the size of the window
window_width = 360
window_height = 110
center_window(root, window_width, window_height)

# Add labels to the left side
label1 = Label(root, text="Choose folder location: ")
label2 = Label(root, text="Enter base name: ")
label3 = Label(root, text="Enter number of folders: ")

label1.grid(row=0, column=0, sticky="w")
label2.grid(row=1, column=0, sticky="w")
label3.grid(row=2, column=0, sticky="w")

# Add textboxes to the right
textbox1 = Entry(root)
textbox2 = Entry(root)
textbox3 = Entry(root)

textbox1.grid(row=0, column=1)
textbox2.grid(row=1, column=1)
textbox3.grid(row=2, column=1)

# Add a button to open the path selector
button_path_selector = Button(root, text="Select Path", command=open_path_selector)
button_path_selector.grid(row=0, column=2)

# Add a button to create folders
button_create_folders = Button(root, text="Create Folders", command=create_folders_from_gui)
button_create_folders.grid(row=3, column=1, padx=5, pady=5)

# Start the Tkinter event loop
root.mainloop()
