# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import re

import os

import requests


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。






if __name__ == '__main__':
    url = "https://edusys.xmdas-link.com/auth/login/teacher"
    data = {
        "user": "chenls",
        "pass": "j7JH21YaQU1E6scNQt47xg==",
        "bizState": "teacher_pc",
        "randstr": "@obT",
        "ticket": "tr03QAsYLXdk7prLI9qry--P1ViiZdBsgzMMUPyOoI9rzYzylTEa9zTfKPcvfsVzGGQPQw-2g5bAzAn2grJHODF8KcU3Oq_v75Gq971Vwfrus-zcggGDTG5P_-PCSEBeLIe1KaOw1KyA29dWnmHUYKcm95HTfKvVjowSGZ4jrM6LwqNAH2qOl3ptiwxn9WKDbJW-Yosc4HEtI-s*"
    }
    print(type(data))
    res = requests.post(url=url, data=data)
    print(res.json())
