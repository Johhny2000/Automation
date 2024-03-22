from tkinter import *
import pyautogui
from tkinter import messagebox

current_function = ""


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")


def check_value():
    return var_scroll_down.get()


def scroll_down():
    try:
        value = check_value()
        if value:
            pyautogui.scroll(-20)
            root.after(500, scroll_down)
    except Exception as e:
        messagebox.showerror("Error", str(e))
        var_scroll_down.set(0)


def on_start_button_click():
    global current_function
    if var_scroll_down.get():
        current_function = "scroll down"
        scroll_down()


def on_stop_click():
    var_scroll_down.set(0)


def create_gui():
    # Create the main window
    window = Tk()
    window.title("Page Tools")

    # Set the size of the window
    window_width = 300
    window_height = 300
    center_window(window, window_width, window_height)
    return window


def create_buttons(window):
    # Add labels & check-buttons
    # Checkbutton row 1
    global var_scroll_down
    var_scroll_down = IntVar()  # Save as integer

    check_scroll_down = Checkbutton(window, variable=var_scroll_down, text="Scroll down", onvalue=1, offvalue=0)
    check_scroll_down.grid(row=0, column=0, sticky=W)

    var_auto_read = IntVar()
    check_auto_read = Checkbutton(window, variable=var_auto_read, text="Autoread", onvalue=1, offvalue=0)
    check_auto_read.grid(row=0, column=1, sticky=W)

    # Checkbutton 2
    check_save_text = Checkbutton(window, text="Save text")
    check_save_text.grid(row=1, column=0, sticky=W)
    check_save_pic = Checkbutton(window, text="Save pic")
    check_save_pic.grid(row=1, column=1, sticky=W)

    # Checkbutton 3
    check_log_page = Checkbutton(window, text="Log pages")
    check_log_page.grid(row=2, column=0, sticky=W)
    # check_log_page.select()

    # Set start button
    start = Button(window, text="Start", width=10, padx=2, command=on_start_button_click)
    start.grid(row=4, column=0)
    # Set stop button
    stop = Button(window, text="Stop", width=10, padx=2, command=on_stop_click)
    stop.grid(row=4, column=1)


def main():
    global root
    root = create_gui()
    create_buttons(root)
    # Main loop
    root.mainloop()


if __name__ == '__main__':
    main()
