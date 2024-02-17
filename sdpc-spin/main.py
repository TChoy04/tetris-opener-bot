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

def press_up():
    pyautogui.press("up")
    time.sleep(random.random()*0.12)
def press_right():
    pyautogui.press("right")
    time.sleep(random.random()*0.18)

def press_space():
    pyautogui.press("space")
    time.sleep(random.random()*0.15)

def press_down():
    pyautogui.press("down")
    time.sleep(random.random() * 0.17)

FIRST_MOVE = True
def check_first_move(first_move):
    if(first_move == True):
        FIRST_MOVE = False
        pyautogui.press("c")
    else:
        press_space()
def first_bag():
    try:
        if pyautogui.locateOnScreen('../images/T.png', confidence=0.95) != None:
            check_first_move(FIRST_MOVE)
            for _ in range(5):
                press_left()
    except:
        print("a")
    try:
        if pyautogui.locateOnScreen('../images/O.png',confidence=0.95) != None:
            check_first_move(FIRST_MOVE)
            for _ in range(5):
                press_left()
    except:
        try:
            if pyautogui.locateOnScreen('../images/L.png', confidence=0.95) != None:
                check_first_move(FIRST_MOVE)
                press_right()
                press_up()
                press_down()
                press_up()
                press_right()
        except:
            try:
                if pyautogui.locateOnScreen('../images/I.png', confidence=0.95) != None:
                    check_first_move(FIRST_MOVE)
                    press_up()
                    for _ in range(6):
                        press_right()

            except:
                print("a")


    return 0
def main():
    # time.sleep(3)
    # for _ in range(8):
    #     first_bag()
    #     time.sleep(0.5)
    time.sleep(5)
    pyautogui.screenshot('full_screen.png')

if __name__ == "__main__":
    main()