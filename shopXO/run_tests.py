"""
执行整个项目的测试用例
"""
import os
import time

import pytest



def run(m):
    if m is None or m == 'run':
        print('开始执行用例：执行用例并在report目录下生成测试报告')
        """
            -s: 展示print与log信息
            -q: 安静模式运行
            ./test_case: 指定运行测试目录
            --alluredir=./test_case/allure_result: 指定allure报告数据存放目录
            --clear-alluredir: 清除allure报告数据
        """
        pytest.main(['-s', '-q', './test_case', '--alluredir=./test_case/allure_result', '--clean-alluredir'])

        """
            ./test_case/allure_result: 指定allure报告数据
            -c: 清除历史数据
            -o：指定报告目录
        
        """
        os.system('allure generate ./test_case/allure_result -c -o ./test_report')
    else:
        print('debug模式运行：不生成测试报告')
        pytest.main(['-s', './test_case/test_home_searchbox.py::TestSearch::test_case_phone'])


if __name__ == '__main__':
    run('m')
