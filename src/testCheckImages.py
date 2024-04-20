import pydirectinput
import time
import pyautogui
import os
import sys
import logging
import logging.config
import json


def check_one_image(image_path):
    try:
        location = pyautogui.locateCenterOnScreen(image_path, confidence=0.8)
        if location:
            return True
    except pyautogui.ImageNotFoundException:
        pass
    return False


def loop(image_path):
    loopCount = 0
    while True:
        loopCount += 1
        found_pic = check_one_image(image_path)
        if found_pic:
            print("找到了")
            break
        print(loopCount, ":没找到,等待五秒重新寻找...")
        time.sleep(5)

def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        # 如果程序被打包成了单个文件
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# test_image_paths = "D:\\GitHub\\calabiqiu-auto\\src\\images\\test.png"
test_image_paths = resource_path('images\\test.png')
print(test_image_paths)

def main_loop():
    loop(test_image_paths)


def main():
    # 运行主循环
    main_loop()


if __name__ == "__main__":
    main()
