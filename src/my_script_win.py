# #废弃2号方案：游戏外可用，游戏内不可用
# import ctypes
# from ctypes import wintypes
# import time

# user32 = ctypes.WinDLL('user32', use_last_error=True)

# INPUT_MOUSE = 0
# MOUSEEVENTF_MOVE = 0x0001
# MOUSEEVENTF_ABSOLUTE = 0x8000
# MOUSEEVENTF_LEFTDOWN = 0x0002
# MOUSEEVENTF_LEFTUP = 0x0004


# class MOUSEINPUT(ctypes.Structure):
#     _fields_ = (("dx", wintypes.LONG),
#                 ("dy", wintypes.LONG),
#                 ("mouseData", wintypes.DWORD),
#                 ("dwFlags", wintypes.DWORD),
#                 ("time", wintypes.DWORD),
#                 ("dwExtraInfo", ctypes.c_ulonglong))  # 使用 ctypes.c_ulonglong 替代原来的 ULONG_PTR


# class INPUT(ctypes.Structure):
#     class _INPUT(ctypes.Union):
#         _fields_ = (("mi", MOUSEINPUT),)
#     _anonymous_ = ("_input",)
#     _fields_ = (("type", wintypes.DWORD),
#                 ("_input", _INPUT))


# def move_and_click(x, y):
#     # 直接使用屏幕的实际分辨率
#     screen_width = 1920
#     screen_height = 1080
#     x_scaled = int(x * 65535 / screen_width)
#     y_scaled = int(y * 65535 / screen_height)

#     # 打印调试信息
#     print("x_scaled:", x_scaled, "y_scaled:", y_scaled)

#     # 移动到指定位置并点击
#     mi = MOUSEINPUT(dx=x_scaled, dy=y_scaled, mouseData=0,
#                     dwFlags=MOUSEEVENTF_MOVE | MOUSEEVENTF_ABSOLUTE | MOUSEEVENTF_LEFTDOWN | MOUSEEVENTF_LEFTUP,
#                     time=0, dwExtraInfo=0)
#     inp = INPUT(type=INPUT_MOUSE, mi=mi)
#     ctypes.windll.user32.SendInput(1, ctypes.byref(inp), ctypes.sizeof(inp))


# # 示例：在屏幕坐标开始处点击
# time.sleep(3)
# move_and_click(900, 983)
# print("完成点击")
