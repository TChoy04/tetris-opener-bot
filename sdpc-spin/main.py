from pyautogui import *
import pyautogui
import time
import keyboard
import random
import random
import win32api, win32con


def main():
    while 1:
        try:
            if pyautogui.locateOnScreen('../images/T.png')!=None:
                print("hello")
                time.sleep(2)
        except:
            print("bye")
            time.sleep(2)

if __name__ == "__main__":
    main()