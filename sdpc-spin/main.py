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
FIRST_L = False
FIRST_J = False
FIRST_Z = False
FIRST_I = False
DELAYED_RED = False
SECOND_BAG = {"O":False,"S":False,"L":False,"J":False,"Z":False,"I":False}
def press_left():
    pyautogui.press("left")
    time.sleep(random.random()*0.005)

def press_up():
    pyautogui.press("up")
    time.sleep(random.random()*0.003)
def press_right():
    pyautogui.press("right")
    time.sleep(random.random()*0.005)

def press_space():
    pyautogui.press("space")
    time.sleep(random.random() * 0.005)

def press_down():
    pyautogui.keyDown("down")
    time.sleep(random.random() * 0.003)
    pyautogui.keyUp("down")
    time.sleep(random.random() * 0.007)
def press_z():
    pyautogui.press("z")
    time.sleep(random.random() * 0.004)
def press_c():
    pyautogui.press("c")
    time.sleep(random.random() * 0.002)

def first_bag():
    global FIRST_I, FIRST_J, FIRST_L, FIRST_Z, FIRST_S, FIRST_O, DELAYED_RED
    try:
        if pyautogui.locateOnScreen('../images/I.png',region=(825,70,300,100), confidence=0.7) != None:
            FIRST_I = True
            press_up()
            for _ in range(6):
                press_right()
            press_space()
            return 0
    except:
        pass
    try:
        if pyautogui.locateOnScreen('../images/s.png', region=(825, 70, 300, 100), confidence=0.7) != None:
            FIRST_S = True
            press_left()
            press_space()
            return 0
    except:
        pass
    try:
        if pyautogui.locateOnScreen('../images/O.png', region=(825, 70, 300, 100), confidence=0.7) != None:
            FIRST_O = True

            for _ in range(5):
                press_left()
            press_space()
            return 0
    except:
        pass
    try:
        if pyautogui.locateOnScreen('../images/J.png', region=(825, 70, 300, 100), confidence=0.8) != None:
            FIRST_J = True
            press_up()
            press_down()
            press_right()
            press_down()
            press_up()
            if FIRST_S != True:
                press_right()
            press_space()
            return 0
    except:
        pass
    try:
        if pyautogui.locateOnScreen('../images/L.png', region=(825, 70, 300, 100), confidence=0.8) != None:
            FIRST_L = True
            press_z()
            for _ in range(4):
                press_right()
            press_space()
            return 0
    except:
        pass
    try:
        if pyautogui.locateOnScreen('../images/Z.png', region=(825, 70, 300, 100), confidence=0.7) != None or (DELAYED_RED == True and FIRST_O):
            if(FIRST_O != True):
                print("O not down yet!")
                DELAYED_RED = True
                press_c()
                return 0
            FIRST_Z = True
            press_z()
            for _ in range(5):
                press_left()
            press_space()
            return 0
    except:
        pass
    try:
        if pyautogui.locateOnScreen('../images/T.png', region=(825, 70, 300, 100), confidence=0.7) != None:
            press_c()
            return 0
    except:
        pass

def first_T_Drop():
    press_c()
    press_up()
    press_left()
    press_left()
    press_down()
    press_up()
    press_space()

def second_bag():
    global SECOND_BAG
    try:
        if pyautogui.locateOnScreen('../images/s.png', region=(825, 70, 300, 100), confidence=0.7) != None:
            SECOND_BAG["S"] = True
            press_up()
            press_down()
            press_z()
            press_space()
            return 0
    except:
        pass
    try:
        if pyautogui.locateOnScreen('../images/L.png', region=(825, 70, 300, 100), confidence=0.7) != None:
            SECOND_BAG["L"] = True
            press_up()
            for _ in range(4):
                press_right()
            press_space()
            return 0
    except:
        pass
    try:
        if pyautogui.locateOnScreen('../images/T.png', region=(825, 70, 300, 100), confidence=0.7) != None:
            press_c()
            return 0
    except:
        pass
    try:
        if pyautogui.locateOnScreen('../images/O.png', region=(825, 70, 300, 100), confidence=0.7) != None:
            SECOND_BAG["O"] = True
            for _ in range(3):
                press_left()
            press_space()
            return 0
    except:
        pass
    try:
        if pyautogui.locateOnScreen('../images/J.png', region=(825, 70, 300, 100), confidence=0.7) != None:
            SECOND_BAG["J"] = True
            for _ in range(2):
                press_right()
            press_down()
            press_right()
            press_space()
            return 0
    except:
        pass
    try:
        if pyautogui.locateOnScreen('../images/I.png', region=(825, 70, 300, 100), confidence=0.7) != None:
            SECOND_BAG["I"] = True
            press_z()
            for _ in range(4):
                press_left()
            press_space()
            return 0
    except:
        pass
    try:
        if pyautogui.locateOnScreen('../images/Z.png', region=(825, 70, 300, 100), confidence=0.7) != None:
            SECOND_BAG["Z"] = True
            press_z()
            press_down()
            press_left()
            press_space()
            return 0
    except:
        pass
def second_T_Drop():
    press_up()
    press_down()
    press_up()
    press_space()

def third_bag():
    try:
        if pyautogui.locateOnScreen('../images/I.png', region=(825, 70, 300, 100), confidence=0.7) != None:

            press_z()
            for _ in range(5):
                press_right()
            press_space()
            return 0
    except:
        pass
    try:
        if pyautogui.locateOnScreen('../images/L.png', region=(825, 70, 300, 100), confidence=0.7) != None:
            press_z()
            press_space()
            return 0
    except:
        pass
    try:
        if pyautogui.locateOnScreen('../images/J.png', region=(825, 70, 300, 100), confidence=0.7) != None:
            press_up()
            press_right()
            press_space()
            return 0
    except:
        pass
    try:
        if pyautogui.locateOnScreen('../images/S.png', region=(825, 70, 300, 100), confidence=0.7) != None:
            SECOND_BAG["Z"] = True
            press_z()
            for _ in range(4):
                press_right()
            press_space()
            return 0
    except:
        pass
def main():
    global FIRST_I, FIRST_J, FIRST_L, FIRST_Z, FIRST_S, FIRST_O
    time.sleep(3)
    while FIRST_I!= True or FIRST_J != True or FIRST_L != True or FIRST_Z != True or FIRST_S != True or FIRST_O != True:
        first_bag()
    first_T_Drop()
    while SECOND_BAG["O"]!= True or SECOND_BAG["J"] != True or SECOND_BAG["L"] != True or SECOND_BAG["Z"] != True or SECOND_BAG["S"] != True or SECOND_BAG["I"] != True:
        second_bag()
    second_T_Drop()
    while 1:
        third_bag()


if __name__ == "__main__":
    main()