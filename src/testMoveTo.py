# test moveto
import pyautogui
import os
import time
from PIL import Image
import timeit

# 禁用自动停止
pyautogui.FAILSAFE = False

# 设置当前工作目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print('等待五秒...')
time.sleep(5)
print('等待结束...')

# 使用绝对路径
test_image_path = 'D:\\GitHub\\calabiqiu-auto\\images\\test.png'

# 屏幕快照如下
screenshot = pyautogui.screenshot()
screenshot.save(r'd:\GitHub\calabiqiu-auto\images\screenshot\screenshot.png')

try:
    location = pyautogui.locateCenterOnScreen(test_image_path, confidence=0.6)
except Exception as e:
    print("在寻找图片时发生错误:", str(e))
    location = None


if location:
    print("点击start,location:")
    print(location)
    pyautogui.moveTo(942, 984, duration=2)
    time.sleep(1)
    pyautogui.click()
else:
    print("图像未找到")
