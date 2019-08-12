#! /usr/bin/env python
# -*- coding:utf-8
# author:mlh
# datetime:2019/5/16 下午5:56

import unittest
from init import InitTest
import random
from common import login
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def horizontal(self):
    '''选择公告标签'''
    try:
        ul = self.driver.find_element(By.CLASS_NAME, "dropdown-horizontal")
        lis = ul.find_elements(By.XPATH, "li")
        i = 0

        for n in range(len(lis)):
            lis[n].click()

            text = lis[n].find_element(By.XPATH, "a").text

            if text != "地区类型":

                flag1 = self.driver.find_elements(By.CLASS_NAME, "one-row")
                ls = flag1[i].find_elements(By.XPATH, "li")
                num = random.randint(0, len(ls) - 1)
                ls[num].click()
                i += 1
                time.sleep(3)

            elif text == "地区类型":

                flag2 = self.driver.find_element(By.CLASS_NAME, "two-row")  # 地区类型
                ls1 = flag2.find_elements(By.XPATH, "li")
                num = random.randint(0, len(ls1) - 1)
                ls1[num].click()
                time.sleep(2)

            else:
                print("出错了")

    except Exception as e:
        print(e, "没有公告标签")

def Portfolio(self):
    '''证券组合'''
    div= self.driver.find_element(By.CLASS_NAME,"abs-width-a")
    div.click()
    ul = div.find_element(By.XPATH,"ul")
    lis = ul.find_elements(By.XPATH,"li")
    try:
        num = random.randint(1,len(lis)-1)
        lis[num].find_element(By.XPATH,"a").click()
    except Exception as e:
        print(e,"无效的证券组合")

def Select(self):
    '''已选条件'''
    # self.driver.find_element(By.LINK_TEXT, "已选条件").click()
    try:

        self.driver.find_element(By.CLASS_NAME,"selected-condition")

        dele = self.driver.find_elements(By.CLASS_NAME,"small-delete")
        num = random.randint(0,len(dele)-1)
        dele[num].click()
        print(dele[num].text)

    except Exception as e:
        print(e,"已选条件为空")

class Search(InitTest):

    def test_002_search(self):
        self.driver.implicitly_wait(30)
        login.login(self)
        # self.driver.get("http://ibdata.cn/#!/login")
        # self.driver.find_element(By.CLASS_NAME, "input-search-a").clear()
        self.driver.find_element(By.CLASS_NAME, "input-search-a").send_keys("大数据")
        self.driver.find_element("id", "backTo-g").click()
        ul = self.driver.find_element(By.CLASS_NAME,"search-tab-w")
        lis = ul.find_elements(By.XPATH,"li")
        print(len(lis))

        for i in range(len(lis)):
            #:
                # print(i)
            lis[i].click()
            # print(i)

            try:
                horizontal(self)
            except Exception as e:
                print(e)
            self.driver.find_element(By.CLASS_NAME, "search-bot").click()
            time.sleep(3)
            # 搜索结果
            if lis[i] != "综合":
                # 搜索结果的标签
                try:
                    div = self.driver.find_elements(By.CLASS_NAME, "notice-board")
                    for n in range(len(div)):
                        ul = div[n].find_element(By.XPATH, "ul")
                        lis = ul.find_elements(By.XPATH, "li")
                        num = random.randint(0, len(lis)-1)
                        lis[num].find_elements((By.CLASS_NAME, "el-checkbox")).click()
                except Exception as e:
                    print(e)
                # 下载和收藏
                try:
                    self.driver.find_element(By.ID,"download_0").click() # 下载
                    load = self.driver.find_elements(By.CLASS_NAME,"small-down")
                    t = random.randint(0,len(load)-1)
                    load[t].click()
                    time.sleep(3)
                    ul = self.driver.find_elements(By.CLASS_NAME,"green")
                    num2 = random.randint(0,len(ul)-1)
                    ul[num2].click()
                    self.driver.switch_to.default_content()
                    self.driver.find_element(By.CLASS_NAME,'tag-choice-list').click()
                    lis2 = self.driver.find_elements(By.CLASS_NAME,"left")
                    num3 = random.randint(0,len(lis2)-1)
                    lis2[num3].click()
                    self.driver.find_element(By.CLASS_NAME,"collect-Tag-bot").click()
                    self.driver.switch_to.default_content()
                    self.driver.find_element(By.CLASS_NAME,"right30").click()

                except Exception as e:
                    print(e)

            else:
                t = self.driver.find_elements(By.CLASS_NAME,"compre-more")
                num = random.randint(0,len(t)-1)
                t[num].click()


                ul = self.driver.find_element(By.CLASS_NAME,"fixedmeau")
                lis = ul.find_elements(By.XPATH,"li")
                num = random.randint(0,len(lis)-1)
                lis[num].click()


            ul = self.driver.find_element(By.CLASS_NAME, "search-tab-w")
            lis = ul.find_elements(By.XPATH, "li")


