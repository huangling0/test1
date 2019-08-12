#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:mlh
# datetime:2019/5/16 上午10:03

import unittest
from init import InitTest
import xlrd
import time
from log import logTest


def readExcel(row):
    '''
       :param row:该参数表示行
       E:\\huangmeiling\\UI_IBDATA\\UI_IBDATA\\data\\login_data01.xlsx
       路径：E:\\huangmeiling\\UI_IBDATA\\UI_IBDATA\\data\\login_data01.xlsx
    '''

    # book = xlrd.open_workbook('E:\\huangmeiling\\UI_IBDATA\\UI_IBDATA\\data\\login_data01.xlsx')

    book = xlrd.open_workbook('..\\data\\login_data01.xlsx')

    table = book.sheet_by_index(0)
    # print(table.row_values(row))

    return table.row_values(row)


class LoginTest(InitTest):
    '''测试登录模块'''

    def login(self, username, password):
        '''登录帐号密码输入框'''

        self.driver.find_element_by_xpath("//*[@id='handle']").clear()
        self.driver.find_element_by_xpath("//*[@id='handle']").send_keys(username)
        time.sleep(2)
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys(password)
        time.sleep(2)
        self.driver.find_element_by_class_name("sign-button").click()
        time.sleep(2)

    def getloginError1(self):
        '''用户名为空的错误提示信息'''

        loginError = self.driver.find_elements_by_xpath("//span[@class='pt-error']")[0]
        return loginError.text

    def getloginError2(self):
        '''密码为空的错误信息'''
        loginError = self.driver.find_elements_by_xpath("//span[@class='pt-error']")[1]
        return loginError.text

    def getloginError3(self):
        '''用户名或者密码错误时的提示信息'''
        loginError = self.driver.find_element_by_class_name("agreement-wrong")
        return loginError.text

    def test_0001_login_null(self):
        '''用户名和密码为空'''
        logTest.log("测试用户名和密码为空")
        self.login(readExcel(1)[1], readExcel(1)[2])
        #
        self.assertEqual(self.getloginError1(), readExcel(1)[3])
        logTest.log("断言验证成功")

    def test_0002_login_userNull(self):
        '''用户名为空'''
        logTest.log("测试用户名为空")
        self.login(readExcel(3)[1], readExcel(3)[2])
        self.assertEqual(self.getloginError1(), readExcel(3)[3])
        logTest.log("断言验证成功")

    def test_0003_login_passnull(self):
        '''密码为空'''
        logTest.log("测试密码为空")
        self.login(str(int(readExcel(2)[1])), readExcel(2)[2])
        self.assertEqual(self.getloginError2(), readExcel(2)[3])
        logTest.log("断言验证成功")

    def test_0004_login_Error(self):
        '''用户名或者密码错误'''
        # logTest.log("测试用户名或者密码错误")
        self.login(str(int(readExcel(4)[1])), readExcel(4)[2])
        self.assertEqual(self.getloginError3(), readExcel(4)[3])
        logTest.log("断言验证成功")

    def test_0005_login_True(self):
        '''正常登录'''
        logTest.log("测试正常登录")
        self.login(str(int(readExcel(5)[1])), readExcel(5)[2])
        self.assertEqual(self.driver.current_url, readExcel(5)[3])
        logTest.log("正常登录断言验证成功")


if __name__ == "__main__":
    unittest.main(verbosity=2)



