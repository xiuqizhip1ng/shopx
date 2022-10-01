"""
基类：用于关键字封装

"""
from selenium import webdriver
from selenium.webdriver.common.by import By


class KeyWords:

    #shopXO base URl
    base_url = 'http://39.98.138.157/shopxo/'

    # 初始函数：用于driver对象
    def __init__(self, driver):
        self.driver = driver
        #运行时注释
        # self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
    #打开浏览器
    def open(self, url):
        self.driver.get(url=url)

    #定位元素
    def location(self, by, value):
        return self.driver.find_element(by, value)

    #输入元素
    def input(self, by, value, txt):
        self.location(by, value).send_keys(txt)

    #点击
    def click(self, by, value):
        self.location(by, value).click()

    #获取title
    def get_title(self):
        return self.driver.title

    #关闭页面
    def quit(self):
        self.driver.quit()

    #获取元素文本
    def get_text(self, by, value):
        text = self.location(by, value).text
        return text