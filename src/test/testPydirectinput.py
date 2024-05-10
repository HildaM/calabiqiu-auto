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

def get_position(image_path):
    try:
        location = pyautogui.locateCenterOnScreen(image_path, minSearchTime=5, confidence=0.9)
        if location:
            return location
    except pyautogui.ImageNotFoundException:
        pass
    return False

print("考虑升级情况")
upgrade_pic = get_position(test_image_paths)
if upgrade_pic:
    print("升级了")
    pydirectinput.moveTo(upgrade_pic.x, upgrade_pic.y)
    pydirectinput.click()

