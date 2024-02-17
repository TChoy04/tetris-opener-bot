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
    time.sleep(random.random()*0.05)

def press_up():
    pyautogui.press("up")
    time.sleep(random.random()*0.1)
def press_right():
    pyautogui.press("right")
    time.sleep(random.random()*0.08)

def press_space():
    pyautogui.press("space")
    time.sleep(random.random() * 0.1)

def press_down():
    pyautogui.keyDown("down")
    time.sleep(random.random() * 0.5)
    pyautogui.keyUp("down")
    time.sleep(random.random() * 0.2)

def first_bag():
    try:
        if pyautogui.locateOnScreen('../images/I.png',region=(875,70,200,100), confidence=0.7) != None:
            press_up()
            for _ in range(6):
                press_right()
            press_space()
            time.sleep(0.5)
            return 0
    except:
        pass
    try:
        if pyautogui.locateOnScreen('../images/O.png', region=(875, 70, 200, 100), confidence=0.7) != None:
            for _ in range(5):
                press_left()
            press_space()
            time.sleep(0.5)
            return 0
    except:
        pass
    try:
        if pyautogui.locateOnScreen('../images/L.png', region=(875, 70, 200, 100), confidence=0.8) != None:
            print("L found")
            press_up()
            press_down()
            press_right()
            press_down()
            press_up()
            press_right()
            press_right()
            press_space()
            time.sleep(0.5)
            return 0
    except:
        pass

def main():
    while 1:
        time.sleep(0.5)
        first_bag()

if __name__ == "__main__":
    main()