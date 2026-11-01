import time

import keyboard
import pydirectinput

TARGET_KEY = 'e'      
TOGGLE_KEY = 'f1'      
DELAY = 0.05     

is_running = False

def toggle_clicking():
    global is_running
    is_running = not is_running
    if is_running:
        print("autoclicker runned!")
    else:
        print("autoclicker on pause")

keyboard.add_hotkey(TOGGLE_KEY, toggle_clicking)

print('ready')

try:
    while True:
        if is_running:
            pydirectinput.keyDown(TARGET_KEY)
            time.sleep(0.01)
            pydirectinput.keyUp(TARGET_KEY)
            
            time.sleep(DELAY)
        else:
            time.sleep(0.1)
except KeyboardInterrupt:
    print("\nShutdown!")
