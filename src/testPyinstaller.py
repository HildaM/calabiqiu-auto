# 播放音乐
# coding:utf-8
import sys
import os


# 生成资源文件目录访问路径
def resource_path(relative_path):
    # 是否Bundle Resource
    if getattr(sys, ' frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def get_resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


# 访问Sing文件夹下Happy.MP3的内容
filepath = resource_path(os.path.join("images", "test.png"))
print(filepath)


