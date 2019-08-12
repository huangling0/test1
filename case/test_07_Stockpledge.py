#! /usr/bin/env python
# -*- coding:utf-8
# author:mlh
# datetime:2019/5/28 下午4:15

import time
import unittest
from init import InitTest
from selenium.webdriver.common.action_chains import ActionChains
from common import login, securities
import random
from log import logTest
from selenium.webdriver.common.by import By


class Stockpledge(InitTest):
    '''测试大黄押'''

    def test_001_Stockpledge(self):
        '''页面跳转到大黄押'''
        self.driver.get("http://ibdata.cn/#!/stockpledge")
        login.login(self)
        self.driver.find_element_by_link_text("大黄押").click()
        handles = self.driver.window_handles
        self.driver.switch_to.window(self.driver.window_handles[len(handles) - 1])
        logTest.log("页面跳转到大黄押")

    def test_002_Stockpledge(self):
        '''输入标的证券搜索'''
        # lis = ["00", "600", "300", "002", "200", "900"]
        # num = random.randint(0, len(lis) - 1)
        # ep_input = self.driver.find_elements_by_class_name("ep-input")
        # ep_input[0].send_keys(lis[num])
        # time.sleep(3)
        # company_menu = self.driver.find_element(By.CLASS_NAME, "company-menu")
        # lis_company = company_menu.find_elements(By.XPATH, "li")
        # lis_num = random.randint(0, len(lis_company)-1)
        # lis_company[lis_num].click()
        # time.sleep(3)
        company_name = securities.Asecurities()
        ep_input = self.driver.find_elements_by_class_name("ep-input")
        ep_input[0].send_keys(company_name)
        time.sleep(5)
        btn_search = self.driver.find_element_by_class_name("btn-search")
        btn_search.click()
        time.sleep(30)
        logTest.log("输入标的证券并搜索")

    def test_003_Stockpledge(self):
        '''查看质押信息'''
        try:
            dhy = self.driver.find_elements_by_class_name("dhy-small-mor")
            dhy[0].click()
            ul = self.driver.find_elements_by_class_name("lanmu")[0]
            ul.find_elements_by_xpath("li")[1].click()
            logTest.log("选择质押期内的历史质押信息")
            logTest.log("对表格的操作")
            self.driver.find_elements_by_class_name("dhy-btn-open")[0].click()
            logTest.log("对股东进行排序")

            self.driver.find_elements_by_class_name("icofont-caret-up")[0].click()
            logTest.log("按照开始日期排序")

            '''展开和收起'''
            try:
                self.driver.find_elements_by_class_name("dhy-Display-all")[0].click()
                self.driver.find_elements_by_class_name("dhy-Display-all")[1].click()
                # self.driver.find_element_by_class_name("info-Underline").click()
                logTest.log("展开和收起")
            except Exception as e:
                logTest.log(e)
        except Exception as e:
            print(e)
            logTest.log("没有质押信息")

    def test_004_Stockpledge(self):
        '''获取融入方，并且输入进行搜索'''
        try:
            t = self.driver.find_elements_by_class_name("dhy-title-box1")
            text = t[0].text
            self.driver.find_elements_by_class_name("ep-input")[1].send_keys(text)
            self.driver.find_element_by_class_name("btn-search").click()
            time.sleep(10)
            logTest.log("获取融入方，并且输入进行搜索")
        except Exception as e:
            logTest.log(e)

    def test_005_Stockpledge(self):
        '''跳转到质权人页面，输入质权人，进行搜索'''

        self.driver.find_element_by_link_text("质权人").click()
        self.driver.find_element_by_class_name("ep-input").send_keys("中国")
        time.sleep(3)
        ul = self.driver.find_element(By.CLASS_NAME, "company-menu")
        lis = ul.find_elements(By.XPATH, "li")
        num = random.randint(0, len(lis)-1)
        lis[num].click()
        self.driver.find_element_by_class_name("btn-search").click()
        time.sleep(10)
        logTest.log("输入质权人,并搜索")
        '''关系图和表格的切换'''
        self.driver.find_element_by_link_text("表格").click()
        time.sleep(5)
        logTest.log("关系图和表格的切换")
        div_table = self.driver.find_element(By.CLASS_NAME, "financ-tables")
        ul_table = div_table.find_element(By.XPATH, "ul")
        li_table = ul_table.find_elements(By.XPATH, "li")
        li_table[0].click()
        time.sleep(5)
        logTest.log("关系图和表格的切换")
        '''移动滚动条'''
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        logTest.log("移动滚动条")
        time.sleep(2)
        try:
            locator = self.driver.find_elements_by_class_name("node")[2]
            '''对ActionChains实例化'''
            ActionChains(self.driver).move_to_element(locator).perform()
            time.sleep(30)
            logTest.log("鼠标放到对应的目标,查看来源")
        except Exception as e:
            logTest.log(e)

    def test_006_Stockpledge(self):
        '''融入方'''
        self.driver.find_element_by_link_text("融入方").click()
        logTest.log("跳转到融入方")
        self.driver.find_element_by_class_name("ep-input").send_keys("有限公司")
        time.sleep(3)
        try:
            ul = self.driver.find_element(By.CLASS_NAME, "company-menu")
            lis = ul.find_elements(By.XPATH, "li")
            num = random.randint(0, len(lis) - 1)
            lis[num].click()
            logTest.log("输入融入方")
        except Exception as e:
            logTest.log(e)
        self.driver.find_element_by_class_name("btn-search").click()
        time.sleep(2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
