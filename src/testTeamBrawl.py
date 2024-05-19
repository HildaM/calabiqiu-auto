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
    resource_path('images\\m-45.png'),
    resource_path('images\\m-46.png'),
    resource_path('images\\m-47.png'),
    resource_path('images\\m-48.png'),
    resource_path('images\\m-49.png')
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


exception_game_start_image_lists = [
    {"code": 2, "image_paths": start_image_paths,
        "description": "对局开始:等待超过10min，开始",
        "x1": 960, "y1": 980, "clickStep": 1},
]
exception_game_enter_image_lists = [
    {"code": 1, "image_paths": enter_image_paths,
     "description": "对局开始:玩家未准备，进入链接",
     "x1": 970, "y1": 920, "clickStep": 1},
    {"code": 3, "image_paths": ensure_image_paths,
     "description": "对局开始:有玩家无法连接至服务器，对局终止，确定",
     "x1": 963, "y1": 695, "clickStep": 1},
    {"code": 2, "image_paths": start_image_paths,
     "description": "对局开始:有玩家无法连接至服务器，对局终止，开始",
     "x1": 960, "y1": 980, "clickStep": 1},
]
exception_game_over_image_paths = [
    {"code": 1, "image_paths": back_image_paths,
        "description": "对局结束:30级以前的升级检测，返回",
        "x1": 800, "y1": 970, "clickStep": 1},
    {"code": 2, "image_paths": close_image_paths,
        "description": "对局结束:30级之后的升级检测，关闭",
        "x1": 960, "y1": 970, "clickStep": 1},
    {"code": 3, "image_paths": ensure_image_paths,
        "description": "挂机检测,确认 ",
        "x1": 945, "y1": 676, "clickStep": 1}
]

def handlingExceptions(exception_image_lists):
    print("自动检查异常情况开始......")
    for image_lists in exception_image_lists:
        for image_path in image_lists.get("image_paths"):
            try:
                location = pyautogui.locateCenterOnScreen(image_path, minSearchTime=1, confidence=0.8)
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
            time.sleep(0.5)
    print("自动检查异常情况结束，没有异常出现")


# 循环查找图像的像素匹配度
def loopList(image_list, loop_times, confidence, description, x, y, sleepTime,
             pictureLocation=True, exceptions=False, randomMove=False, exception_image_lists=None):
    if exception_image_lists is None:
        exception_image_lists = []
    print(f"{description}")
    time.sleep(sleepTime)
    loopListCount = 0
    findThePic = False
    while True:
        loopListCount += 1
        if loopListCount >= loop_times:
            print(f"循环超过{loop_times}次，尝试点击默认位置({x},{y})，处理失败则跳出循环")
            pydirectinput.moveTo(x, y)
            pydirectinput.click()
            break
        for image_path in image_list:
            try:
                if exceptions:
                    handlingExceptions(exception_image_lists)
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

def pressSkillKeys(pressTimes):
    print("循环按下 Q 键")
    count = 0
    for i in range(pressTimes):
        count += 1
        pydirectinput.press('q')
        # 添加一点延迟，以防止按键速度过快
        time.sleep(0.05)
        print(f"Q 键按压次数：{count}")
    print("按下 Q 键结束")

def main():
    print('卡拉彼丘团队乱斗脚本启动中...')
    print('请位于团队乱斗的准备界面')
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
        loopList(start_image_paths,
                 50, 0.8, "1.自动点击开始按钮", 960, 980, 5, True)

        # Exception:可能的无法连接、未准备、超过10min
        loopList(enter_image_paths,
                 120, 0.8, "2.自动点击进入链接", 970, 920, 5, True,
                 True, False, exception_game_start_image_lists)

        loopList(ao_image_paths,
                 50, 0.8, "3.自动点击奥黛丽", 575, 996, 5, True,
                 True, False, exception_game_enter_image_lists)
        loopList(lock_image_paths,
                 50, 0.8, "4.自动点击锁定", 918, 779, 5, True)
        print("对局没有哪么快结束，先睡60s")
        time.sleep(60)
        print("已经睡了60s,结束睡眠")
        pressSkillKeys(300)
        loopList(nums_image_paths,
                 50, 0.9, "5.图像识别上方比分45-50", 800, 970, 3, True)
        # Exception:可能的升级和挂机检测
        loopList(next_image_paths,
                 50, 0.8, "6.下一步", 1588, 1000, 5, True,
                 True, True, exception_game_over_image_paths)
        loopList(next_image_paths,
                 50, 0.8, "7.下一步", 1588, 1000, 5, True)
        loopList(leave_image_paths,
                 50, 0.8, "8.离开", 1588, 1000, 5, True)
        print("结束本次卡拉比丘对战")


if __name__ == "__main__":
    main()
