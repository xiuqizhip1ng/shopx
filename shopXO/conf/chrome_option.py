"""
chrome 的 options参数

"""
from selenium import webdriver


class Options:
    options = webdriver.ChromeOptions()
    # 最大化运行（全屏窗口）,不设置，取元素会报错
    options.add_argument('--start-maximized')