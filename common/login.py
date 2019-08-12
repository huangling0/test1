#! /usr/bin/env python
# -*- coding:utf-8
# author:mlh
# datetime:2019/5/29 下午2:06

from selenium.webdriver.common.action_chains import ActionChains
from log import logTest
import time


def login(self):
    '''帐号密码登录'''
    self.driver.find_elements_by_name("handle")[0].clear()
    self.driver.find_elements_by_name("handle")[0].send_keys("182xxx1209")
    # time.sleep(2)
    self.driver.find_elements_by_name("handle")[1].clear()
    self.driver.find_elements_by_name("handle")[1].send_keys("93...ing")
    # time.sleep(2)
    self.driver.find_element_by_class_name("sign-button").click()
    time.sleep(30)

    try:
        self.driver.switch_to.default_content()
        '''点击取消登录成功的提示'''
        self.driver.find_element_by_xpath("//*[@id='dialog']/div/div/div[1]/a").click()

    except Exception as e:
        logTest.log(e)
        logTest.log("没有登录成功的提示")

    try:
        self.driver.switch_to.default_content()
        '''点击取消引导'''
        self.driver.find_element_by_xpath("/html/body/div[5]/span[2]/button").click()
    except Exception as e:
        logTest.log(e)
        logTest.log("没有登录引导")


def login_out(self):
    '''退出登录'''
    locator = self.driver.find_element_by_class_name("name-a")
    ActionChains(self.driver).move_to_element(locator).perform()
    self.driver.find_element_by_class_name("loginout").click()
    logTest.log("退出登陆")
