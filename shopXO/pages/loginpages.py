"""
登录页面类：
测试登录流程

"""
import allure

from bases.basekeys import KeyWords


class Loginpage(KeyWords):
    # 登录页URL
    url = KeyWords.base_url + '/index.php?s=/index/user/logininfo.html'
    # 登录核心元素

    login_account = {'by': 'xpath', 'value': '/html/body/div[4]/div/div[2]/div[2]/form/div[1]/input'}
    login_passwd = {'by': 'xpath', 'value': '/html/body/div[4]/div/div[2]/div[2]/form/div[2]/input'}
    login_button = {'by': 'xpath', 'value': '/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button'}
    show_user = {'by': 'xpath', 'value': '/html/body/div[2]/div/ul[1]/div/div/em[2]'}

    @allure.step('登录页面登录流程')
    def login(self, username, password):
        with allure.step('打开登录页面'):
            self.open(url=self.url)
        with allure.step('输入账号'):
            self.input(txt=username, **self.login_account)
        with allure.step('输入密码'):
            self.input(txt=password, **self.login_passwd)
        with allure.step('点击登录按钮'):
            self.click(**self.login_button)
        with allure.step('获取登录后页面title'):
            reality = self.get_text(**self.show_user)
        return reality
