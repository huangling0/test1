#! /usr/bin/env python
# -*- coding:utf-8
# author:mlh
# datetime:2019/5/31 下午5:36

import time
from init import InitTest
from common import login, page, code
import random
import unittest
from log import logTest
from selenium.webdriver.common.by import By


def delt(self):
    '''删除已经创建的项目'''
    try:
        dele = self.driver.find_elements_by_class_name("search-delete")
        logTest.log("项目已存在")
        num = random.randint(0, len(dele)-1)
        dele[num].click()
        logTest.log("点击删除")
        time.sleep(3)

        self.driver.switch_to.default_content()
        dele2 = self.driver.find_elements_by_class_name("btn-primary")
        num2 = random.randint(0, len(dele2)-1)
        print(num2)
        logTest.log("确定 or 取消？")
        dele2[num2].click()
        time.sleep(3)
        if num2 == 0:
            logTest.log("已经删除其中的某个项目")
        else:
            logTest.log("已经取消删除该项目")
    except Exception as e:
        logTest.log(e)


def creat(self):
    '''创建新的项目'''
    self.driver.find_element_by_class_name("Establish-btn").click()
    logTest.log("开始创建新项目")
    # 项目信息
    company_code = code.Acode()
    self.driver.find_elements_by_class_name("input-name")[0].send_keys(company_code)
    ul = self.driver.find_element_by_class_name("company-menu")
    lis0 = ul.find_element_by_xpath("li")
    lis0.click()
    logTest.log("点击输入项目的代码")

    # 选择项目类型
    div = self.driver.find_element_by_class_name("project-a")
    ul1 = div.find_element_by_xpath("ul")
    lis1 = ul1.find_elements_by_xpath("li")
    num2 = random.randint(0, len(lis1)-1)
    print(num2)
    time.sleep(3)
    lis1[num2].click()
    logTest.log("选择项目类型")
    # 选择业务类型
    lis3 = self.driver.find_elements_by_class_name("project-b-box1")
    num3 = random.randint(0, len(lis3)-1)
    print(num3)
    time.sleep(3)
    lis3[num3].click()
    logTest.log("选择业务类型")
    # 点击下一步
    self.driver.find_element_by_class_name("step-btn").click()
    time.sleep(60)
    # 添加可比公司
    self.driver.find_element_by_link_text("主营业务").click()
    self.driver.switch_to.default_content()
    time.sleep(3)
    # self.driver.find_element_by_xpath("//*[@id='wrapper']/div[3]/div/div/div/div[2]/div/ul/li[2]/a").click()
    # ul = self.driver.find_elements(By.CSS_SELECTOR, ".search-tab-w.search-b")
    # pro = ul[1].find_elements(By.XPATH, "li")
    pro1 = self.driver.find_element(By.CSS_SELECTOR,
    "#wrapper>div.modal.fade.in>div>div>div>div.search-nun-tags>div>ul>li:nth-child(2)>a")
    pro1.click()
    logTest.log("查看主营业务和主要产品")
    time.sleep(5)
    try:
        global td
        td = self.driver.find_element_by_xpath(
            "//*[@id='wrapper']/div[3]/div/div/div/div[3]/div/table/tbody/tr[1]/td[1]")
        print(td.text)
    except Exception as e:
        logTest.log(e)
        print(e)
    self.driver.find_element_by_class_name("delete-icon").click()
    logTest.log("准备输入可比公司")
    ul = self.driver.find_element_by_class_name("search-tab-w")
    lis4 = ul.find_elements_by_xpath("li")
    num4 = random.randint(0, len(lis4)-1)
    print(num4)
    lis4[num4].click()
    time.sleep(5)
    if num4 == 3:
        try:
            t3 = self.driver.find_elements_by_class_name("time")
            num5 = random.randint(0, len(t3)-1)
            print(num5)
            t3[num5].click()
            time.sleep(5)
        except Exception as e:
            logTest.log(e)
            logTest.log("没有适合的可比公司")
    else:
        # td = self.driver.find_element_by_xpath(
        #     "//*[@id='wrapper']/div[3]/div/div/div/div[3]/div/table/tbody/tr[1]/td[1]")
        try:
            text1 = td.text
            if text1 != " ":
                self.driver.find_element_by_class_name("input-search-a").send_keys(text1)
                self.driver.find_element_by_class_name("search-bot").click()
                try:
                    t3 = self.driver.find_elements_by_class_name("time")
                    num5 = random.randint(0, len(t3)-1)
                    print(num5)
                    time.sleep(3)
                    t3[num5].click()
                except Exception as e:
                    # print(e, "没有适合的可比公司")
                    logTest.log(e)
                    logTest.log("没有适合的可比公司")
            else:
                pass
        except Exception as e:
            logTest.log(e)
    step_btn = self.driver.find_element_by_class_name("step-btn")
    step_btn.click()
    logTest.log("点击下一步")
    time.sleep(3)
    start_btn = self.driver.find_element_by_class_name("start-btn")
    start_btn.click()
    logTest.log("点击保存")
    time.sleep(60)
    stop = self.driver.find_element(By.CLASS_NAME, "stop")
    stop.click()
    logTest.log("点击返回项目尽调")
    time.sleep(5)


