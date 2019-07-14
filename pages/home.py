# - * - coding：utf-8 -*-
# @Time       ：2019/7/14 15:57
# @Author     ：BeginsCalm
# @Email      ：13631693461@163.com
# @File       ：home.py


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class HomePage:
    """
    首页
    """

    def __init__(self, driver):
        """
        在一个流程中，同时只有一个浏览器在运行
        :param driver:
        """
        self.driver = driver

    # 封装显示等待
    def wait_click_element(self, driver, locator):
        wait = WebDriverWait(self.driver, 30)
        return wait.until(ec.element_to_be_clickable(locator))

    def wait_presence_element(self, driver, locator):
        wait = WebDriverWait(self.driver, 20)
        return wait.until(ec.presence_of_element_located(locator))

    def get_element__user(self):
        """

        :return:
        """
        return self.wait_presence_element(self.driver, (By.CSS_SELECTOR, 'a[href="/Member/index.html"]'))
