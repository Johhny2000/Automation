import threading
import time
from pynput import keyboard
import pyautogui


def check_key(stop_event):
    """Monitor if the 'q' key is being held down."""
    def on_press(key):
        try:
            if key.char == 'q':
                print("'q' key pressed. Exiting...")
                stop_event.set()
        except AttributeError:
            pass

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


def check_image(image_path, stop_event):
    """Continuously checks a specific area for a matching image."""
    screen_width, screen_height = pyautogui.size()
    search_area = (
        100,
        100,
        400,
        250,
    )

    while not stop_event.is_set():
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)
            if location:
                print("Image found! Reloading page...")
                pyautogui.hotkey('ctrl', 'r')
                time.sleep(10)  # Add a delay to prevent repeated reloads

                # Click in the middle of the screen after reload
                pyautogui.moveTo(screen_width // 2, screen_height // 2)
                pyautogui.click()
                print("Started.")
        except Exception as e:
            pass

        time.sleep(0.3)  # Slight delay to reduce CPU usage


if __name__ == "__main__":
    image_to_find = "C:/Users/37251/Desktop/Folders/Find pics/Reload/error_img.png"

    # Create a stop event to coordinate thread termination
    stop_event = threading.Event()

    # Start the key monitoring thread
    key_thread = threading.Thread(target=check_key, args=(stop_event,), daemon=True)
    key_thread.start()

    # Start the image checking thread
    image_thread = threading.Thread(target=check_image, args=(image_to_find, stop_event), daemon=True)
    image_thread.start()

    # Keep the main thread alive until stop_event is set
    try:
        while not stop_event.is_set():
            time.sleep(1)
    except KeyboardInterrupt:
        print("Keyboard interrupt received. Exiting...")
        stop_event.set()
