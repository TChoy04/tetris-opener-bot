from pyautogui import *
import pyautogui
import time
import keyboard
import random
import random
import win32api, win32con
import pydirectinput

def press_left():
    pyautogui.press("left")
    time.sleep(random.random()*0.1)

def press_space():
    pyautogui.press("space")
    time.sleep(random.random()*0.15)
def first_bag():

    try:
        if pyautogui.locateOnScreen('../images/O.png',confidence=0.9) != None:
            pyautogui.press("c")
            press_left()
            press_left()
            press_left()
            press_left()
            press_space()

    except:
        print("bye")
        time.sleep(1)
    return 0
def main():
    time.sleep(3)
    while(1):
        first_bag()


if __name__ == "__main__":
    main()