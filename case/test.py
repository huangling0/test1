# # !/user/bin/env python
# # -*-coding:gbk-*-
# # author：mlh
#
# import unittest
# from selenium.webdriver.common.by import By
# from common import login, securities, companyInfo, financial_data
# from log import logTest
# import random
# from init import InitTest
# import time
#
#
# def nav(self):
# 	'''获取左侧指标'''
# 	div_nav = self.driver.find_element(By.CLASS_NAME, "nav-add-notice")
# 	ul_nav = div_nav.find_element(By.XPATH, "ul")
# 	li_nav = ul_nav.find_elements(By.XPATH, "li")
# 	num = 2
# 	li_nav[num].click()
# 	a = li_nav[num].find_element(By.XPATH, "a")
# 	time.sleep(5)
# 	global index_nav
# 	index_nav = li_nav[num].text
# 	logTest.log(a.get_attribute("textContent"))
#
#
# def cont(self):
# 	'''右侧指标'''
# 	# div_cont = self.driver.find_element(By.CLASS_NAME, "r-cont")
# 	# ul_cont = div_cont.find_element(By.XPATH, "ul")
# 	# li_cont = ul_cont.find_elements(By.XPATH, "li")
# 	# num = random.randint(0, len(li_cont)-1)
# 	# a = li_cont[num].find_element(By.XPATH, "a")
# 	# a.click()
# 	# global index_cont
# 	# index_cont = a.text
# 	# logTest.log(a.get_attribute("textContent"))
# 	lis_a = self.driver.find_elements(By.CSS_SELECTOR, ".select")
# 	global num
# 	num = random.randint(0, len(lis_a)-1)
# 	print("num=:", num)
# 	global index_cont
# 	index_cont = lis_a[num].get_attribute("textContent")
# 	lis_a[num].click()
# 	logTest.log(index_cont)
#
#
# def inp(self, keys):
# 	'''输入'''
# 	w_search = self.driver.find_element(By.CSS_SELECTOR, ".w-search.a1")
# 	w_search.send_keys(keys)
#
#
# def date(self):
# 	'''日期'''
# 	div_cont = self.driver.find_element(By.CLASS_NAME, "r-cont")
# 	ul_cont = div_cont.find_element(By.XPATH, "ul")
# 	li_cont = ul_cont.find_elements(By.XPATH, "li")
# 	num = random.randint(0, len(li_cont) - 2)
# 	a = li_cont[num].find_element(By.XPATH, "a")
# 	a.click()
# 	logTest.log(a.get_attribute("textContent"))
#
#
# def a_company(self):
# 	'''标签为公司'''
# 	cont(self)
# 	time.sleep(5)
# 	if index_cont == "基本信息":
# 		cont(self)
# 		time.sleep(5)
# 		if index_cont == "公司名称":
# 			company_a = companyInfo.AcompanyInfo(1)
# 			inp(self, company_a)
# 		elif index_cont == "证券简称":
# 			a_securities = companyInfo.AcompanyInfo(2)
# 			inp(self, a_securities)
# 		elif index_cont == "地区":
# 			cont(self)
# 			btn1 = self.driver.find_elements(By.CSS_SELECTOR, ".new-built.right")
# 			btn1[1].click()
# 		elif index_cont == "注册资本":
# 			a_finical = companyInfo.AcompanyInfo(6)
# 			inp(self, a_finical)
# 		elif index_cont == "注册地址":
# 			a_local = companyInfo.AcompanyInfo(4)
# 			inp(self, a_local)
# 		elif index_cont == "市值":
# 			a_shizhi = companyInfo.AcompanyInfo(7)
# 			inp(self, a_shizhi)
# 		elif index_cont == "市盈率":
# 			a_shiyinglv = companyInfo.AcompanyInfo(8)
# 			inp(self, a_shiyinglv)
# 		elif index_cont == "股票代码":
# 			a_code = companyInfo.AcompanyInfo(3)
# 			inp(self, a_code)
# 		elif index_cont == "主营业务":
# 			a_hangye = companyInfo.AcompanyInfo(5)
# 			inp(self, a_hangye)
# 		elif index_cont == "公司类型":
# 			cont(self)
# 			btn1 = self.driver.find_elements(By.CSS_SELECTOR, ".new-built.right")
# 			btn1[1].click()
# 		elif index_cont == "行业类型":
# 			cont(self)
# 			time.sleep(5)
# 			cont(self)
# 			btn1 = self.driver.find_elements(By.CSS_SELECTOR, ".new-built.right")
# 			btn1[1].click()
# 		elif index_cont == "全场质押比例":
# 			a_zhiya = companyInfo.AcompanyInfo(9)
# 			inp(self, a_zhiya)
# 		else:
# 			pass
# 	else:
# 		cont(self)
# 		i = num
# 		print("i=:", i)
# 		time.sleep(10)
# 		cont(self)
# 		j = num
# 		print("j=：", j)
# 		time.sleep(5)
# 		data = financial_data.financial(i+1, j+1)
# 		print("data=", data)
# 		inp(self, data)
#
#
# class advsearch(InitTest):
# 	'''测试深度搜索'''
#
# 	def test_001_advsearch(self):
# 		'''登陆'''
# 		self.driver.get("http://ibdata.cn/#!/advsearch")
# 		self.driver.find_element(By.CLASS_NAME, "head-img").click()
# 		login.login(self)
# 		logTest.log("登陆成功")
#
# 	def test_006_advsearch(self):
# 		'''A股'''
# 		logTest.log("开始测试A股：")
# 		div_a = self.driver.find_element(By.CLASS_NAME, "block")
# 		a = div_a.find_element(By.XPATH, "a")
# 		a.click()
# 		logTest.log(a.text)
# 		self.driver.switch_to.default_content()
# 		nav(self)
# 		if index_nav == "搜索范围":
# 			cont(self)
# 			time.sleep(5)
# 			if index_cont == "章节":
# 				cont(self)
# 				inp(self, "主营业务")
# 			else:
# 				inp(self, "主营业务")
# 		elif index_nav == "公司":
# 			a_company(self)
# 		elif index_nav == "发布日期":
# 			date(self)
# 		elif index_nav == "证券组合":
# 			cont(self)
# 		else:
# 			cont(self)
# 			time.sleep(5)
# 			button = self.driver.find_elements(By.CSS_SELECTOR, ".new-built.right")
# 			button[1].click()
#
# 		time.sleep(5)
# 		# clear(self)  # 清除
# 		# time.sleep(5)
# 		btn1 = self.driver.find_element(By.CSS_SELECTOR, ".one1.right20")
# 		btn1.click()
# 		time.sleep(62)
# 		try:
# 			self.driver.switch_to.default_content()
# 			btn_del = self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-del.right30")
# 			btn_del.click()
# 			logTest.log("很抱歉，请求超时请重新搜索")
# 		except:
# 			logTest.log("successful")
# 		logTest.log("A股测试结束")
#
#
# if __name__ == "__main__":
# 	unittest.main(verbosity=2)
#


import random
print(random.randint(0, 3))
