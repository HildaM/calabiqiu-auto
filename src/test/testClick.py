import pydirectinput
import time
import pyautogui
import os
import logging
import logging.config
import json
import sys


def main():
    print("start")
    time.sleep(5)
    pydirectinput.moveTo(800, 970)
    pydirectinput.click()
    time.sleep(0.5)
    pydirectinput.click()
    time.sleep(0.5)
    pydirectinput.click()
    print("低于30级，升级位于左边")
    time.sleep(3)
    pydirectinput.moveTo(960, 970)
    pydirectinput.click()
    time.sleep(0.5)
    pydirectinput.click()
    time.sleep(0.5)
    pydirectinput.click()
    print("高于30级，升级位于正中间")
    print("end")
if __name__ == '__main__':
    main()