"""
测试用例类
    ：用于测试首页搜索框
    : 测试数据全部大写
"""
import allure
import pytest
from selenium import webdriver

from conf.chrome_option import Options
from pages.homepages import Homepages


@allure.feature("首页模块")
class TestSearch:

    @pytest.fixture(autouse=True)
    def setup_method(self, brower):
        print('setup_method')
        # driver对象
        self.hp = Homepages(brower)

    @pytest.mark.parametrize('data',
                             [{'PRODUCT': '手机'}, {'PRODUCT': '裙子'}, {'PRODUCT': '包包'}]
                             )
    @allure.title("首页直接搜索")
    def test_case_phone(self, data):
        """在首页进行搜索"""
        #动态修改用例标题
        allure.dynamic.title(f"首页直接搜索{data['PRODUCT']}")
        #测试前
        # reality = self.hp.search_box(data['PRODUCT'])
        #测试后
        reality = self.hp.search_box(**data)
        # 断言
        expected = data['PRODUCT']
        assert expected in reality, f'实际结果{reality}与期望结果{expected}不一致'

    @allure.title("首页进行登录")
    def test_case_loginbutton(self):
        """首页进行登录"""
        reality = self.hp.loginbutton()
        # 断言
        expected = '用户登录'
        assert expected in reality, f'实际结果{reality}与期望结果{expected}不一致'
