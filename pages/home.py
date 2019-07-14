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
        self.driver.find_element_by_css_selector('a[href="/Index/login.html"]').click()
        # 输入用户名和密码
        username_ele = self.wait_click_element(self.driver, (By.NAME, 'phone'))
        pwd_ele = self.wait_click_element(self.driver, (By.NAME, 'password'))
        username_ele.send_keys(username)
        pwd_ele.send_keys(pwd)
        # 提交  1.直接使用submit()   2.定位登录按钮
        # username.submit()
        self.driver.find_element_by_xpath("//button[contains(@class,'btn-special')]").click()

