#最终解决方案：pydirectinput
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
    '../images/start1.png',
    '../images/start2.png'
]
enter_image_paths = '../images/enter.png'
ao_image_paths = '../images/ao.png'
lock_image_paths = [
    '../images/lock1.png',
    '../images/lock2.png'
]
image_paths = [
    '../images/r-45.png',
    '../images/r-46.png',
    '../images/r-47.png',
    '../images/r-48.png',
    '../images/r-49.png',
    '../images/b-45.png',
    '../images/b-46.png',
    '../images/b-47.png',
    '../images/b-48.png',
    '../images/b-49.png'
]
next_image_paths = '../images/next.png'


# 检查图像


def check_one_image(image_path):
    try:
        location = pyautogui.locateCenterOnScreen(image_path, confidence=0.8)
        if location:
            return True
    except pyautogui.ImageNotFoundException:
        pass
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
        try:
            location = pyautogui.locateCenterOnScreen(image_path, confidence=0.8)
            if location:
                return True
        except pyautogui.ImageNotFoundException:
            pass
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
def main_loop():
    print("循环启动脚本")
    count = 0
    while True:  # 无限循环
        # 自动点击开始按钮：开1，开2
        count += 1
        print("第",count,"次对战")     
        print("###################################")
        print("自动点击开始按钮")
        time.sleep(3)
        loopList(start_image_paths)
        pydirectinput.moveTo(960, 980)
        pydirectinput.click()
        print("自动点击开始按钮完毕")
        print("###################################")

        # 自动点击进入链接：进  debugger
        print("自动点击进入链接")
        time.sleep(3)
        loop(enter_image_paths)
        pydirectinput.moveTo(970, 920)
        pydirectinput.click()
        time.sleep(0.5)
        pydirectinput.click()
        time.sleep(0.5)
        pydirectinput.click()
        print("自动点击进入链接完毕")
        print("###################################")

        # 自动选择奥黛丽：头像
        print("自动选择奥黛丽")
        time.sleep(3)
        loop(ao_image_paths)
        pydirectinput.moveTo(575, 996)
        pydirectinput.click()
        time.sleep(0.5)
        pydirectinput.click()
        time.sleep(0.5)
        pydirectinput.click()
        print("自动选择奥完毕")
        print("###################################")

        # 自动选中锁定
        print("自动选中锁定")
        time.sleep(3)
        loopList(lock_image_paths)
        pydirectinput.moveTo(918, 779)
        pydirectinput.click()
        time.sleep(0.5)
        pydirectinput.click()
        time.sleep(0.5)
        pydirectinput.click()
        print("自动选中锁定完毕")
        print("###################################")

        # 对局没有哪么快结束，先睡180s
        print("对局没有哪么快结束，先睡180s")
        time.sleep(60)
        print("已经睡了60s")
        time.sleep(60)
        print("已经睡了120s")
        time.sleep(60)
        print("结束睡眠")
        print("###################################")

        # 图片路径

        # 图像识别上方比分，当到达45时候，移动人物
        # 循环搜索
        print("图像识别上方比分45-50")
        loopList(image_paths)
        print("图像识别上方比分完毕")
        print("###################################")
        # 保持运动等待游戏结束
        print("保持运动等待游戏结束")
        pydirectinput.press('w')
        pydirectinput.click()
        time.sleep(10)
        pydirectinput.press('d')
        pydirectinput.click()
        time.sleep(10)
        pydirectinput.press('w')
        pydirectinput.click()
        time.sleep(10)
        pydirectinput.press('d')
        pydirectinput.click()
        time.sleep(10)
        pydirectinput.press('w')
        pydirectinput.click()
        print("###################################")

        #图像识别：下一步
        print("图像识别：下一步")
        time.sleep(3)
        loop(next_image_paths)
        print("###################################")

        # 点击下一步，下一步，退出
        print("下一步")
        time.sleep(3)
        pydirectinput.moveTo(1628, 949)
        pydirectinput.click()
        time.sleep(3)
        pydirectinput.moveTo(1628, 949)
        pydirectinput.click()
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
        print("###################################")

# 运行主循环
main_loop()