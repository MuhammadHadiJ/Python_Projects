import time
import threading
import random
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

Activate_Key = KeyCode(char="x")
Clicking = False
mouse = Controller()

def clicker():
    while True:
        if Clicking == True:
            mouse.click(Button.left)
        time.sleep(random.randint(270,372))

def Activation(key):
    if key == Activate_Key:
        global Clicking
        Clicking = not Clicking


click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=Activation) as listener:
    listener.join()