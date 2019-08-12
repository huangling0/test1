# !/usr/bin/env python
# -*-coding:utf-8
# author:mlh
# datetime:2019/6/3 下午2:49

import unittest
import time
from init import InitTest
from common import login
from selenium.webdriver.common.action_chains import ActionChains
import random
from log import logTest
from selenium.webdriver.common.by import By


def event(self):
    num8 = random.randint(6, 8)
    event = self.driver.find_elements_by_class_name("el-radio-inner")
    event[num8].click()
    logTest.log("选择事件")
    if num8 == 7:

        div = self.driver.find_element_by_css_selector(".My-Event-cont")
        ul = div.find_element(By.XPATH, "ul")
        lis3 = ul.find_elements_by_xpath("li")
        num9 = random.randint(0, len(lis3) - 1)
        lis3[num9].click()
        logTest.log("选择推荐事件")
    elif num8 == 8:
        self.driver.find_element_by_class_name("keyword-title").click()
        ul = self.driver.find_element_by_class_name("dropdown-menu")
        lis4 = ul.find_elements_by_xpath("li")
        num10 = random.randint(0, len(lis4) - 1)
        lis4[num10].click()
        self.driver.find_element_by_class_name("input-search-a").send_keys("公告")
        logTest.log("选择自定义事件")
    else:
        pass
    time.sleep(3)
    #
    self.driver.find_elements_by_class_name("btn-add")[1].click()
    time.sleep(3)
    logTest.log("点击保存")


def event1(self):
    num8 = random.randint(7, 8)
    event = self.driver.find_elements_by_class_name("el-radio-inner")
    event[num8].click()
    logTest.log("选择事件")
    if num8 == 7:

        div1 = self.driver.find_element_by_css_selector(".My-Event-cont")
        ul = div1.find_element_by_xpath("ul")
        lis3 = ul.find_elements_by_xpath("li")
        num9 = random.randint(0, len(lis3) - 1)
        lis3[num9].click()
        logTest.log("选择推荐事件")
    else:
        keyword = self.driver.find_element_by_class_name("keyword-title")
        keyword.click()
        ul = self.driver.find_element_by_class_name("dropdown-menu")
        lis4 = ul.find_elements_by_xpath("li")
        num10 = random.randint(0, len(lis4) - 1)
        lis4[num10].click()
        inp = self.driver.find_element_by_class_name("input-search-a")
        inp.send_keys("公告")
        logTest.log("选择自定义事件")
    #
    self.driver.find_elements_by_class_name("btn-add")[1].click()
    time.sleep(3)
    logTest.log("点击保存")


