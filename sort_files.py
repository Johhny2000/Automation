import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

# Function to sort files by extension in file name
def sort_by_extension(source_folder, ignore_list):
    for file in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file)
        if os.path.isfile(file_path) and file not in ignore_list:
            ext = file.split('.')[-1]
            ext_folder = os.path.join(source_folder, ext)
            os.makedirs(ext_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(ext_folder, file))

# Function to sort files by category
def sort_by_category(source_folder, ignore_list):
    categories = {
        "music": ['mp3', 'wav', 'flac'],
        "videos": ['mp4', 'mkv', 'avi'],
        "pictures": ['png', 'jpeg', 'jpg', 'gif']
    }
    for file in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file)
        if os.path.isfile(file_path) and file not in ignore_list:
            ext = file.split('.')[-1]
            for category, extensions in categories.items():
                if ext in extensions:
                    category_folder = os.path.join(source_folder, category)
                    os.makedirs(category_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(category_folder, file))
                    break

# Function to unsort files (move files back to the source folder and delete subfolders)
def unsort_files():
    source_folder = source_folder_var.get()
    if not source_folder:
        messagebox.showerror("Error", "Please select a source folder.")
        return

    for root_dir, dirs, files in os.walk(source_folder, topdown=False):
        for file in files:
            file_path = os.path.join(root_dir, file)
            shutil.move(file_path, source_folder)
        for dir in dirs:
            os.rmdir(os.path.join(root_dir, dir))

    messagebox.showinfo("Success", "Unsorting completed!")

# Function to handle sorting
def start_sorting():
    source_folder = source_folder_var.get()
    if not source_folder:
        messagebox.showerror("Error", "Please select a source folder.")
        return

    ignore_list = [ignore_listbox.get(idx) for idx in ignore_listbox.curselection()]
    sort_option = sort_option_var.get()

    if sort_option == "By File Names":
        sort_by_extension(source_folder, ignore_list)
    elif sort_option == "By Categories":
        sort_by_category(source_folder, ignore_list)
    else:
        messagebox.showerror("Error", "Please select a sorting option.")
        return

    messagebox.showinfo("Success", "Sorting completed!")

# Function to select source folder
def select_source_folder():
    folder = filedialog.askdirectory(title="Select Source Folder")
    if folder:
        source_folder_var.set(folder)
        update_file_list(folder)

# Function to update file list in the ignore listbox
def update_file_list(folder):
    ignore_listbox.delete(0, tk.END)
    for file in os.listdir(folder):
        if os.path.isfile(os.path.join(folder, file)):
            ignore_listbox.insert(tk.END, file)

# Main GUI
root = tk.Tk()
root.title("File Sorter")

# Source folder selection
source_folder_var = tk.StringVar()
tk.Label(root, text="Source Folder:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
tk.Entry(root, textvariable=source_folder_var, width=50, state="readonly").grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=select_source_folder).grid(row=0, column=2, padx=10, pady=5)

# Ignore list
tk.Label(root, text="Ignore List:").grid(row=1, column=0, padx=10, pady=5, sticky="nw")
ignore_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, height=10, width=50)
ignore_listbox.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# Sorting options
tk.Label(root, text="Sorting Option:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
sort_option_var = tk.StringVar(value="By File Names")
ttk.Radiobutton(root, text="By File Names (jpg, png, etc.)", variable=sort_option_var, value="By File Names").grid(row=2, column=1, padx=10, pady=5, sticky="w")
ttk.Radiobutton(root, text="By Categories (music, videos, pictures)", variable=sort_option_var, value="By Categories").grid(row=3, column=1, padx=10, pady=5, sticky="w")

# Start sorting button
tk.Button(root, text="Start Sorting", command=start_sorting).grid(row=4, column=1, padx=10, pady=10)

# Unsort button
tk.Button(root, text="Unsort", command=unsort_files).grid(row=5, column=1, padx=10, pady=10)

root.mainloop()