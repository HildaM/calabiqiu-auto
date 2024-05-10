import pydirectinput
import time
import pyautogui
import os
import logging
import logging.config
import json
import sys

# 获取资源的绝对路径，用于PyInstaller打包后资源的访问
def resource_path(relative_path):
    # 是否Bundle Resource
    if getattr(sys, ' frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# 日志文件
def setup_logging(default_path=resource_path('logging_configs\\config.json')):
    """Setup logging configuration"""
    if os.path.exists(default_path):
        with open(default_path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=logging.DEBUG)
        print("Failed to load configuration file. Using default configs")


# 禁用自动停止
pyautogui.FAILSAFE = False

# 设置当前工作目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 图像导入，使用resource_path函数确保路径正确
start_image_paths = [
    resource_path('images\\start1.png'),
    resource_path('images\\start2.png')
]
enter_image_paths = resource_path('images\\enter.png')
# chooseRole_image_paths = resource_path('images\\chooseRole.png')
ao_image_paths = resource_path('images\\ao.png')
lock_image_paths = [
    resource_path('images\\lock1.png'),
    resource_path('images\\lock2.png')
]
image_paths = [
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
next_images_paths = [
    resource_path('images\\next.png'),
    resource_path('images\\back1.png'),
    resource_path('images\\back2.png'),
    resource_path('images\\note.png'),
    resource_path('images\\close1.png'),
    resource_path('images\\close2.png'),
    resource_path('images\\close3.png'),
    resource_path('images\\close4.png')
    # resource_path('images\\box.png')
]


# 获取x和y坐标
def check_one_image_location(image_path):
    try:
        location = pyautogui.locateCenterOnScreen(image_path, minSearchTime=5, confidence=0.8)
        if location:
            return location
    except pyautogui.ImageNotFoundException:
        pass
    return False


# 检查图像
def check_one_image(image_path, confidence):
    try:
        location = pyautogui.locateCenterOnScreen(image_path, minSearchTime=5, confidence=confidence)
        if location:
            return True
    except pyautogui.ImageNotFoundException:
        pass
    return False


def loop(image_path, loop_times, confidence):
    loopCount = 0
    while True:
        loopCount += 1
        found_pic = check_one_image(image_path, confidence)
        if found_pic:
            print("找到了")
            break
        if loopCount >= loop_times:
            print(f"循环超过{loop_times}次，跳出循环")
            break
        print(loopCount, ":没找到,等待五秒重新寻找...")
        time.sleep(5)

# 找到开始点开始，找不到奥黛丽就一直点击进入链接位置
def loopAndClick(image_path, images_paths, loop_times, x, y):
    loopCount = 0
    while True:
        loopCount += 1
        # 查找开始
        found_pic2 = check_images(images_paths, 0.8)
        if found_pic2:
            print("等待超过10min，需要重新点击开始")
            pydirectinput.moveTo(960, 980)
            pydirectinput.click()
        # 查找进入链接
        found_pic = check_one_image(image_path, 0.8)
        if found_pic:
            print("找到了")
            break
        if loopCount >= loop_times:
            print(f"循环超过{loop_times}次，跳出循环")
            break
        print(loopCount, ":没找到,等待五秒重新寻找...尝试点击进入链接按钮")
        pydirectinput.moveTo(x, y)
        pydirectinput.click()
        time.sleep(5)


# 检查图像列表


def check_images(image_list, confidence):
    for image_path in image_list:
        try:
            location = pyautogui.locateCenterOnScreen(image_path, minSearchTime=5, confidence=confidence)
            if location:
                return True
        except pyautogui.ImageNotFoundException:
            pass
        return False


def loopList(image_list, loop_times, confidence):
    loopListCount = 0
    while True:
        loopListCount += 1
        found_pic = check_images(image_list, confidence)
        if found_pic:
            print("找到了")
            break
        if loopListCount >= loop_times:
            print(f"循环超过{loop_times}次，跳出循环")
            break
        print(loopListCount, ":没找到,等待五秒重新寻找...")
        time.sleep(5)

def main():
    setup_logging()
    logger = logging.getLogger("root")
    # 运行主循环
    # 启动脚本延时
    logger.debug('脚本启动中...')
    time.sleep(3)
    logger.debug('启动完成')
    count = 0
    while True:  # 无限循环
        # 自动点击开始按钮：开1，开2
        count += 1
        logger.debug("   ____           _           _       _           _         ")
        logger.debug("  / ___|   __ _  | |   __ _  | |__   (_)   __ _  (_)  _   _ ")
        logger.debug(" | |      / _` | | |  / _` | | '_ \\  | |  / _` | | | | | | |")
        logger.debug(" | |___  | (_| | | | | (_| | | |_) | | | | (_| | | | | |_| |")
        logger.debug("  \\____|  \\__,_| |_|  \\__,_| |_.__/  |_|  \\__, | |_|  \\__,_|")
        logger.debug("                                             |_|            ")
        logger.debug("第%s次对战", count)
        logger.debug("###################################")
        logger.debug("自动点击开始按钮")
        time.sleep(3)
        loopList(start_image_paths, 50, 0.8)
        pydirectinput.moveTo(960, 980)
        pydirectinput.click()
        logger.debug("自动点击开始按钮完毕")
        logger.debug("###################################")

        # 判断是否进入，进入链接界面

        # 自动点击进入链接：进，需要考虑玩家未准备情况
        logger.debug("自动点击进入链接")
        time.sleep(3)
        loop(enter_image_paths, 120, 0.8)
        pydirectinput.moveTo(970, 920)
        pydirectinput.click()
        time.sleep(0.5)
        pydirectinput.click()
        time.sleep(0.5)
        pydirectinput.click()
        logger.debug("自动点击进入链接完毕")
        logger.debug("###################################")

        # 自动识别选择角色界面，识别玩家未准备情况
        logger.debug("自动识别选择角色界面")
        time.sleep(3)
        loopAndClick(ao_image_paths, start_image_paths, 120, 970, 920)
        logger.debug("自动识别选择角色界面")
        logger.debug("###################################")

        # 自动选择奥黛丽：头像
        logger.debug("自动选择奥黛丽")
        # time.sleep(3)
        loop(ao_image_paths, 50, 0.8)
        # 每个人的奥黛丽顺序不同，这个坐标只能手动获取
        # 存在识别不到图像的bug，坐标回到手动配置
        try:
            location = check_one_image_location(ao_image_paths)
            if location:
                pydirectinput.moveTo(location.x, location.y)
                logging.debug("奥黛丽坐标为x=%s，y=%s", location.x, location.y)
            else:
                pydirectinput.moveTo(575, 996)
        except pyautogui.ImageNotFoundException:
            pydirectinput.moveTo(575, 996)

        # 东雪莲office，x=789，y=992
        # pydirectinput.moveTo(789, 992)
        # vx 2 号的坐标,第二行第一个(575, 996)
        # pydirectinput.moveTo(575, 996)
        pydirectinput.click()
        time.sleep(0.5)
        pydirectinput.click()
        time.sleep(0.5)
        pydirectinput.click()
        logger.debug("自动选择奥黛丽完毕")
        logger.debug("###################################")

        # 自动选中锁定
        logger.debug("自动选中锁定")
        time.sleep(3)
        loopList(lock_image_paths, 50, 0.8)
        pydirectinput.moveTo(918, 779)
        logging.debug(pyautogui.position())
        pydirectinput.click()
        time.sleep(0.5)
        pydirectinput.click()
        time.sleep(0.5)
        pydirectinput.click()
        logger.debug("自动选中锁定完毕")
        logger.debug("###################################")

        # 对局没有哪么快结束，先睡3min=180s
        logger.debug("对局没有哪么快结束，先睡180s")
        time.sleep(60)
        logger.debug("已经睡了60s")
        time.sleep(60)
        logger.debug("已经睡了120s")
        time.sleep(60)
        logger.debug("已经睡了180s")
        logger.debug("结束睡眠")
        logger.debug("###################################")

        # 图片路径

        # 图像识别上方比分，当到达45时候，移动人物
        # 循环搜索
        logger.debug("图像识别上方比分45-50")
        loopList(image_paths, 50, 0.85)
        logger.debug("图像识别上方比分完毕")
        logger.debug("###################################")
        # 保持运动等待游戏结束
        logger.debug("保持运动等待游戏结束")
        pydirectinput.press('w')
        pydirectinput.moveTo(800, 970)
        pydirectinput.click()   # 升级返回键
        time.sleep(10)
        pydirectinput.press('d')
        pydirectinput.moveTo(800, 970)
        pydirectinput.click()
        time.sleep(10)
        pydirectinput.press('w')
        pydirectinput.moveTo(800, 970)
        pydirectinput.click()
        time.sleep(10)
        pydirectinput.press('d')
        pydirectinput.moveTo(800, 970)
        pydirectinput.click()
        time.sleep(10)
        pydirectinput.press('w')
        pydirectinput.moveTo(800, 970)
        pydirectinput.click()
        logger.debug("###################################")

        # 图像识别：下一步或者升级或者挂机警告提示
        logger.debug("图像识别：下一步或者升级检测")
        time.sleep(3)
        loopList(next_images_paths, 50, 0.6)
        logger.debug("图像识别完毕")
        logger.debug("###################################")

        # 点击升级的返回按钮,三十级以前，三十级以后不一样
        logger.debug("###################################")
        logger.debug("升级")
        time.sleep(3)
        pydirectinput.moveTo(800, 970)
        pydirectinput.click()
        logger.debug("低于30级，升级位于左边")
        time.sleep(3)
        pydirectinput.moveTo(960, 970)
        pydirectinput.click()
        logger.debug("高于30级，升级位于正中间")
        logger.debug("升级, 完毕")
        logger.debug("###################################")
        # 挂机检测
        logger.debug("挂机检测")
        time.sleep(3)
        pydirectinput.moveTo(945, 678)
        logging.debug(pyautogui.position())
        pydirectinput.click()
        logger.debug("挂机检测, 完毕")
        logger.debug("###################################")

        # 点击下一步，下一步，退出
        logger.debug("###################################")
        logger.debug("下一步")
        time.sleep(3)
        pydirectinput.moveTo(1588, 1000)
        pydirectinput.click()
        time.sleep(3)
        pydirectinput.moveTo(1588, 1000)
        pydirectinput.click()
        time.sleep(3)
        pydirectinput.moveTo(1588, 1000)
        pydirectinput.click()
        time.sleep(3)
        pydirectinput.moveTo(1588, 1000)
        pydirectinput.click()
        time.sleep(3)
        pydirectinput.moveTo(1588, 1000)
        pydirectinput.click()
        logger.debug("退出完毕")
        logger.debug("###################################")
        logger.debug("==================================================")


if __name__ == "__main__":
    main()
