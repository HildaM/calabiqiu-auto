import pyautogui
import pydirectinput
import time
print("test pydirectinput")
time.sleep(3)
pydirectinput.moveTo(960, 980)
pydirectinput.click()
print(pyautogui.position())   # 得到当前鼠标位置；输出：Point(x=200, y=800)

test_image_paths = "D:\\GitHub\\calabiqiu-auto\\src\\images\\test.png"
location = pyautogui.locateCenterOnScreen(test_image_paths)
print(location)
print(location.x)
print(location.y)
