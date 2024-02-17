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
                pyautogui.press("z")
                time.sleep(1)

        except:
            print("bye")
            time.sleep(1)

if __name__ == "__main__":
    main()