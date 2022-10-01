"""
conftest.py pytest 配置文件
"""
import allure
import pytest
from selenium import webdriver

from conf.chrome_option import Options

# 配置运行的url
url = 'http://39.98.138.157/shopxo'

# 设置失败重跑次数
rerun = '3'

# # 运行测试用例的目录或者文件
# cases_path = './test_case/'

# 配置浏览器驱动类型
driver_type = 'chrome'


# 启动浏览器
@pytest.fixture(scope='session')
def brower():
    """
    定义全局浏览器驱动
    :return:
    """
    global driver
    global driver_type

    if driver_type == 'chrome':
        driver = webdriver.Chrome(options=Options.options)

    elif driver_type == 'firefox':
        driver = webdriver.Firefox()

    else:
        raise NameError('driver驱动类型错误')

    #用例后置 关闭浏览器
    yield driver
    driver.quit()
    print('用例结束')



"""
    装饰器@pytest.hookimpl(hookwrapper=True)等价于@pytest.mark.hookwrapper
    作用：
    1.可以获取测试用例的信息，比如用例函数的描述
    2.可以获取测试用例的执行结果，yield 返回一个result对象
"""
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport():
    """可以获取测试用例的执行结果，yield 返回一个result对象"""
    out = yield
    """
        从返回的result对象(out)获取调用结果的测试报告，返回一个report对象
        report对象属性
        包含when（setup, call, teardown的三个值）、nodeid（测试用例的名字）
        outcome(测试用例的执行结果：passed, failed)
    """
    report = out.get_result()
    if report.when == "call":
        """获取call阶段 用例执行结果为失败的情况"""
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            """添加allure报告截图 """
            with allure.step("失败截图"):
                """使用allure自带的添加附件的方式：三个参数：源文件、 文件名、 文件类型"""
                allure.attach(driver.get_screenshot_as_png(), '失败截图', allure.attachment_type.PNG)