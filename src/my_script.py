# 实现了游戏外有效果
import pyautogui
import os
import time
from PIL import Image
import timeit

pyautogui.FAILSAFE = False  # 禁用自动停止

# 设置当前工作目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# print("修改后的工作目录:", os.getcwd())

print('等待五秒...')
time.sleep(5)  # Number of seconds
print('等待结束...')

# 使用绝对路径
start_image_path = 'D:\\GitHub\\calabiqiu-auto\\images\\start.png'
# 使用相对路径
# start_image_path = '../images/start.png'

# 屏幕快照如下
screenshot = pyautogui.screenshot()
screenshot.save(r'd:\GitHub\calabiqiu-auto\images\screenshot\screenshot.png')

try:
    # 尝试找到图片位置，设置一定的匹配容忍度
    location = pyautogui.locateCenterOnScreen(start_image_path, confidence=0.6)
except Exception as e:
    # 如果发生错误，打印错误信息
    print("在寻找图片时发生错误:", str(e))
    location = None  # 确保location被定义，即使在异常情况下


if location:
    # pyautogui.click(location)
    # pyautogui.click(x=location.x, y=location.y)
    # pyautogui.moveTo(location)
    # pyautogui.mouseDown()
    # pyautogui.mouseUp()
    print("点击start,location:")
    print(location)
    # 移动鼠标到指定位置
    pyautogui.moveTo(942, 984, duration=2)  # 在两秒内移动到指定位置
    # 等待一秒，确保你可以看到鼠标移动
    time.sleep(1)
    # 执行点击操作
    pyautogui.click()
else:
    print("图像未找到")
