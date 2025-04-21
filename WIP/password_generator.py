'''
Create a random password with GUI and options
'''
from tkinter import *
import random


def generate_password():
    a_list = ["Apple","Beer","Chocolate"]
    b_list = ["Drink","Elevate","Farm"]

    password = f"{random.choice(a_list)}{random.choice(b_list)}{random.randint(0, 9)}"
    return password


if __name__ == "__main__":
    root = Tk()
    root.title("Create password")

    # Set the size of the window
    window_width = 360
    window_height = 110

    # Add labels to the left side
    label1 = Label(root, text="Choose folder location: ")

    label1.grid(row=0, column=0, sticky="w")

    checkbox = Checkbutton(root, text="Noun")

    # Add textboxes to the right
    textbox1 = Entry(root)

    textbox1.grid(row=0, column=1)
    root.mainloop()

    # print(generate_password())
