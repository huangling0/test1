#! /usr/bin/env python
# -*- coding:utf-8
# author:mlh
# datetime:2019/6/13 上午9:47

import unittest
import time
from init import InitTest
from common import login,page
from selenium.webdriver.common.action_chains import ActionChains
import random
from selenium.webdriver.common.by import By
from log import logTest
from common import companyInfo


def select(self):
    self.driver.find_element_by_class_name("My-choice-list").click()
    time.sleep(5)
    ul = self.driver.find_element_by_class_name("dropdown-menu")
    lis = ul.find_elements_by_xpath("li")
    num = random.randint(0, len(lis) - 3)
    lis[num].click()
    time.sleep(5)


def add_company(self):
    '''添加对比公司'''
    logTest.log("开始添加可比公司")
    company = companyInfo.AcompanyInfo(2)
    tags = self.driver.find_elements(By.CLASS_NAME, "tags-input")
    tags[0].send_keys(company)
    time.sleep(5)
    company_menu = self.driver.find_element(By.CLASS_NAME, "company-menu")
    company_li = company_menu.find_element(By.XPATH, "li")
    company_li.click()
    logTest.log("成功添加可比公司")


def del_company(self):
    '''删除已有的公司'''
    logTest.log("开始测试删除添加的可比公司")
    del_div = self.driver.find_element(By.CLASS_NAME, "Switching-comparison")
    del_ul = del_div.find_element(By.XPATH, "ul")
    del_li = del_ul.find_elements(By.XPATH, "li")
    t = random.randint(0, len(del_li) - 1)
    ActionChains(self.driver).move_to_element(del_li[t]).perform()
    time.sleep(3)
    del_delete = del_li[t].find_element(By.CLASS_NAME, "Switching-delete")
    del_delete.click()
    time.sleep(5)
    logTest.log("成功删除添加的可比公司")


def alter_index(self):
    '''指标切换'''
    logTest.log("开始测试指标切换")
    alter_index = self.driver.find_element(By.CSS_SELECTOR, ".small-mor.small-mar")
    alter_index.click()
    time.sleep(5)
    alter_ul = self.driver.find_element(By.CSS_SELECTOR, ".dropdown-menu.lanmu")
    alter_li = alter_ul.find_elements(By.XPATH, "li")
    index = random.randint(0, len(alter_li) - 1)
    index_a = alter_li[index].find_element(By.XPATH, "a")
    index_a.click()
    time.sleep(5)
    logTest.log("指标切换成功")


def add_financial(self):
    '''添加财务指标'''
    logTest.log("开始添加财务指标")
    tags = self.driver.find_elements(By.CLASS_NAME, "tags-input")
    tags[1].click()
    time.sleep(5)
    lis = self.driver.find_elements(By.CLASS_NAME, "small-top")
    t = random.randint(0, len(lis) - 1)
    lis[t].click()
    time.sleep(5)
    index_ul = self.driver.find_element(By.CLASS_NAME, "justforshow")
    index_li = index_ul.find_elements(By.XPATH, "li")
    n = random.randint(0, len(index_li) - 1)
    index_a = index_li[n].find_element(By.XPATH, "a")
    index_a.click()
    time.sleep(5)
    logTest.log("成功添加财务指标")


class MySecurities(InitTest):
    '''测试我的证券和公司信息页面'''

    def test_001_securities(self):
        '''切换到我的证券页面'''
        self.driver.get("http://ibdata.cn/#!/login")
        login.login(self)
        self.driver.find_element_by_link_text("我的证券").click()
        handles = self.driver.window_handles
        global old_handle
        old_handle = self.driver.current_window_handle
        self.driver.switch_to.window(self.driver.window_handles[len(handles) - 1])

    def test_002_securities(self):
        # 获取我的证券的列表
        self.driver.find_element_by_class_name("My-choice-list").click()
        time.sleep(5)
        ul = self.driver.find_element_by_class_name("dropdown-menu")
        lis = ul.find_elements_by_xpath("li")
        num = random.randint(0, len(lis) - 1)

        if num == len(lis) - 1:
            lis[num].click()
            time.sleep(3)
            self.driver.switch_to.default_content()
            time.sleep(3)
            self.driver.find_element_by_class_name("tags-input").send_keys("TestUI" + num + 1)
            self.driver.find_element_by_class_name("btn-add").click()
            time.sleep(3)
            logTest.log("自定义新的证券组合")
        else:
            lis[num].click()
            time.sleep(3)
            logTest.log(lis[num].text)
            # page.page(self)
        time.sleep(5)

    def test_003_securities(self):
        '''删除已有的证券'''
        self.driver.find_element_by_class_name("btn-see").click()
        try:
            lis = self.driver.find_elements_by_class_name("small-delete")
            logTest.log("获取证券列表")
            page.page(self)
            num = random.randint(0, len(lis) - 1)
            lis[num].click()
            time.sleep(5)
            self.driver.switch_to.default_content()
            btn_del = self.driver.find_elements(By.CSS_SELECTOR, ".btn.btn-del.right30")
            btn_del[0].click()
            logTest.log("删除某个证券")
            time.sleep(5)
            self.driver.find_element_by_class_name("btn-complete").click()
            time.sleep(5)

        except Exception as e:
            logTest.log(e)
        time.sleep(5)

    def test_004_securities(self):
        '''区间分析'''

        try:
            contrast = self.driver.find_element_by_class_name("company-contrast-btn")
            self.assertEqual(contrast.text, "区间分析")
            contrast.click()
            logTest.log("点击区间分析")
            time.sleep(15)
            self.driver.switch_to.default_content()
            div = self.driver.find_element_by_class_name("cp-of-down-a")
            div.click()
            time.sleep(5)
            ul = div.find_element(By.XPATH, "ul")
            lis = ul.find_elements_by_xpath("li")
            num = random.randint(0, len(lis) - 1)
            lis[num].find_element_by_xpath("a").click()
            time.sleep(5)
            logTest.log("选择指标，点击")
            self.driver.find_element_by_class_name("delete-icon").click()
        except Exception as e:
            logTest.log(e)

        time.sleep(10)

    def test_005_securities(self):
        '''财务分析'''
        try:
            # 选中证券
            select(self)

            lis = self.driver.find_elements_by_class_name("el-checkbox-inner")
            num1 = random.randint(0, len(lis) - 1)
            lis[num1].click()
            time.sleep(5)
            num2 = random.randint(0, len(lis) - 1)
            if num2 != num1:
                lis[num2].click()
                time.sleep(5)
            else:
                logTest.log("该项已经被选择了")
            # 财务分析
            self.driver.find_element_by_class_name("cata-Contrast").click()
            time.sleep(5)
            self.driver.close()
            handles = self.driver.window_handles
            for handle in handles:
                if handle != old_handle:
                    self.driver.switch_to.window(handle)
                    ul = self.driver.find_element_by_class_name("personnel")
                    ul.find_elements_by_xpath("li")[1].click()
                    time.sleep(3)
                    logTest.log("年度、季度的切换")
                    # 添加对比公司
                    add_company(self)

                    # 添加财务指标
                    add_financial(self)
                    # 指标切换
                    alter_index(self)
                    # 删除对比公司
                    del_company(self)
                    # 删除财务指标
                    del_company(self)
        except Exception as e:
            logTest.log(e)


if __name__ == "__main__":
    unittest.main(verbosity=2)
