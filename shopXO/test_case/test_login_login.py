"""
登录页面测试
    1.测试数据全部大写
"""
import allure
import pytest

from pages.loginpages import Loginpage


@allure.feature('登录模块')
class TestLogin:

    @pytest.fixture(autouse=True)
    def setup_method(self, brower):
        self.lp = Loginpage(brower)

    @pytest.mark.parametrize('data',
                             [{'USERNAME': 'xiuqizhiping1', 'PASSWORD': '123456', 'TYPE': "正确账号名密码"}]
                             )
    @allure.title('输入账号密码登录')
    def test_login(self, data):
        reality = self.lp.login(data['USERNAME'], data['PASSWORD'])
        # 动态修改测试用例标题
        allure.dynamic.title(data['TYPE'])
        # 断言
        expect = f"{data['USERNAME']}，欢迎来到"
        assert reality == expect, f"实际结果:{reality}与预期结果不一致:{expect}"
