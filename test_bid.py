# - * - coding：utf-8 -*-
# @Time       ：2019/7/14 15:27
# @Author     ：BeginsCalm
# @Email      ：13631693461@163.com
# @File       ：test_bid.py

# 登录

import unittest
from selenium import webdriver

from pages import login


class TestBid(unittest.TestCase):

    def serUp(self):
        """
        初始化浏览器
        加上隐式等待
        登录
        是否有可投的标，判断是否有足够的余额，如果没有余额，就充值
        前置条件满足即可
        :return:
        """
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        login()

    def test_bid(self):
        """

        :return:
        """
        pass