if __name__ == "__main__":
    unittest.main(verbosity=2)








# def title(self):
#     ''' 选择标题 '''
#     self.driver.find_element_by_class_name("keyword-title").click()
#     time.sleep(2)
#     ul = self.driver.find_element_by_class_name("lanmu")
#     lis = ul.find_elements_by_xpath("li")
#
#     for i in range(len(lis)):
#         try:
#             EC.visibility_of_element_located(ul.find_elements_by_xpath("li")[i])
#             ul.find_elements_by_xpath("li")[i].click()
#             print(ul.find_elements_by_xpath("li")[i])
#             self.driver.find_element_by_class_name("keyword-title").click()
#
#         except Exception as e:
#             self.driver.find_element_by_class_name("keyword-title").click()
#             print(e,"不可见")
#
# def keyword(self):
#     '''包含全部/任意关键词'''
#     self.driver.find_element_by_class_name("small-add").click()
#     time.sleep(2)
#     self.driver.find_element_by_class_name("small-cut").click()
#     self.driver.find_element_by_class_name("keyword-down-b").click()
#     time.sleep(3)
#     ul = self.driver.find_elements_by_class_name("dropdown-menu")[2]
#     lis = ul.find_elements_by_xpath("li")
#     for i in range(1,len(lis)):
#         li = ul.find_elements_by_xpath("li")[i]
#         li.find_element_by_xpath("a").click()
#         self.driver.find_element_by_class_name("keyword-down-b").click()
#
# def AnnouncementType(self,a,c):
#     '''公告类型'''
#
#     self.driver.find_elements_by_class_name("dio-type")[a].click()
#     time.sleep(2)
#     ul = self.driver.find_elements_by_class_name("one-row")[0]
#     lis = ul.find_elements_by_xpath("li")
#     for i in range(len(lis)):
#         li = ul.find_elements_by_xpath("li")[i]
#         li.find_element_by_xpath("a").click()
#         time.sleep(10)
#         Local(self,c)
#         empty(self)
#         self.driver.find_element_by_class_name("input-search-a").send_keys(" ")
#         self.driver.find_elements_by_class_name("dio-type")[a].click()
#
# def exist(self):
#     '''存为标签'''
#     self.driver.find_elements_by_class_name("exist-btn-empty")[1].click()
#     self.driver.switch_to.default_content()
#     self.driver.find_element_by_class_name("cle").click()
#     self.driver.find_elements_by_class_name("exist-btn-empty")[1].click()
#     self.driver.switch_to.default_content()
#     self.driver.find_element_by_class_name("wo-bk").send_keys("自动化测试")
#     self.driver.find_element_by_class_name("o-baocn").click()
#
# def empty(self):
#     '''清空条件'''
#     self.driver.find_elements_by_class_name("exist-btn-empty")[0].click()
#
# def ModuleTypes(self,a,b,c):
#     '''板块类型'''
#     self.driver.find_elements_by_class_name("dio-type")[b].click()
#     time.sleep(2)
#     ul = self.driver.find_elements_by_class_name("one-row")[1]
#     lis = ul.find_elements_by_xpath("li")
#     for i in range(len(lis)):
#         li = ul.find_elements_by_xpath("li")[i]
#         li.find_element_by_xpath("a").click()
#         time.sleep(10)
#         AnnouncementType(self,a,c)
#         empty(self)
#         self.driver.find_element_by_class_name("input-search-a").send_keys(" ")
#         self.driver.find_elements_by_class_name("dio-type")[b].click()
#
# def Local(self,c):
#     '''地区类型'''
#     self.driver.find_elements_by_class_name("dio-type")[c].click()
#     time.sleep(2)
#     ul = self.driver.find_element_by_class_name("two-row")
#     lis = ul.find_elements_by_xpath("li")
#     for i in range(len(lis)):
#         li = ul.find_elements_by_xpath("li")[i]
#         li.find_element_by_xpath("a").click()
#         time.sleep(10)
#         empty(self)
#         self.driver.find_element_by_class_name("input-search-a").send_keys(" ")
#         self.driver.find_elements_by_class_name("dio-type")[c].click()
#
# def Classification(self,d,d1):
#     '''行业分类'''
#     self.driver.find_elements_by_class_name("dio-type")[d].click()
#     time.sleep(2)
#     ul = self.driver.find_elements_by_class_name("one-row")[d1]
#     lis = ul.find_elements_by_xpath("li")
#     for i in range(len(lis)):
#         li = ul.find_elements_by_xpath("li")[i]
#         li.find_element_by_xpath("a").click()
#         time.sleep(10)
#         empty(self)
#         self.driver.find_element_by_class_name("input-search-a").send_keys(" ")
#         self.driver.find_elements_by_class_name("dio-type")[d].click()
#
# def Portfolio(self,e):
#     '''证券组合'''
#     self.driver.find_elements_by_class_name("small-mor")[e].click()
#     time.sleep(2)
#     ul = self.driver.find_elements_by_class_name("mydropdown")[3]
#     time.sleep(3)
#     lis = ul.find_elements_by_xpath("li")
#     for i in range(1,len(lis)):
#         li = ul.find_elements_by_xpath("li")[i]
#         try:
#             li.find_element_by_xpath("a").click()
#             time.sleep(10)
#             self.driver.find_elements_by_class_name("small-mor")[e].click()
#         except Exception as e:
#             print(li,e)
#
# def HostBroker(self,f):
#     '''主办券商'''
#     self.driver.find_elements_by_class_name("dio-type")[f].click()
#     time.sleep(3)
#     ul = self.driver.find_elements_by_class_name("one-row")[2]
#     lis = ul.find_elements_by_xpath("li")
#     for i in range(len(lis)):
#         lis[i].find_element_by_xpath("a").click()
#         time.sleep(10)
#         empty(self)
#         self.driver.find_element_by_class_name("input-search-a").send_keys(" ")
#         self.driver.find_elements_by_class_name("dio-type")[f].click()
#
# def QuestionType(self,g,h,h1):
#     '''公告类型'''
#
#     self.driver.find_elements_by_class_name("dio-type")[g].click()
#     time.sleep(2)
#     ul = self.driver.find_elements_by_class_name("one-row")[0]
#     lis = ul.find_elements_by_xpath("li")
#     for i in range(len(lis)):
#         li = ul.find_elements_by_xpath("li")[i]
#         li.find_element_by_xpath("a").click()
#         time.sleep(10)
#         Classification(self,h,h1)
#         empty(self)
#         self.driver.find_element_by_class_name("input-search-a").send_keys(" ")
#         self.driver.find_elements_by_class_name("dio-type")[g].click()
#
# def ResearchReportType(self):
#     '''研报类型'''
#     self.driver.find_element_by_class_name("dio-type").click()
#     ul = self.driver.find_element_by_class_name("one-row")
#     lis = ul.find_elements_by_xpath("li")
#     for i in range(len(lis)):
#         lis[i].find_element_by_xpath("a").click()
#         time.sleep(10)
#         empty(self)
#         self.driver.find_element_by_class_name("input-search-a").send_keys(" ")
#         self.driver.find_element_by_class_name("dio-type").click()
#
#
# class SearchFirst(InitTest):
#     '''测试信批搜索'''
#
#     def test_01_search(self):
#         '''测试A股'''
#         self.driver.get("http://ibdata.cn/#!/login")
#         login.login(self)
#         time.sleep(2)
#
#         # 标题等
#         # search1.title(self)
#
#         # 点击“高级搜索”
#         self.driver.find_element_by_class_name("search-icon-blue").click()
#         self.driver.find_element_by_class_name("input-search-a").send_keys(" ")
#         self.driver.find_element_by_class_name("search-bot").click()
#         time.sleep(5)
#         # 是否包含关键词
#         # keyword(self)
#         # # 输入搜索内容
#         # self.driver.find_element_by_class_name("input-search-a").send_keys("大数据 科技")
#         # 公告类型
#         # AnnouncementType(self,0,2)
#         # 板块类型
#         # ModuleTypes(self,0,1,2)
#         # 地区类型
#         # Local(self,2)
#         # 行业分类
#         # Classification(self,3,2)
#         # 证券组合
#         # Portfolio(self,7)
#
#
#     def test_02_searchN3B(self):
#         '''测试新三板'''
#         # self.driver.get("http://ibdata.cn/#!/search")
#         # 定位到新三板
#         ul = self.driver.find_element_by_class_name("search-tab-w")
#         li = ul.find_elements_by_xpath("li")[2]
#         li.find_element_by_xpath("a").click()
#         # 点击“高级搜索”
#         # self.driver.find_element_by_class_name("search-icon-blue").click()
#         # self.driver.find_element_by_class_name("input-search-a").send_keys(" ")
#         # 地区类型
#         Local(self, 2)
#         self.driver.find_element_by_class_name("search-bot").click()
#         time.sleep(3)
#         # 主办券商
#         # HostBroker(self,3)
#         # 证券组合
#         # Portfolio(self,8)
#         # 公告类型
#         # AnnouncementType(self,0,2)
#         # 板块类型
#         # ModuleTypes(self,0,1,2)
#         # 行业类型
#         # Classification(self,4,3)
#
#
#     def test_03_searchH(self):
#         '''测试港股'''
#         # self.driver.get("http://ibdata.cn/#!/search")
#         # 定位到新港股
#         ul = self.driver.find_element_by_class_name("search-tab-w")
#         li = ul.find_elements_by_xpath("li")[3]
#         li.find_element_by_xpath("a").click()
#         # 点击“高级搜索”
#         # self.driver.find_element_by_class_name("search-icon-blue").click()
#         # self.driver.find_element_by_class_name("input-search-a").send_keys(" ")
#         self.driver.find_element_by_class_name("search-bot").click()
#         time.sleep(3)
#
#         # 证券组合
#         Portfolio(self,3)
#
#
#     def test_04_searchBond(self):
#         '''测试债券'''
#
#         # self.driver.get("http://ibdata.cn/#!/login")
#         # login.login(self)
#         # 定位到债券
#         ul = self.driver.find_element_by_class_name("search-tab-w")
#         li = ul.find_elements_by_xpath("li")[4]
#         li.find_element_by_xpath("a").click()
#         # 点击“高级搜索”
#         # self.driver.find_element_by_class_name("search-icon-blue").click()
#         # self.driver.find_element_by_class_name("input-search-a").send_keys(" ")
#         self.driver.find_element_by_class_name("search-bot").click()
#         time.sleep(3)
#         # 公告类型
#         # AnnouncementType(self,0,1)
#         # 证券组合
#         # Portfolio(self,5)
#         # 地区
#         Local(self,1)
#
#
#     def test_05_searchAnswer(self):
#         '''测试问题库'''
#         # self.driver.get("http://ibdata.cn/#!/login")
#         # login.login(self)
#         # 定位到问题库
#         ul = self.driver.find_element_by_class_name("search-tab-w")
#         li = ul.find_elements_by_xpath("li")[5]
#         li.find_element_by_xpath("a").click()
#         # 点击“高级搜索”
#         # self.driver.find_element_by_class_name("search-icon-blue").click()
#         # self.driver.find_element_by_class_name("input-search-a").send_keys(" ")
#         Classification(self, 1, 1)
#         self.driver.find_element_by_class_name("search-bot").click()
#         time.sleep(3)
#         # 问题类型
#         # QuestionType(self,0,1,1)
#         # 行业分类
#
#
#     def test_06_searchwechat(self):
#         '''测试知识库'''
#         # self.driver.get("http://ibdata.cn/#!/login")
#         # login.login(self)
#         # 定位到知识库
#         ul = self.driver.find_element_by_class_name("search-tab-w")
#         li = ul.find_elements_by_xpath("li")[6]
#         li.find_element_by_xpath("a").click()
#         # 点击“高级搜索”
#         # self.driver.find_element_by_class_name("search-icon-blue").click()
#         # self.driver.find_element_by_class_name("input-search-a").send_keys(" ")
#         self.driver.find_element_by_class_name("search-bot").click()
#         time.sleep(3)
#
#
#     def test_07_searchABS(self):
#         '''测试ABS'''
#         # self.driver.get("http://ibdata.cn/#!/login")
#         # login.login(self)
#         # 定位到ABS
#         ul = self.driver.find_element_by_class_name("search-tab-w")
#         li = ul.find_elements_by_xpath("li")[7]
#         li.find_element_by_xpath("a").click()
#         # 点击“高级搜索”
#         # self.driver.find_element_by_class_name("search-icon-blue").click()
#         self.driver.find_element_by_class_name("input-search-a").send_keys(" ")
#         self.driver.find_element_by_class_name("search-bot").click()
#         time.sleep(3)
#
#
#     def test_08_searchResearchReport(self):
#         '''测试研报'''
#         # self.driver.get("http://ibdata.cn/#!/login")
#         # login.login(self)
#         # 定位到研报
#         ul = self.driver.find_element_by_class_name("search-tab-w")
#         li = ul.find_elements_by_xpath("li")[8]
#         li.find_element_by_xpath("a").click()
#         # 点击“高级搜索”
#         # self.driver.find_element_by_class_name("search-icon-blue").click()
#         # self.driver.find_element_by_class_name("input-search-a").send_keys(" ")
#         ResearchReportType(self)
#         time.sleep(3)
#
#
#     def test_09_searchNews(self):
#         '''测试新闻'''
#         # self.driver.get("http://ibdata.cn/#!/login")
#         # login.login(self)
#         # 定位到新闻
#         ul = self.driver.find_element_by_class_name("search-tab-w")
#         li = ul.find_elements_by_xpath("li")[9]
#         li.find_element_by_xpath("a").click()
#         # 点击“高级搜索”
#         # self.driver.find_element_by_class_name("search-icon-blue").click()
#         # self.driver.find_element_by_class_name("input-search-a").send_keys(" ")
#         self.driver.find_element_by_class_name("search-bot").click()
#         time.sleep(3)
#
#
# if __name__ == "__main__":
#     unittest.main(verbosity=2)
