# - * - coding：utf-8 -*-
# @Time       ：2019/7/10 21:28
# @Author     ：BeginsCalm
# @Email      ：13631693461@163.com
# @File       ：test_login.py
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.login import login, wait_presence_element


class TestLogin(unittest.TestCase):
    """
    引入unittest测试框架
    """

    def setUp(self):
        """
        初始化浏览器
        :return:
        """
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)

    def tearDown(self):
        """
        关闭浏览器
        :return:
        """
        self.driver.quit()

    def test_success(self):
        """
        正向用例
        :return:
        """
        login(self.driver, '18684720553', 'python')
        # 断言
        user = wait_presence_element(self.driver, (By.CSS_SELECTOR, 'a[href="/Member/index.html"]'))
        self.assertTrue( '我的帐户[python10]' in user.text )

    def test_error(self):
        """
        反向用例
        :return:
        """
        login(self.driver, '', '')
        # 定位实际结果
        actual_ele = wait_presence_element(self.driver, (By.CSS_SELECTOR, ".form-error-info"))
        self.assertTrue(actual_ele.text == '请输入手机号')


if __name__ == '__main__':
    unittest.main()


# 测使用里面 test_success， 不要写太多的逻辑：
# 1.包含操作的函数，获取实际结果
# 2.预期结果
# 3.断言

# 函数封装的意义：封装重用的程序，



# 可以改进的地方
# 1.测试数据要抽离
# 2.定位表达式需要抽离
#