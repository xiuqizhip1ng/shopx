"""
首页页面：用于首页页面流程

"""
import allure

from bases.basekeys import KeyWords
from selenium import webdriver


class Homepages(KeyWords):
    # URL
    url = KeyWords.base_url + '/index.php'
    # 搜索框核心元素
    search_box_box = {'by': 'xpath', 'value': '//input[@id="search-input"]'}
    search_box_button = {'by': 'xpath', 'value': '//input[@id="ai-topsearch"]'}

    # 登录按钮核心元素
    login_button = {'by': 'xpath', 'value': '/html/body/div[6]/div/div[1]/div[2]/a[1]'}

    @allure.step("首页搜索框搜索流程")
    def search_box(self, PRODUCT):
        with allure.step("打开首页"):
            self.open(url=self.url)
        with allure.step(f"搜索框输入{PRODUCT}"):
            self.input(txt=PRODUCT, **self.search_box_box)
        with allure.step("点击搜索按钮"):
            self.click(**self.search_box_button)
        with allure.step("返回搜索页title"):
            reality = self.get_title()
        return reality

    @allure.step("首页点击登录按钮登录流程")
    def loginbutton(self):
        with allure.step("打开登录页面"):
            self.open(url=self.url)
        with allure.step("点击登录按钮"):
            self.click(**self.login_button)
        with allure.step("获取登录后页面title"):
            reality = self.get_title()
        return reality
