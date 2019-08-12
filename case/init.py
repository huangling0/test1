#! /usr/bin/env python
# -*- coding:utf-8
# author:mlh
# datetime:2019/5/16 上午9:53

from selenium import webdriver
import unittest
from log import logTest
import warnings


class InitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        warnings.simplefilter('ignore', ResourceWarning)
        logTest.log("测试开始，打开浏览器")
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(60)
        # cls.driver.get("http://ibdata.cn/#!/login")
        # cls.driver.get("http://ibdata.cn/#!/search")
        cls.driver.get("http://ibdata.cn/#!/")
        logTest.log("打开登录页面")

    @classmethod
    def tearDownClass(cls) -> None:

        cls.driver.quit()
        logTest.log("测试结束，关闭浏览器并退出")
        logTest.log("---------------------------------")
        logTest.log("---------------------------------")




