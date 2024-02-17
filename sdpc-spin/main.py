from pyautogui import *
import pyautogui
import time
import keyboard
import random
import random
import win32api, win32con
import pydirectinput

FIRST_O = False
FIRST_S = False
DELAYED_RED = False
def press_left():
    pyautogui.press("left")
    time.sleep(random.random()*0.05)

def press_up():
    pyautogui.press("up")
    time.sleep(random.random()*0.1)
def press_right():
    pyautogui.press("right")
    time.sleep(random.random()*0.05)

def press_space():
    pyautogui.press("space")
    time.sleep(random.random() * 0.05)

def press_down():
    pyautogui.keyDown("down")
    time.sleep(random.random() * 0.1)
    pyautogui.keyUp("down")
    time.sleep(random.random() * 0.07)
def press_z():
    pyautogui.press("z")
    time.sleep(random.random() * 0.07)
def press_c():
    pyautogui.press("c")
    time.sleep(random.random() * 0.06)

def first_bag():
    try:
        if pyautogui.locateOnScreen('../images/I.png',region=(825,70,300,100), confidence=0.7) != None:

            press_up()
            for _ in range(6):
                press_right()
            press_space()
            time.sleep(0.5)
            return 0
    except:
        pass
    try:
        if pyautogui.locateOnScreen('../images/s.png', region=(825, 70, 300, 100), confidence=0.8) != None:

            global FIRST_S
            FIRST_S = True
            press_left()
            press_space()
    except:
        pass
    try:
        if pyautogui.locateOnScreen('../images/O.png', region=(825, 70, 300, 100), confidence=0.7) != None:
            global FIRST_O
            FIRST_O = True

            for _ in range(5):
                press_left()
            press_space()
            time.sleep(0.5)
            return 0
    except:
        pass
    try:
        if pyautogui.locateOnScreen('../images/J.png', region=(825, 70, 300, 100), confidence=0.8) != None:
            press_up()
            press_down()
            press_right()
            press_down()
            press_up()
            if FIRST_S != True:
                press_right()
            press_space()
            time.sleep(0.5)
            return 0
    except:
        pass
    try:
        if pyautogui.locateOnScreen('../images/L.png', region=(825, 70, 300, 100), confidence=0.8) != None:
            press_z()
            for _ in range(6):
                press_right()
            press_left()
            press_space()
            return 0
    except:
        pass
    try:
        if pyautogui.locateOnScreen('../images/Z.png', region=(825, 70, 300, 100), confidence=0.7) != None:
            if(FIRST_O != True):
                print("O not down yet!")
                press_c()
                return 0
            press_z()
            for _ in range(5):
                press_left()
            press_space()
            time.sleep(0.5)
            return 0
    except:

        pass


def main():
    while 1:
        first_bag()


if __name__ == "__main__":
    main()