def alter(self):
    '''修改项目'''
    page.page(self)
    time.sleep(5)
    titles = self.driver.find_elements_by_class_name("aproject-cont-left")
    # print(titles)
    num = random.randint(0, len(titles)-1)
    # print(num)
    title = titles[num].find_element_by_xpath("p")
    title.find_element_by_xpath("a").click()
    logTest.log("修改已存在的项目")
    time.sleep(2)
    # 编辑全文
    eit_btn = self.driver.find_element_by_class_name("eit-btn")
    eit_btn.click()
    time.sleep(15)
    logTest.log("编辑全文")
    # 预览/保存
    eit = self.driver.find_elements_by_class_name("eit-btn")
    num2 = random.randint(0, len(eit)-1)
    # print(num2)
    eit[num2].click()
    time.sleep(30)
    logTest.log("预览/保存")
    # 生成报告
    report = self.driver.find_element_by_class_name("Report-btn")
    report.click()
    time.sleep(60)
    logTest.log("生成报告")
    # 返回
    ti = self.driver.find_element_by_class_name("stop")
    ti.click()
    time.sleep(5)
    logTest.log("返回主页面")


class Survey(InitTest):
    '''测试项目尽调'''

    def test_001_survey(self):
        '''打开尽调页面'''
        self.driver.get("http://ibdata.cn/#!/login")
        login.login(self)
        logTest.log("登陆成功")
        self.driver.find_element_by_link_text("项目尽调").click()
        time.sleep(5)
        # old_handle = self.driver.current_window_handle
        handles = self.driver.window_handles
        self.driver.switch_to.window(self.driver.window_handles[len(handles)-1])
        logTest.log("页面转到项目尽调")

    def test_002_survey(self):
        ''' 删除已有的项目'''
        page.page(self)
        delt(self)
        page.page(self)
        time.sleep(3)
        delt(self)
        time.sleep(3)
        page.page(self)
        delt(self)
        time.sleep(3)

    def test_004_survey(self):
        '''创建新项目'''
        creat(self)
        # self.driver.switch_to.window(old_handle)
        # self.driver.get("http://dd.ibdata.cn/#/survey")
        # handles = self.driver.window_handles
        # self.driver.switch_to.window(self.driver.window_handles[len(handles)-1])

    def test_005_survey(self):
        '''修改项目'''
        alter(self)

    def test_003_survey(self):
        '''搜索已有项目'''
        logTest.log("开始搜索已有项目：")
        inp = self.driver.find_element(By.ID, "blurinput")
        self.assertTrue(inp.is_enabled())
        inp.send_keys("科技")
        logTest.log("输入搜索的关键词")
        self.driver.find_element(By.CLASS_NAME, "r-search-c").click()
        logTest.log("查看有多少个搜索结果：")
        time.sleep(3)
        try:
            titles = self.driver.find_elements(By.CLASS_NAME, "aproject-cont-left")

            num = len(titles)

            logTest.log(print("当前页面获得相关项目:", num))
        except Exception as e:
            logTest.log(e)

        self.driver.find_element(By.CLASS_NAME, "Return-list-btn").click()
        logTest.log("清空搜索条件")
        time.sleep(3)


if __name__ == "__main__":
    unittest.main(verbosity=2)


