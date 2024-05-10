import pydirectinput
import time
import pyautogui
import os
import logging
import logging.config
import json
import sys


def main():
    time.sleep(3)
    pydirectinput.moveTo(800, 970)
    pydirectinput.click()
    time.sleep(0.5)
    pydirectinput.click()
    time.sleep(0.5)
    pydirectinput.click()
    time.sleep(3)
    pydirectinput.moveTo(960, 970)
    pydirectinput.click()
    time.sleep(0.5)
    pydirectinput.click()
    time.sleep(0.5)
    pydirectinput.click()

if __name__ == '__main__':
    main()