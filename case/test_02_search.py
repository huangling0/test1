#! /usr/bin/env python
# -*- coding:utf-8
# author:mlh
# datetime:2019/5/16 下午5:11

import unittest
import time
from common import login, page
from init import InitTest
import random
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from log import logTest
from selenium.webdriver.common.action_chains import ActionChains


def horizontal(self):
    '''选择公告标签'''
    try:
        ul = self.driver.find_element(By.CLASS_NAME, "dropdown-horizontal")
        lis = ul.find_elements(By.XPATH, "li")
        i = 0
        logTest.log("选择公告类型")

        for n in range(len(lis)):
            lis[n].click()
            time.sleep(3)
            text1 = lis[n].find_element(By.XPATH, "a")
            text = text1.text

            if text != "地区类型":
                self.assertNotEqual(text, "地区类型")
                flag1 = self.driver.find_elements(By.CLASS_NAME, "one-row")
                ls = flag1[i].find_elements(By.XPATH, "li")
                num = random.randint(0, len(ls) - 1)
                logTest.log(ls[num].text)
                ls[num].click()
                time.sleep(60)
                i += 1
                time.sleep(3)
                logTest.log("选择非地区类型")

            elif text == "地区类型":
                self.assertEqual(text, "地区类型")
                flag2 = self.driver.find_element(By.CLASS_NAME, "two-row")  # 地区类型
                ls1 = flag2.find_elements(By.XPATH, "li")
                num = random.randint(0, len(ls1) - 1)
                ls1[num].click()
                time.sleep(60)
                logTest.log("地区类型")

            else:
                print("出错了")
                logTest.log("出错了")

    except Exception as e:
        logTest.log(e)
        print(e, "没有公告标签")


def Portfolio(self):
    '''证券组合'''
    div = self.driver.find_element(By.CLASS_NAME, "abs-width-a")
    div.click()
    ul = div.find_element(By.XPATH, "ul")
    lis = ul.find_elements(By.XPATH, "li")
    logTest.log("选择证券组合")
    try:
        num = random.randint(1, len(lis) - 1)
        lis[num].find_element(By.XPATH, "a").click()
        time.sleep(3)
        logTest.log("已经选择证券组合")
    except Exception as e:
        logTest.log(e)
        print(e, "无效的证券组合")


def Select(self):
    '''已选条件'''
    # self.driver.find_element(By.LINK_TEXT, "已选条件").click()
    try:
        self.driver.find_element(By.CLASS_NAME, "selected-condition")
        dele = self.driver.find_elements(By.CLASS_NAME, "small-delete")
        num = random.randint(0, len(dele) - 1)
        dele[num].click()
        print(dele[num].text)

    except Exception as e:
        print(e, "已选条件为空")


def more(self):
    '''获取热门资讯的‘更多‘，并进行操作'''
    elements = self.driver.find_elements_by_class_name("notice-seo-more")
    logTest.log("点击更多后的操作")
    for i in range(len(elements)):
        seo_more = self.driver.find_elements_by_class_name("notice-seo-more")
        seo_more[i].click()
        time.sleep(10)
        page.page(self)
        time.sleep(5)
        return_btn = self.driver.find_element_by_class_name("notice-return-btn")
        return_btn.click()
        time.sleep(10)


def Industry(self):
    '''行业'''
    try:

        div = self.driver.find_element(By.CLASS_NAME, "hot-industry-cont")
        logTest.log("如果有行业类别，则执行：")
        ul = div.find_element(By.XPATH, "ul")
        lis = ul.find_elements(By.XPATH, "li")
        for i in range(len(lis)):
            logTest.log(lis[i].text)
            lis[i].click()
            time.sleep(60)

            div = self.driver.find_element(By.CLASS_NAME, "hot-industry-cont")
            ul = div.find_element(By.XPATH, "ul")
            lis = ul.find_elements(By.XPATH, "li")

    except Exception as e:
        logTest.log(e)


