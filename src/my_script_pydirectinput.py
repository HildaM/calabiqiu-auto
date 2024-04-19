import pyautogui
import pydirectinput
import time
import pyautogui
import os
# 禁用自动停止
pyautogui.FAILSAFE = False

# 设置当前工作目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 启动脚本延时
print('脚本启动中...')
time.sleep(3)
print('启动完成')

# 图像导入
start_image_paths = [
    'D:\\GitHub\\calabiqiu-auto\\images\\start1.png',
    'D:\\GitHub\\calabiqiu-auto\\images\\start2.png'
]
enter_image_paths = 'D:\\GitHub\\calabiqiu-auto\\images\\enter.png'
ao_image_paths = 'D:\\GitHub\\calabiqiu-auto\\images\\ao.png'
image_paths = [
    'D:\\GitHub\\calabiqiu-auto\\images\\r-45.png',
    'D:\\GitHub\\calabiqiu-auto\\images\\r-46.png',
    'D:\\GitHub\\calabiqiu-auto\\images\\r-47.png',
    'D:\\GitHub\\calabiqiu-auto\\images\\r-48.png',
    'D:\\GitHub\\calabiqiu-auto\\images\\r-49.png',
    # 'D:\\GitHub\\calabiqiu-auto\\images\\b-45.png',
    'D:\\GitHub\\calabiqiu-auto\\images\\b-46.png',
    # 'D:\\GitHub\\calabiqiu-auto\\images\\b-47.png',
    'D:\\GitHub\\calabiqiu-auto\\images\\b-48.png',
    # 'D:\\GitHub\\calabiqiu-auto\\images\\b-49.png'
]
next_image_paths = 'D:\\GitHub\\calabiqiu-auto\\images\\next.png'

# 检查图像


def check_one_image(image_path):
    location = pyautogui.locateCenterOnScreen(image_path, confidence=0.6)
    if location != None:
        return True
    else:
        return False


def loop(image_path):
    while True:
        found_pic = check_one_image(image_path)
        if found_pic:
            print("找到了")
            break
        print("没找到,等待五秒重新寻找...")
        time.sleep(5)

# 检查图像列表


def check_images(image_list):
    for image_path in image_list:
        location = pyautogui.locateCenterOnScreen(image_path, confidence=0.7)
        if location:
            return True
        else:
            return False


def loopList(image_list):
    while True:
        found_pic = check_images(image_list)
        if found_pic:
            print(f"找到了")
            break
        print("没找到,等待五秒重新寻找...")
        time.sleep(5)


# 循环启动脚本

# 自动点击开始按钮：开1，开2
print("自动点击开始按钮")
time.sleep(3)
loopList(start_image_paths)
pydirectinput.moveTo(960, 980)
pydirectinput.click()
print("自动点击开始按钮完毕")


# 自动点击进入链接：进  debugger
print("自动点击进入链接")
time.sleep(3)
loop(enter_image_paths)
pydirectinput.moveTo(970, 920)
pydirectinput.click()
print("自动点击进入链接完毕")

# 自动选择奥黛丽：头像
print("自动选择奥黛丽")
time.sleep(3)
loop(ao_image_paths)
pydirectinput.moveTo(575, 996)
pydirectinput.click()
print("自动选择奥完毕")

# 对局没有哪么快结束，先睡120s
time.sleep(120)


# 图片路径

# 图像识别上方比分，当到达45时候，移动人物
# 循环搜索
print("图像识别上方比分")
loopList(image_paths)
print("图像识别上方比分完毕")
# 保持运动等待游戏结束

print("自动选择退出")
while True:
    found_pic = check_one_image(next_image_paths)
    if found_pic:
        print("找到了")
        break
    print("对局还没有结束,等待五秒重新寻找...")
    pydirectinput.moveTo(1628, 949)
    pydirectinput.click()
    time.sleep(5)
print("自动选择退出完毕")

# 点击下一步，下一步，退出
print("退出")
time.sleep(3)
pydirectinput.moveTo(1628, 949)
pydirectinput.click()
time.sleep(3)
pydirectinput.moveTo(1628, 949)
pydirectinput.click()
time.sleep(3)
pydirectinput.moveTo(1628, 949)
pydirectinput.click()
print("退出完毕")


input()