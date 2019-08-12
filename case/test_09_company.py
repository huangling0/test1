# !/user/bin/env python
# -*- coding:utf-8 -*-
# author：mlh

import unittest
from selenium.webdriver.common.by import By
import time
import random
from init import InitTest
from common import login, page
from log import logTest
from common import code


def error(self):
	''' internal error'''
	try:
		self.driver.switch_to.default_content()
		t = self.driver.find_element(By.CLASS_NAME, "t")
		logTest.log(t.text)
		btn_del = self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-del.right30")
		btn_del.click()

	except:
		logTest.log("successful")


def sort(self):
	'''排序'''

	self.driver.find_element(By.CLASS_NAME, "icofont-caret-default")
	up = self.driver.find_elements(By.CLASS_NAME, "icofont-caret-up")
	for i in range(1, len(up)):
		up[i].click()
		time.sleep(5)
		logTest.log("升序排列")
	down = self.driver.find_elements(By.CLASS_NAME, "icofont-caret-down")
	for j in range(len(down)):
		down[j].click()
		time.sleep(5)
		logTest.log("倒序排列")


def ctime(self):
	'''选择时间'''
	down_btn = self.driver.find_element(By.CLASS_NAME, "dropdown-btn")
	down_btn.click()
	time_ul = self.driver.find_element(By.CSS_SELECTOR, ".dropdown-menu.lanmu")
	time_li = time_ul.find_elements(By.XPATH, "li")
	num = random.randint(0, len(time_li)-2)
	time_a = time_li[num].find_element(By.XPATH, "a")
	time_a.click()


def c_alter_1(self):
	'''财务指标按报告期和年度的切换'''
	ul = self.driver.find_element(By.CLASS_NAME, "personnel")
	li = ul.find_elements(By.XPATH, "li")
	li[1].click()
	time.sleep(5)


def c_alter_2(self):
	'''具体财务指标的点击'''
	li_a = self.driver.find_elements(By.CLASS_NAME, "blue")
	num1 = random.randint(0, len(li_a)-1)
	num2 = random.randint(0, len(li_a)-1)
	li_a[num1].click()
	time.sleep(5)
	li_a[num2].click()
	time.sleep(5)


def comparable(self):
	'''添加可比公司'''
	logTest.log("准备添加可比公司：")
	cp_input = self.driver.find_element(By.CLASS_NAME, "cp-comparison-input")
	# comp_list = ["00", "600", "300", "002", "200", "900", "87", "43", "83"]
	# num = random.randint(0, len(comp_list) - 1)
	# cp_input.send_keys(comp_list[num])
	keys = code.Acode()
	cp_input.send_keys(keys)
	time.sleep(5)
	ul = self.driver.find_element_by_class_name("company-menu")
	li = ul.find_element_by_xpath("li")
	time.sleep(3)
	li.click()
	logTest.log("已经添加可比公司")
	time.sleep(10)
	c_alter_2(self)


def regular(self):
	'''定期报告'''
	try:
		dropdown = self.driver.find_element(By.CLASS_NAME, "dropdown-btn")
		dropdown.click()
		time.sleep(5)
		ul = self.driver.find_element(By.CSS_SELECTOR, ".dropdown-menu.lanmu")
		li = ul.find_elements(By.XPATH, "li")
		num = random.randint(1, len(li) - 1)
		a = li[num].find_element(By.XPATH, "a")
		a.click()
		time.sleep(5)
		logTest.log(a.text)
	except:
		logTest.log("没有定期报告")