class Search(InitTest):
    '''测试信披搜索'''

    def test_001_search(self):
        self.driver.get("http://ibdata.cn/#!/login")
        login.login(self)

    def test_002_search(self):
        '''热门资讯的切换'''
        logTest.log("执行信批搜索的热门资讯:")
        '''热门资讯（A股、新三板等）'''
        logTest.log("开始执行热门资讯之间的切换执行：")
        div = self.driver.find_element(By.CLASS_NAME, "notice-hot-header")
        ul = div.find_element(By.XPATH, "ul")
        lis = ul.find_elements(By.XPATH, "li")
        for i in range(len(lis)):
            lis[i].click()
            time.sleep(30)
            if lis[i].text == "A股" or lis[i].text == "新三板":
                logTest.log(lis[i].text)
                more(self)
            elif lis[i].text == "行业":
                logTest.log(lis[i].text)
                Industry(self)
            else:
                time.sleep(60)
                logTest.log("对行政许可执行的操作")
                logTest.log("行政许可")
            div = self.driver.find_element(By.CLASS_NAME, "notice-hot-header")
            ul = div.find_element(By.XPATH, "ul")
            lis = ul.find_elements(By.XPATH, "li")
        logTest.log("成功测试信批搜索的热门资讯")

    def test_003_search(self):
        ''' 测试不同模块的搜索功能和搜索结果 '''
        self.driver.get("http://ibdata.cn/#!/search")
        # login.login(self)
        time.sleep(60)
        self.driver.find_element(By.ID, "backTo-g").click()
        logTest.log("点击高级搜索")
        time.sleep(3)
        global search
        search = self.driver.find_element(By.CLASS_NAME, "input-search-a")
        global btn
        btn = self.driver.find_element(By.CLASS_NAME, "search-bot")
        search.send_keys("大数据")
        ul = self.driver.find_element(By.CLASS_NAME, "search-tab-w")
        lis = ul.find_elements(By.XPATH, "li")
        for i in range(len(lis)):
            #:
            # print(i)
            lis[i].click()
            time.sleep(5)
            # 搜索结果
            if lis[i].text != "综合" and lis[i].text != "研报":
                # t =lis[i].text
                logTest.log(lis[i].text)
                search = self.driver.find_element(By.CLASS_NAME, "input-search-a")
                btn = self.driver.find_element(By.CLASS_NAME, "search-bot")
                search.clear()
                search.send_keys(" ")
                try:
                    horizontal(self)
                    logTest.log("标签")
                except Exception as e:
                    print(e)
                    logTest.log(e)
                time.sleep(60)
                self.driver.find_elements(By.CLASS_NAME, "exist-btn-empty")[0].click()
                search.clear()
                search.send_keys(" ")
                btn.click()
                time.sleep(30)
                logTest.log("对搜索结果的执行：")
                try:
                    self.driver.find_elements(By.CLASS_NAME, "notice-board")
                    lis = self.driver.find_elements(By.CSS_SELECTOR, ".el-checkbox.mar")
                    num = random.randint(2, len(lis) - 1)
                    logTest.log(lis[num].text)
                    lis[num].find_element(By.CLASS_NAME, "el-checkbox-input").click()
                    logTest.log("点击结果标签li")
                    time.sleep(30)
                    logTest.log("结果有标签的执行")
                except Exception as e:
                    # print(e)
                    logTest.log(e)
                # 下载和收藏
                try:
                    download = self.driver.find_element(By.CLASS_NAME, "download_0")  # 下载
                    download.click()
                    logTest.log("下载的执行 ")
                    load = self.driver.find_elements(By.CLASS_NAME, "small-down")
                    t = random.randint(0, len(load) - 1)
                    load[t].click()
                    time.sleep(3)
                    logTest.log("收藏的执行开始")
                    ul = self.driver.find_elements(By.CLASS_NAME, "small-collect-n")
                    num2 = random.randint(0, len(ul) - 1)
                    ul[num2].click()
                    time.sleep(3)
                    self.driver.switch_to.default_content()
                    title = self.driver.find_element(By.CLASS_NAME, "collect-Tag-header")
                    self.assertEqual(title.text, "添加到标签")
                    choice = self.driver.find_element(By.CLASS_NAME, 'tag-choice-list')
                    choice.click()
                    time.sleep(3)
                    ul = choice.find_element(By.XPATH, "ul")
                    lis2 = ul.find_elements(By.XPATH, "li")
                    # print("有多少个left：", len(lis2))
                    num3 = random.randint(0, len(lis2) - 1)
                    lis2[num3].click()
                    time.sleep(3)
                    if num3 != len(lis2)-1:
                        tag = self.driver.find_element(By.CLASS_NAME, "collect-Tag-bot")
                        self.assertEqual(tag.text, "添加")
                        tag.click()
                        time.sleep(3)
                        self.driver.switch_to.default_content()
                        self.driver.find_element(By.CLASS_NAME, "right30").click()
                        logTest.log("已经收藏")
                    else:
                        tags_input = self.driver.find_element(By.CLASS_NAME, "tags-input")
                        tags_input.send_keys("UI_test", len(lis2))
                        btn_add = self.driver.find_element(By.CLASS_NAME, "btn-add")
                        btn_add.click()
                        time.sleep(5)
                        # 如果标签名字已存在
                        try:
                            btn_del = self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-del.right30")
                            btn_del.click()
                        except Exception as e:
                            logTest.log(e)
                except Exception as e:
                    # print(e)
                    logTest.log(e)
            elif lis[i].text == "综合":
                btn.click()
                time.sleep(30)
                logTest.log("综合")
                t = self.driver.find_elements(By.CLASS_NAME, "compre-more")
                num = random.randint(0, len(t) - 1)
                t[num].click()
                logTest.log("点击查看更多")
                time.sleep(10)
            else:
                btn.click()
                time.sleep(60)
                try:
                    more_a = self.driver.find_elements(By.CLASS_NAME, "Notes-triangle-b")
                    index = random.randint(0, len(more_a)-1)
                    more_a[index].click()
                    logTest.log("点击展开")
                except Exception as e:
                    logTest.log(e)
                notice_board = self.driver.find_elements(By.CLASS_NAME, "notice-board")
                num_no = random.randint(1, len(notice_board)-1)
                ul = notice_board[num_no].find_element(By.XPATH, "ul")
                try:
                    li = ul.find_elements(By.XPATH, "li")
                    num_li = random.randint(0, len(li)-1)
                    label = li[num_li].find_element(By.XPATH, "label")
                    logTest.log(label.text)
                    label.click()
                    time.sleep(5)
                    try:
                        self.driver.switch_to.default_content()
                        page.page(self)
                        restags_cont = self.driver.find_element(By.CSS_SELECTOR, ".restags-cont-abs")
                        table = restags_cont.find_element(By.CSS_SELECTOR, ".table-od.line-h")
                        tr_list = table.find_elements(By.CSS_SELECTOR, ".rb.odd")
                        n = random.randint(0, len(tr_list)-1)
                        td = tr_list[n].find_element(By.XPATH, "td")
                        a = td.find_element(By.CSS_SELECTOR, ".green.cpw-cursor")
                        logTest.log(a.text)
                        try:
                            xz_sc = td.find_element(By.CSS_SELECTOR, ".xz-sc.left")
                            lis_a = xz_sc.find_elements_by_xpath("a")
                            t = random.randint(0, len(lis_a)-1)
                            logTest.log(lis_a[t].text)
                            lis_a[t].click()
                            time.sleep(5)
                            try:
                                self.driver.switch_to.default_content()
                                product_personnel = self.driver.find_element(By.CSS_SELECTOR, ".product-personnel")
                                product_li = product_personnel.find_elements_by_xpath("li")
                                p = random.randint(0, len(product_li)-1)
                                logTest.log(product_li[p].text)
                                product_li[p].click()
                                time.sleep(5)
                                if product_li[p].text == "观点":
                                    point = self.driver.find_element(By.CSS_SELECTOR, ".yanbao-coll-pro")
                                    tbody = point.find_element(By.XPATH, "tbody")
                                    tr_list = tbody.find_elements(By.XPATH, "tr")
                                    ActionChains(self.driver).move_to_element(tr_list[0]).perform()
                                    time.sleep(5)
                                    a = self.driver.find_elements(By.CSS_SELECTOR, ".login-close")
                                    a[1].click()
                                else:
                                    a = self.driver.find_elements(By.CSS_SELECTOR, ".login-close")
                                    a[1].click()
                            except Exception as e:
                                logTest.log(e)
                        except Exception as e:
                            logTest.log(e)
                        delt = self.driver.find_element(By.CSS_SELECTOR, ".delete-icon")
                        delt.click()
                    except Exception as e:
                        logTest.log(e)
                except Exception as e:
                    logTest.log(e)
                    logTest.log("被隐藏")
            ul = self.driver.find_element(By.CLASS_NAME, "search-tab-w")
            lis = ul.find_elements(By.XPATH, "li")

    def test_004_search(self):
        '''test我的标签'''
        self.driver.get("http://ibdata.cn/#!/search")
        time.sleep(5)
        # login.login(self)
        tag = self.driver.find_element(By.CLASS_NAME, "my-tagged")
        ul = tag.find_element(By.XPATH, "ul")
        li = ul.find_element(By.XPATH, "li")
        a = li.find_element(By.XPATH, "a")
        self.assertEqual(a.text, "我的标签")
        tag_list = self.driver.find_element(By.CLASS_NAME, "my-tagged-list")
        ul_list = tag_list.find_element(By.XPATH, "ul")
        li_list = ul_list.find_elements(By.XPATH, "li")
        num = random.randint(0, len(li_list)-1)
        ActionChains(self.driver).move_to_element(li_list[num]).perform()
        logTest.log("鼠标放到选择的元素上")
        time.sleep(5)
        span = li_list[num].find_element(By.XPATH, "span")
        logTest.log("定位到删除log")
        self.driver.execute_script("arguments[0].scrollIntoView();", span)
        logTest.log("当前元素所在位置处")
        span.click()
        logTest.log("删除选择的标签")
        time.sleep(3)
        tag_list1 = self.driver.find_element(By.CLASS_NAME, "my-tagged-list")
        ul_list1 = tag_list1.find_element(By.XPATH, "ul")
        li_list1 = ul_list1.find_elements(By.XPATH, "li")
        num2 = random.randint(0, len(li_list1)-1)
        a_list1 = li_list1[num2].find_element(By.XPATH, "a")
        a_list1.click()
        logTest.log("点击选中的标签")
        time.sleep(3)
        search_bot = self.driver.find_element(By.CLASS_NAME, "search-bot")
        search_bot.click()
        logTest.log("点击搜索标签的内容")


if __name__ == "__main__":
    unittest.main(verbosity=2)
