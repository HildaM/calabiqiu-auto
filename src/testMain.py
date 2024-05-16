# -*- coding: utf-8 -*-
import pydirectinput
import time
import pyautogui
import os
import sys

class Logger(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


path = os.path.abspath(os.path.dirname(__file__))
type = sys.getfilesystemencoding()
sys.stdout = Logger('calabiqiuAuto.txt')

# 获取资源的绝对路径，用于PyInstaller打包后资源的访问
def resource_path(relative_path):
    # 是否Bundle Resource
    if getattr(sys, ' frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# 禁用自动停止
pyautogui.FAILSAFE = False

# 设置当前工作目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 图像导入
start_image_paths = [
    resource_path('images\\start1.png'),
    resource_path('images\\start2.png')
]
enter_image_paths = [resource_path('images\\enter.png')]
ao_image_paths = [resource_path('images\\ao.png')]
lock_image_paths = [
    resource_path('images\\lock1.png'),
    resource_path('images\\lock2.png')
]
nums_image_paths = [
    resource_path('images\\r-45.png'),
    resource_path('images\\r-46.png'),
    resource_path('images\\r-47.png'),
    resource_path('images\\r-48.png'),
    resource_path('images\\r-49.png'),
    resource_path('images\\b-45.png'),
    resource_path('images\\b-46.png'),
    resource_path('images\\b-47.png'),
    resource_path('images\\b-48.png'),
    resource_path('images\\b-49.png'),
]
back_image_paths = [
    resource_path('images\\back1.png'),
    resource_path('images\\back2.png')
]
close_image_paths = [
    resource_path('images\\close1.png'),
    resource_path('images\\close2.png'),
    resource_path('images\\close3.png'),
    resource_path('images\\close4.png')
]
next_image_paths = [
    resource_path('images\\next.png'),
    resource_path('images\\next2.png')
]
leave_image_paths = [
    resource_path('images\\leave1.png'),
    resource_path('images\\leave2.png'),
]
ensure_image_paths = [
    resource_path('images\\ensure1.png')
]
exception_image_lists = [
    {"code": 1, "image_paths": back_image_paths,
     "description": "对局结束:30级以前的升级检测，需要点击返回",
     "x1": 800, "y1": 970, "clickStep": 1},
    {"code": 2, "image_paths": close_image_paths,
     "description": "对局结束:30级之后的升级检测，需要点击关闭",
     "x1": 960, "y1": 970, "clickStep": 1},
    {"code": 3, "image_paths": ensure_image_paths,
     "description": "对局开始:有玩家无法连接至服务器，对局终止，需要点击确定后,点击开始,并点击进入链接 "
                    "|| 挂机检测,需要点击确认 ",
     "x1": 963, "y1": 695, "x2": 960, "y2": 980, "x3": 970, "y3": 920, "x4": 945, "y4": 676,  "clickStep": 4},
    {"code": 4, "image_paths": enter_image_paths,
     "description": "对局开始:玩家未准备，需要重新点击进入链接",
     "x1": 970, "y1": 920, "clickStep": 1},
    {"code": 5, "image_paths": start_image_paths,
     "description": "对局开始:等待超过10min，需要重新点击开始,重新点击进入链接",
     "x1": 960, "y1": 980, "x2": 970, "y2": 920, "clickStep": 2}
]

def handlingExceptions():
    for image_lists in exception_image_lists:
        for image_path in image_lists.get("image_paths"):
            try:
                location = pyautogui.locateCenterOnScreen(image_path, minSearchTime=5, confidence=0.8)
                if location:
                    print(f"错误代码：{image_lists.get("code")},"
                          f"找到了{image_lists.get("description")}，")
                    for i in range(1, image_lists.get("clickStep")+1):
                        print(f"默认点击坐标为({image_lists.get("x"+str(i))},{image_lists.get("y"+str(i))})")
                        pydirectinput.moveTo(image_lists.get("x"+str(i)), image_lists.get("y"+str(i)))
                        pydirectinput.click()
                        time.sleep(1)
                    return
            except pyautogui.ImageNotFoundException:
                pass
            # print(f"没找到下列异常：{image_lists.get("description")}")
    print("没有异常出现")

# 获取x和y坐标
def check_one_image_location(image_path):
    try:
        location = pyautogui.locateCenterOnScreen(image_path, minSearchTime=5, confidence=0.8)
        if location:
            return location
    except pyautogui.ImageNotFoundException:
        pass
    return False

# 循环查找图像的像素匹配度
def loopList(image_list, loop_times, confidence, description, x, y, sleepTime,
             pictureLocation=True, exceptions=False, randomMove=False):
    print(f"{description}")
    time.sleep(sleepTime)
    loopListCount = 0
    findThePic = False
    while True:
        loopListCount += 1
        if loopListCount >= loop_times:
            print(f"循环超过{loop_times}次，尝试处理异常，处理失败则跳出循环")
            if exceptions:
                handlingExceptions()
            break
        for image_path in image_list:
            try:
                location = pyautogui.locateCenterOnScreen(image_path, minSearchTime=5, confidence=confidence)
                if location:
                    if pictureLocation:
                        print(f"找到了{description}，坐标为({location.x},{location.y})")
                        pydirectinput.moveTo(location.x, location.y)
                        pydirectinput.click()
                        findThePic = True
                        break
                    else:
                        print(f"找到了{description}，默认点击坐标为({x},{y})")
                        pydirectinput.moveTo(x, y)
                        pydirectinput.click()
                        break
                if exceptions:
                    handlingExceptions()
            except pyautogui.ImageNotFoundException:
                pass
        print(f"第{loopListCount}次寻找:没找到{description},等待{sleepTime}秒重新寻找...")
        if findThePic:
            print(f"{description}完毕")
            return
        if randomMove:
            print("保持运动等待游戏结束")
            pydirectinput.press('w')
            pydirectinput.moveTo(800, 970)
            pydirectinput.click()
        time.sleep(sleepTime)

def main():
    print('脚本启动中...')
    print('启动完成')
    scriptPlayTimesCount = 0
    while True:  # 无限循环
        # 自动点击开始按钮：开1，开2
        scriptPlayTimesCount += 1
        print("   ____           _           _       _           _         ")
        print("  / ___|   __ _  | |   __ _  | |__   (_)   __ _  (_)  _   _ ")
        print(" | |      / _` | | |  / _` | | '_ \\  | |  / _` | | | | | | |")
        print(" | |___  | (_| | | | | (_| | | |_) | | | | (_| | | | | |_| |")
        print("  \\____|  \\__,_| |_|  \\__,_| |_.__/  |_|  \\__, | |_|  \\__,_|")
        print("                                             |_|            ")
        print(f"第{scriptPlayTimesCount}次对战,当前时间为{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")
        loopList(start_image_paths, 50, 0.8, "自动点击开始按钮", 960, 980, 5, True)
        # Exception:可能的无法连接、未准备、超过10min
        loopList(enter_image_paths, 120, 0.8, "自动点击进入链接", 970, 920, 5, True, True)
        loopList(ao_image_paths, 50, 0.8, "自动点击奥黛丽", 575, 996, 5, True)
        loopList(lock_image_paths, 50, 0.8, "自动点击锁定", 918, 779, 5, True)
        print("对局没有哪么快结束，先睡180s")
        time.sleep(180)
        print("已经睡了180s,结束睡眠")
        loopList(nums_image_paths, 50, 0.9, "图像识别上方比分45-50", 800, 970, 3, True)
        # Exception:可能的升级和挂机检测
        loopList(next_image_paths, 50, 0.8, "下一步", 1588, 1000, 5, True, True, True)
        loopList(next_image_paths, 50, 0.8, "下一步", 1588, 1000, 5, True, True)
        loopList(leave_image_paths, 50, 0.8, "离开", 1588, 1000, 5, True, True)
        print("结束本次卡拉比丘对战")


if __name__ == "__main__":
    main()
