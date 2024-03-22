import time
from tkinter import *
import pyautogui as py
import threading


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")


def check_value():
    return var_scroll_down.get()

def scroll_down():
    print("Enter function")
    value = var_scroll_down.get() == 1
    while value:
        print("In function")
        py.scroll(-12)
        time.sleep(0.5)
        value = check_value()


# Create the main window
root = Tk()
root.title("Page Tools")

# Set the size of the window
window_width = 300
window_height = 300
center_window(root, window_width, window_height)


# Add labels & check-buttons
# Checkbutton row 1
var_scroll_down = IntVar()  # Save as integer
check_scroll_down = Checkbutton(root, variable=var_scroll_down, text="Scroll down", onvalue=1, offvalue=0, command=scroll_down)
check_scroll_down.grid(row=0, column=0, sticky=W)
scroll_down()

var_auto_read = IntVar()
check_auto_read = Checkbutton(root, variable=var_auto_read, text="Autoread", onvalue=1, offvalue=0)
check_auto_read.grid(row=0, column=1, sticky=W)


# Checkbutton 2
check_save_text = Checkbutton(root, text="Save text")
check_save_text.grid(row=1, column=0, sticky=W)
check_save_pic = Checkbutton(root, text="Save pic")
check_save_pic.grid(row=1, column=1, sticky=W)

# Checkbutton 3
check_log_page = Checkbutton(root, text="Log pages")
check_log_page.grid(row=2, column=0, sticky=W)
check_log_page.select()

# Set start button
start = Button(root, text="Start", width=10, padx=2)
start.grid(row=4, column=0)

# Main loop
root.mainloop()


