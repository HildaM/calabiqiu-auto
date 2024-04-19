# #测试
# import pyautogui
# import pydirectinput
# import time
# import pyautogui
# import os
# # 禁用自动停止
# pyautogui.FAILSAFE = False

# # 设置当前工作目录
# os.chdir(os.path.dirname(os.path.abspath(__file__)))

# # 启动脚本延时
# print('脚本启动中...')
# time.sleep(3)
# print('启动完成')

# # 图像导入
# images_paths = [
#     'D:\\GitHub\\calabiqiu-auto\\images\\test2.png'
# ]
# test_image_paths = 'D:\\GitHub\\calabiqiu-auto\\images\\test.png'

# # 检查图像


# def check_one_image(image_path):
#     location = pyautogui.locateCenterOnScreen(image_path, confidence=0.6)
#     if location != None:
#         return True
#     else:
#         return False


# def loop(image_path):
#     while True:
#         found_pic = check_one_image(image_path)
#         if found_pic:
#             print("找到了")
#             break
#         print("没找到,等待五秒重新寻找...")
#         time.sleep(5)

# # 检查图像列表


# def check_images(image_list):
#     for image_path in image_list:
#         location = pyautogui.locateCenterOnScreen(image_path, confidence=0.7)
#         if location:
#             return True
#         else:
#             return False


# def loopList(image_list):
#     while True:
#         found_pic = check_images(image_list)
#         if found_pic:
#             print(f"找到了")
#             break
#         print("没找到,等待五秒重新寻找...")
#         time.sleep(5)


# # 循环启动脚本

# # 自动点击开始按钮:开
# time.sleep(3)
# loopList(images_paths)
# pydirectinput.moveTo(960, 980)
# pydirectinput.click()

# # 自动点击进入链接：进
# time.sleep(3)
# loop(test_image_paths)
# pydirectinput.moveTo(970, 920)
# pydirectinput.click()