class Company(InitTest):
	'''测试公司信息页面'''

	def test_001_company(self):
		'''登陆跳转'''
		company_code = code.Acode()
		self.driver.get("http://ibdata.cn/#!/company/?code={}&stype=1".format(company_code))
		time.sleep(30)
		self.driver.switch_to.default_content()
		btn_del = self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-del.right30")
		btn_del.click()
		time.sleep(5)
		login.login(self)
		time.sleep(60)
		logTest.log("登陆成功且成功跳转")

	def test_002_company(self):
		'''高管'''
		text1 = self.driver.find_element(By.LINK_TEXT, "高管")
		logTest.log(text1.text)
		text1.click()
		time.sleep(60)
		error(self)
		try:
			a = self.driver.find_elements(By.CLASS_NAME, "Navy-Blue")
			num = random.randint(0, len(a) - 1)
			if len(a) == 1:
				logTest.log("只有一个")
			else:
				a[num].click()
				time.sleep(5)
				logTest.log(a[num].text)
				logTest.log("查看相关公告")

		except Exception as e:
			logTest.log(e)
			logTest.log("可能没有相关公告")

	def test_003_company(self):
		'''机构持仓'''
		text2 = self.driver.find_element(By.LINK_TEXT, "机构持仓")
		logTest.log(text2.text)
		text2.click()
		time.sleep(62)
		error(self)

	def test_004_company(self):
		'''十大股东'''
		text3 = self.driver.find_element(By.LINK_TEXT, "十大股东")
		text3.click()
		time.sleep(60)
		logTest.log(text3.text)
		error(self)
		try:
			sort(self)
			page.page(self)
			self.driver.find_element(By.CLASS_NAME, "dropdown-btn-wrap").click()
			time.sleep(3)
			logTest.log("选择具体的定期报告")
			history_ul = self.driver.find_element(By.CSS_SELECTOR, ".dropdown-menu.mydropdown.lanmu")
			history_li = history_ul.find_elements(By.XPATH, "li")
			his_num = random.randint(0, len(history_li)-1)
			history_a = history_li[his_num].find_element(By.XPATH, "a")
			history_a.click()
			time.sleep(4)
			logTest.log(history_a.text)
		except:
			logTest.log("没有股东历史")

	def test_005_company(self):
		'''重要股东股权变动'''
		text4 = self.driver.find_element(By.LINK_TEXT, "重要股东股权变动")
		text4.click()
		time.sleep(62)
		logTest.log(text4.text)
		error(self)
		ctime(self)
		button = self.driver.find_element(By.CLASS_NAME, "search-bot")
		button.click()
		time.sleep(5)

	def test_006_company(self):
		'''公司综合能力指标'''
		text5 = self.driver.find_element(By.LINK_TEXT, "公司综合能力指标")
		logTest.log(text5.text)
		text5.click()
		time.sleep(62)
		error(self)
		# 指标切换
		c_alter_1(self)
		c_alter_2(self)
		# 可比公司
		comparable(self)

	def test_007_company(self):
		'''资产负债表'''
		text6 = self.driver.find_element(By.LINK_TEXT, "资产负债表")
		text6.click()
		time.sleep(62)
		logTest.log(text6.text)
		error(self)
		# 指标切换
		c_alter_1(self)
		c_alter_2(self)
		# 可比公司
		comparable(self)

	def test_008_company(self):
		'''利润表'''
		text7 = self.driver.find_element(By.LINK_TEXT, "利润表")
		text7.click()
		time.sleep(62)
		logTest.log(text7.text)
		error(self)
		# 指标切换
		c_alter_1(self)
		c_alter_2(self)
		# 可比公司
		comparable(self)

	def test_009_company(self):
		'''现金流量表'''
		text8 = self.driver.find_element(By.LINK_TEXT, "现金流量表")
		text8.click()
		time.sleep(62)
		logTest.log(text8.text)
		error(self)
		# 指标切换
		c_alter_1(self)
		c_alter_2(self)
		# 可比公司
		comparable(self)

	def test_010_company(self):
		'''业绩预告'''
		text9 = self.driver.find_element(By.LINK_TEXT, "业绩预告")
		text9.click()
		time.sleep(62)
		logTest.log(text9.text)
		error(self)
		try:
			el_box = self.driver.find_element(By.CSS_SELECTOR, ".el-checkbox.mar")
			el_box.click()
			time.sleep(5)
			logTest.log(el_box.text)
		except:
			logTest.log("没有业绩快报")
		sort(self)

	def test_011_company(self):
		'''行业对比'''
		text10 = self.driver.find_element(By.LINK_TEXT, "行业对比")
		text10.click()
		time.sleep(62)
		logTest.log(text10.text)
		error(self)
		sort = self.driver.find_elements(By.CSS_SELECTOR, ".blue-bg.center.can-click-th")
		sort[0].click()
		time.sleep(5)
		sort[1].click()
		time.sleep(5)
		self.driver.find_element(By.LINK_TEXT, "成长性比较").click()
		time.sleep(60)
		self.driver.find_element(By.LINK_TEXT, "净利润增长率(%)").click()
		time.sleep(10)
		self.driver.find_element(By.LINK_TEXT, "盈利比较").click()
		time.sleep(60)
		self.driver.find_element(By.LINK_TEXT, "每股收益").click()
		time.sleep(10)
		self.driver.find_element(By.LINK_TEXT, "资产比较").click()
		time.sleep(60)
		self.driver.find_element(By.LINK_TEXT, "资产负债率(%)").click()
		time.sleep(10)
		self.driver.find_element(By.LINK_TEXT, "现金比较").click()
		time.sleep(60)
		self.driver.find_element(By.LINK_TEXT, "每股现金流净值").click()
		time.sleep(10)

	def test_012_company(self):
		'''公司大事'''
		text11 = self.driver.find_element(By.LINK_TEXT, "公司大事")
		text11.click()
		time.sleep(62)
		logTest.log(text11.text)
		error(self)

	def test_013_company(self):
		'''按产品'''
		text12 = self.driver.find_element(By.LINK_TEXT, "按产品")
		text12.click()
		time.sleep(62)
		logTest.log(text12.text)
		error(self)
		regular(self)

	def test_014_company(self):
		'''按行业'''
		text13 = self.driver.find_element(By.LINK_TEXT, "按行业")
		text13.click()
		time.sleep(62)
		logTest.log(text13.text)
		error(self)
		regular(self)

	def test_015_company(self):
		'''按地域'''
		text14 = self.driver.find_element(By.LINK_TEXT, "按地域")
		text14.click()
		time.sleep(62)
		logTest.log(text14.text)
		error(self)
		regular(self)

	def test_016_company(self):
		'''客户信息'''
		text15 = self.driver.find_element(By.LINK_TEXT, "客户信息")
		text15.click()
		time.sleep(62)
		logTest.log(text15.text)
		error(self)
		regular(self)

	def test_017_company(self):
		'''供应商信息'''
		text16 = self.driver.find_element(By.LINK_TEXT, "供应商信息")
		text16.click()
		time.sleep(62)
		logTest.log(text16.text)
		error(self)
		regular(self)

	def test_018_company(self):
		'''交易行情'''
		text17 = self.driver.find_element(By.LINK_TEXT, "交易行情")
		text17.click()
		time.sleep(62)
		logTest.log(text17.text)
		error(self)
		ctime(self)
		# 表格
		self.driver.find_element(By.LINK_TEXT, "表格").click()
		time.sleep(15)
		# 下载
		load = self.driver.find_element(By.CSS_SELECTOR, ".Data-search-icon.icon-download")
		load.click()
		logTest.log("下载对应的股价信息")

	def test_019_company(self):
		'''龙虎榜'''
		text18 = self.driver.find_element(By.LINK_TEXT, "龙虎榜")
		text18.click()
		time.sleep(60)
		logTest.log(text18.text)
		sort(self)
		try:
			center = self.driver.find_elements(By.CLASS_NAME, "mm-top-five-btn")
			num = random.randint(0, len(center)-1)
			center[num].click()
			time.sleep(60)
			logTest.log(center[num].text)
		except:
			logTest.log("龙虎榜的内容为空")

	def test_020_company(self):
		'''大宗交易'''
		text19 = self.driver.find_element(By.LINK_TEXT, "大宗交易")
		text19.click()
		time.sleep(60)
		logTest.log(text19.text)
		sort(self)
		ctime(self)
		page.page(self)

	def test_021_company(self):
		'''行政许可'''
		text20 = self.driver.find_element(By.LINK_TEXT, "行政许可")
		text20.click()
		time.sleep(60)
		logTest.log(text20.text)
		error(self)

	def test_022_company(self):
		'''输入框'''
		so = self.driver.find_element(By.CSS_SELECTOR, ".ep-input")
		keys = code.N3Bcode()
		logTest.log("新三板的公司代码：")
		logTest.log(keys)
		so.send_keys(keys)
		time.sleep(5)
		btn = self.driver.find_element(By.CSS_SELECTOR, ".btn-search")
		btn.click()
		time.sleep(60)
		logTest.log("测试新三板的公司信息")


if __name__ == "__main__":
	unittest.main(verbosity=2)