class Subscript(InitTest):

    '''测试我的订阅'''

    def test_001_Subscript(self):
        self.driver.get("http://ibdata.cn/#!/login")
        login.login(self)

        # self.driver.get("http://ibdata.cn/#!/my/mysubscribe")
        self.driver.find_element_by_link_text("我的订阅").click()
        time.sleep(5)
        # old_handle = self.driver.current_window_handle
        handles = self.driver.window_handles
        self.driver.switch_to.window(self.driver.window_handles[len(handles)-1])
        logTest.log("跳转到我的订阅的页面")

    def test_002_Subscript(self):
        '''查看订阅的每一项，修改已有的订阅'''
        #
        self.driver.find_element_by_class_name("Explain").click()
        logTest.log("查看订阅说明")
        time.sleep(10)
        div = self.driver.find_element_by_class_name("ubscribe-menu")
        ul = div.find_element_by_xpath("ul")
        lis = ul.find_elements_by_xpath("li")
        for i in range(len(lis)):
            #
            ul.find_elements_by_xpath("li")[i].click()
            time.sleep(30)
            logTest.log("点击我的订阅的每一项")
            # 下拉至当前元素所在位置处
            button = ul.find_elements_by_xpath("li")[i]
            self.driver.execute_script("arguments[0].scrollIntoView();", button)
            logTest.log("下拉至当前元素所在位置处")
        #
        action_chains = ActionChains(self.driver)
        logTest.log("鼠标实例化")
        # 修改已有的订阅
        num = random.randint(0, len(lis) - 1)
        print(num)
        locator = ul.find_elements_by_xpath("li")[num]
        # 定位元素
        self.driver.execute_script("arguments[0].scrollIntoView();", locator)
        time.sleep(2)
        #
        action_chains.move_to_element(locator).perform()
        logTest.log("鼠标移到定位的元素上")
        time.sleep(2)
        #
        edit = self.driver.find_elements_by_class_name("btn-see")
        edit[num].click()
        logTest.log("点击可编辑标签")
        time.sleep(2)
        #
        btn_add = self.driver.find_elements_by_class_name("btn-add")
        btn_add[1].click()
        logTest.log("点击保存")
        time.sleep(10)

    def test_003_Subscript(self):
        ''' 删除已有的订阅'''
        div = self.driver.find_element_by_class_name("ubscribe-menu")
        ul = div.find_element_by_xpath("ul")
        lis = ul.find_elements_by_xpath("li")
        num2 = random.randint(0, len(lis) - 1)
        print(num2)
        locator2 = ul.find_elements_by_xpath("li")[num2]
        self.driver.execute_script("arguments[0].scrollIntoView();", locator2)
        time.sleep(2)
        ActionChains(self.driver).move_to_element(locator2).perform()
        self.driver.find_elements_by_class_name("btn-delete")[num2].click()
        time.sleep(15)
        self.driver.switch_to.default_content()
        dele = self.driver.find_elements_by_class_name("btn-del")
        num3 = random.randint(0, len(dele) - 1)
        dele[num3].click()
        time.sleep(30)
        logTest.log("删除已有的而订阅")

    def test_004_Subscript(self):
        '''添加新的订阅'''
        self.driver.find_element_by_class_name("btn-add").click()
        time.sleep(5)
        logTest.log("点击添加新的订阅")
        #
        tag_inp = self.driver.find_element_by_class_name("tags-input")
        tag_inp.send_keys("uitest")
        logTest.log("输入订阅名称")
        time.sleep(2)
        #
        num4 = random.randint(0, 2)
        plat_type = self.driver.find_elements_by_class_name("el-radio-inner")
        plat_type[num4].click()
        time.sleep(3)
        logTest.log("选择板块类型")
        if num4 == 2:
            num4_1 = random.randint(3, 4)
            company_type1 = self.driver.find_elements_by_class_name("el-radio-inner")
            company_type1[num4_1].click()
            if num4_1 == 3:
                bond = self.driver.find_element_by_class_name("input-search-a")
                bond.send_keys("公告")
                # 点击保存
                self.driver.find_elements_by_class_name("btn-add")[1].click()
                time.sleep(3)
            else:
                self.driver.find_element_by_class_name("My-choice-list").click()
                lis = self.driver.find_elements_by_class_name("text")
                num4_2 = random.randint(0, len(lis) - 1)
                lis[num4_2].click()
                logTest.log("选择了证券组合")
                event2 = self.driver.find_elements(By.CLASS_NAME, "el-radio-input")
                lis4_2 = [6, 8]
                for i in lis4_2:
                    event2[i].click()
                    if i == 8:
                        bond2 = self.driver.find_element_by_class_name("input-search-a")
                        bond2.send_keys("公告")
                # 点击保存
                self.driver.find_elements_by_class_name("btn-add")[1].click()
                time.sleep(3)
        else:
            num5 = random.randint(3, 5)
            company_type = self.driver.find_elements_by_class_name("el-radio-inner")
            company_type[num5].click()
            logTest.log("选择公司范围")
            time.sleep(3)
            if num5 == 4:
                self.driver.find_element_by_class_name("My-choice-list").click()
                lis = self.driver.find_elements_by_class_name("text")
                num6 = random.randint(0, len(lis) - 1)
                lis[num6].click()
                logTest.log("选择了证券组合")
                event(self)
            elif num5 == 5:
                div = self.driver.find_elements_by_class_name("My-Event-cont")[0]
                ul = div.find_element_by_xpath("ul")
                lis2 = ul.find_elements_by_xpath("li")
                num7 = random.randint(0, len(lis2) - 1)
                lis2[num7].click()
                logTest.log("选择了行业")
                event(self)
            else:
                logTest.log("选择全部")
                event1(self)
                time.sleep(2)


if __name__ == "__main__":
    unittest.main(verbosity=2)

