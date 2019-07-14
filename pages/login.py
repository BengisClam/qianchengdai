# - * - coding：utf-8 -*-
# @Time       ：2019/7/14 15:12
# @Author     ：BeginsCalm
# @Email      ：13631693461@163.com
# @File       ：login.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage:
    """
    登录页面相关的属性和操作
    """

    def __init__(self, driver):
        """
        在一个流程中，同时只有一个浏览器在运行
        :param driver:
        """
        self.driver = driver

    # 封装显示等待
    def wait_click_element(self, locator):
        wait = WebDriverWait(self.driver, 30)
        return wait.until(ec.element_to_be_clickable(locator))

    def wait_presence_element(self, locator):
        wait = WebDriverWait(self.driver, 20)
        return wait.until(ec.presence_of_element_located(locator))

    def login(self, username, pwd):
        """
        使用函数封装用户名和密码
        :param driver:
        :param username:
        :param pwd:
        :return:
        """
        # 输入网址 get
        self.driver.get('http://120.78.128.25:8765')
        # 点击登录 click_login
        self.click_login()
        # 输入用户名和密码
        username_ele = self.wait_click_element((By.NAME, 'phone'))
        pwd_ele = self.wait_click_element((By.NAME, 'password'))
        username_ele.send_keys(username)
        pwd_ele.send_keys(pwd)
        # 提交  1.直接使用submit()   2.定位登录按钮
        # username.submit()
        self.driver.find_element_by_xpath("//button[contains(@class,'btn-special')]").click()

    def click_login(self):
        """
        封装登录
        :return:
        """
        return self.driver.find_element_by_css_selector('a[href="/Index/login.html"]').click()

    def get_element_error_info(self):
        return self.wait_presence_element( (By.CSS_SELECTOR, ".form-error-info"))


    def get_element_other(self):
        pass