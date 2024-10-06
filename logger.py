from pynput import keyboard

keys = []

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
