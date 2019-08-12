# !/user/bin/env python
# -*-  coding:utf-8  -*-
# author：mlh


import unittest
from selenium.webdriver.common.by import By
from common import login, securities, companyInfo, financial_data, content
from log import logTest
import random
from init import InitTest
import time
from selenium.webdriver.common.action_chains import ActionChains


def nav(self):
	'''获取左侧指标'''
	div_nav = self.driver.find_element(By.CLASS_NAME, "nav-add-notice")
	ul_nav = div_nav.find_element(By.XPATH, "ul")
	li_nav = ul_nav.find_elements(By.XPATH, "li")
	num = random.randint(0, len(li_nav) - 1)
	li_nav[num].click()
	a = li_nav[num].find_element(By.XPATH, "a")
	time.sleep(5)
	global index_nav
	index_nav = li_nav[num].text
	logTest.log(a.get_attribute("textContent"))


def cont(self):
	'''右侧指标'''
	# div_cont = self.driver.find_element(By.CLASS_NAME, "r-cont")
	# ul_cont = div_cont.find_element(By.XPATH, "ul")
	# li_cont = ul_cont.find_elements(By.XPATH, "li")
	# num = random.randint(0, len(li_cont)-1)
	# a = li_cont[num].find_element(By.XPATH, "a")
	# a.click()
	# global index_cont
	# index_cont = a.text
	# logTest.log(a.get_attribute("textContent"))
	lis_a = self.driver.find_elements(By.CSS_SELECTOR, ".select")
	global num
	num = random.randint(0, len(lis_a) - 1)
	print("num=:", num)
	global index_cont
	index_cont = lis_a[num].get_attribute("textContent")
	lis_a[num].click()
	logTest.log(index_cont)


def inp(self, keys):
	'''输入'''
	w_search = self.driver.find_element(By.CSS_SELECTOR, ".w-search.a1")
	w_search.send_keys(keys)


def date(self):
	'''日期'''
	div_cont = self.driver.find_element(By.CLASS_NAME, "r-cont")
	ul_cont = div_cont.find_element(By.XPATH, "ul")
	li_cont = ul_cont.find_elements(By.XPATH, "li")
	num = random.randint(0, len(li_cont) - 2)
	a = li_cont[num].find_element(By.XPATH, "a")
	logTest.log(a.get_attribute("textContent"))
	a.click()


def a_company(self):
	'''A股：标签为公司'''
	cont(self)
	time.sleep(5)
	if index_cont == "基本信息":
		cont(self)
		time.sleep(5)
		if index_cont == "公司名称":
			company_a = companyInfo.AcompanyInfo(1)
			logTest.log(company_a)
			inp(self, company_a)
		elif index_cont == "证券简称":
			a_securities = companyInfo.AcompanyInfo(2)
			logTest.log(a_securities)
			inp(self, a_securities)
		elif index_cont == "地区":
			cont(self)
			btn1 = self.driver.find_elements(By.CSS_SELECTOR, ".new-built.right")
			btn1[1].click()
		elif index_cont == "注册资本":
			a_finical = companyInfo.AcompanyInfo(6)
			logTest.log(a_finical)
			inp(self, a_finical)
		elif index_cont == "注册地址":
			a_local = companyInfo.AcompanyInfo(4)
			logTest.log(a_local)
			inp(self, a_local)
		elif index_cont == "市值":
			a_shizhi = companyInfo.AcompanyInfo(7)
			logTest.log(a_shizhi)
			inp(self, a_shizhi)
		elif index_cont == "市盈率":
			a_shiyinglv = companyInfo.AcompanyInfo(8)
			logTest.log(a_shiyinglv)
			inp(self, a_shiyinglv)
		elif index_cont == "股票代码":
			a_code = companyInfo.AcompanyInfo(3)
			logTest.log(a_code)
			inp(self, a_code)
		elif index_cont == "主营业务":
			a_hangye = companyInfo.AcompanyInfo(5)
			logTest.log(a_hangye)
			inp(self, a_hangye)
		elif index_cont == "公司类型":
			cont(self)
			btn1 = self.driver.find_elements(By.CSS_SELECTOR, ".new-built.right")
			btn1[1].click()
		elif index_cont == "行业类型":
			cont(self)
			time.sleep(5)
			cont(self)
			btn1 = self.driver.find_elements(By.CSS_SELECTOR, ".new-built.right")
			btn1[1].click()
		elif index_cont == "全场质押比例":
			a_zhiya = companyInfo.AcompanyInfo(9)
			logTest.log(a_zhiya)
			inp(self, a_zhiya)
		else:
			pass
	else:
		cont(self)
		i = num
		print("i=:", i)
		time.sleep(10)
		cont(self)
		j = num
		print("j=：", j)
		time.sleep(5)
		data = financial_data.financial(i+1, j+1)
		print("data=", data)
		inp(self, data)


def n3b_company(self):
	'''新三板：标签为公司'''
	cont(self)
	time.sleep(5)
	if index_cont == "基本信息":
		cont(self)
		time.sleep(5)
		if index_cont == "公司名称":
			company_n3b = companyInfo.N3BCompanyInfo(1)
			logTest.log(company_n3b)
			inp(self, company_n3b)
		elif index_cont == "证券简称":
			n3b_securities = companyInfo.N3BCompanyInfo(2)
			logTest.log(n3b_securities)
			inp(self, n3b_securities)
		elif index_cont == "地区":
			cont(self)
			btn1 = self.driver.find_elements(By.CSS_SELECTOR, ".new-built.right")
			btn1[1].click()
		elif index_cont == "注册地址":
			n3b_local = companyInfo.N3BCompanyInfo(4)
			logTest.log(n3b_local)
			inp(self, n3b_local)
		elif index_cont == "注册资本":
			n3b_login = companyInfo.N3BCompanyInfo(6)
			logTest.log(n3b_login)
			inp(self, n3b_login)
		elif index_cont == "股票代码":
			n3b_code = companyInfo.N3BCompanyInfo(3)
			logTest.log(n3b_code)
			inp(self, n3b_code)
		elif index_cont == "主营业务":
			n3b_product = companyInfo.N3BCompanyInfo(5)
			logTest.log(n3b_product)
			inp(self, n3b_product)
		elif index_cont == "行业类型":
			cont(self)
			time.sleep(5)
			cont(self)
			btn1 = self.driver.find_elements(By.CSS_SELECTOR, ".new-built.right")
			btn1[1].click()
		else:
			pass
	else:
		cont(self)
		i = num
		time.sleep(5)
		cont(self)
		j = num
		time.sleep(5)
		data = financial_data.financial(i+1, j+1)
		inp(self, data)


def h_company(self):
	'''港股：标签为公司'''
	cont(self)
	time.sleep(5)
	if index_cont == "基本信息":
		cont(self)
		time.sleep(5)
		if index_cont == "公司名称":
			company_hk = companyInfo.HKcompanyInfo(1)
			logTest.log(company_hk)
			inp(self, company_hk)

		elif index_cont == "注册地址":
			hk_local = companyInfo.HKcompanyInfo(4)
			logTest.log(hk_local)
			inp(self, hk_local)

		elif index_cont == "股票代码":
			hk_code = companyInfo.HKcompanyInfo(3)
			logTest.log(hk_code)
			inp(self, hk_code)

		elif index_cont == "行业类型":
			cont(self)
			time.sleep(5)
			cont(self)
			btn1 = self.driver.find_elements(By.CSS_SELECTOR, ".new-built.right")
			btn1[1].click()
		else:
			pass
	else:
		cont(self)
		i = num
		time.sleep(5)
		cont(self)
		j = num
		time.sleep(5)
		data = financial_data.hkfinancial(i+2, j+1)
		logTest.log(data)
		inp(self, data)


def label(self, n):
	'''A股、N3B、H股、债券、研报的获取'''
	'''
	A股：n=0
	N3B：n=1
	债券：n=2
	研报：n=3
	H股：n=4
	'''
	fz1 = self.driver.find_element(By.CLASS_NAME, "fz1")
	fz1.click()
	fz2 = self.driver.find_element(By.CLASS_NAME, "fz2")
	ul = fz2.find_element(By.XPATH, "ul")
	li = ul.find_elements(By.XPATH, "li")
	logTest.log(li[n].text)
	a = li[n].find_element(By.XPATH, "a")
	logTest.log(a.text)
	a.click()
	logTest.log(a.get_attribute("textContent"))
	time.sleep(5)


def add_tra(self):
	'''点击增加条件'''
	div_a = self.driver.find_element(By.CLASS_NAME, "block")
	a = div_a.find_element(By.XPATH, "a")
	logTest.log(a.text)
	a.click()
	time.sleep(5)


def clear(self):
	'''清空条件'''
	cls = self.driver.find_element(By.CSS_SELECTOR, ".one2.right20")
	cls.click()


def result_analyze(self):
	'''搜索结果和分析的切换'''
	res1_div = self.driver.find_element(By.CLASS_NAME, "menu-result")
	res1_ul = res1_div.find_element(By.XPATH, "ul")
	res1_li = res1_ul.find_elements(By.XPATH, "li")
	logTest.log("搜索结果和分析的切换")
	res1_li[1].click()
	time.sleep(5)
	logTest.log("分析和搜索结果的切换")
	res1_li[0].click()
	time.sleep(30)


def result_title(self):
	'''点击选中只看标题'''

	res2 = self.driver.find_element(By.CLASS_NAME, "menu-result")
	self.driver.execute_script("arguments[0].scrollIntoView();", res2)
	logTest.log("下拉至当前元素所在位置处")
	check_all = res2.find_elements(By.XPATH, "div")[0]
	lab = check_all.find_elements(By.XPATH, "label")
	title = lab[0].find_element(By.CLASS_NAME, "el-checkbox-inner")
	title.click()
	time.sleep(5)
	# 全选
	selectall = lab[1].find_element(By.CLASS_NAME, "el-checkbox-inner")
	logTest.log("全选")
	selectall.click()
	time.sleep(5)
	# 下载
	# try:
# 	# 	load = self.driver.find_elements(By.CLASS_NAME, "search-down")
# 	# 	n = random.randint(0, 1)
# 	# 	logTest.log("下载")
# 	# 	load[n].click()
# 	# except:
# 	# 	logTest.log("搜索结果为空")


def wechat_share(self):
	'''微信分享'''
	wechat = self.driver.find_element(By.CLASS_NAME, "Share-results-search Share-new")
	self.driver.execute_script("arguments[0].scrollIntoView();", wechat)
	logTest.log("下拉至当前元素所在位置处")
	wechat.click()
	time.sleep(5)
	self.driver.switch_to.default_content()
	inp = self.driver.find_element(By.CLASS_NAME, "input-describe")
	inp.send_keys("分享搜索结果")
	time.sleep(3)
	btn = self.driver.find_element(By.CLASS_NAME, "search-describe")
	btn.click()
	time.sleep(5)
	ActionChains(self.driver).move_by_offset(0, 0).click().perform()
	time.sleep(5)
	logTest.log("微信分享成功")


def result_sort(self):
	'''排序'''
	dropdown = self.driver.find_element(By.CLASS_NAME, "dropdown-icon")
	self.driver.execute_script("arguments[0].scrollIntoView();", dropdown)
	logTest.log("下拉至当前元素所在位置处")
	logTest.log("点击排序")
	dropdown.click()
	time.sleep(5)
	menu = self.driver.find_element(By.CLASS_NAME, "dropdown-menu")
	menu_li = menu.find_elements(By.XPATH, "li")
	n = random.randint(0, 1)
	menu_li[n].click()
	logTest.log("排序")
	time.sleep(60)


def result_load(self):
	'''搜索结果的下载'''
	try:
		load = self.driver.find_element(By.CSS_SELECTOR, ".serch-l.green.advDow_0")
		self.driver.execute_script("arguments[0].scrollIntoView();", load)
		logTest.log("下拉至当前元素所在位置处")
		logTest.log(load)
		load.click()
	except:
		logTest.log("没有搜索结果")


def result_collection(self):
	'''收藏'''

	logTest.log("准备收藏公告：")
	collection = self.driver.find_elements(By.CSS_SELECTOR, ".search-icon.small-collect-n")
	n = random.randint(0, len(collection)-1)
	self.driver.execute_script("arguments[0].scrollIntoView();", collection[n])
	logTest.log("下拉至当前元素所在位置处")
	collection[n].click()
	time.sleep(5)
	self.driver.switch_to.default_content()
	btn_group = self.driver.find_element(By.CSS_SELECTOR, ".tag-choice-list.btn-group")
	btn_group.click()
	time.sleep(5)
	collect_menu = self.driver.find_elements(By.CSS_SELECTOR, ".dropdown-menu.lanmu.mydropdown")
	collect_li = collect_menu[1].find_elements(By.XPATH, "li")
	n2 = random.randint(0, len(collect_li) - 2)
	span = collect_li[n2].find_element(By.XPATH, "span")
	span.click()
	time.sleep(5)
	btn_add = self.driver.find_element(By.CLASS_NAME, "btn-add")
	btn_add.click()
	time.sleep(5)

	try:
		btn_del = self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-del.right30")
		btn_del.click()
		logTest.log("收藏成功")
	except:
		pass


class advsearch(InitTest):
	'''测试深度搜索'''

	def test_001_advsearch(self):
		'''登陆'''
		self.driver.get("http://ibdata.cn/#!/advsearch")
		self.driver.find_element(By.CLASS_NAME, "head-img").click()
		login.login(self)
		logTest.log("登陆成功")

	def test_003_advsearch(self):
		'''公司和公告的切换'''
		alter = self.driver.find_elements(By.CLASS_NAME, "cond")[0]
		lis = alter.find_elements(By.XPATH, "li")
		for i in range(len(lis)):
			lis[i].click()
			time.sleep(5)
			logTest.log(lis[i].text)
		lis[0].click()

	def test_002_advsearch(self):
		'''范例说明'''
		eg = self.driver.find_element(By.CSS_SELECTOR, ".left.right20")
		eg.click()
		logTest.log(eg.text)
		time.sleep(60)

	def test_004_advsearch(self):
		'''简单的搜索'''
		global fz1
		fz1 = self.driver.find_element(By.CLASS_NAME, "fz1")
		fz1.click()
		time.sleep(3)
		global fz2
		fz2 = self.driver.find_element(By.CLASS_NAME, "fz2")
		ul_list = fz2.find_element(By.XPATH, "ul")
		li_list = ul_list.find_elements(By.XPATH, "li")
		for i in range(len(li_list)):
			a = li_list[i].find_element(By.XPATH, "a")
			a.click()
			time.sleep(2)
			logTest.log(a.text)
			global btn
			btn = self.driver.find_element(By.CLASS_NAME, "one1")
			btn.click()
			time.sleep(60)
			logTest.log("搜索结果")

			fz1 = self.driver.find_element(By.CLASS_NAME, "fz1")
			fz1.click()

	def test_005_advsearch(self):
		'''范例和我的标签搜索'''
		tag_button = self.driver.find_element(By.CLASS_NAME, "tag-button")
		my_tags = tag_button.find_element(By.XPATH, "div")
		ul = my_tags.find_element(By.XPATH, "ul")
		li = ul.find_elements(By.XPATH, "li")
		for i in range(len(li)):
			li[i].click()
			time.sleep(3)
			logTest.log(li[i].text)
			if li[i].text == "范例":
				div_1 = self.driver.find_element(By.CLASS_NAME, "tags-notice-a")
				ul_1 = div_1.find_element(By.XPATH, "ul")
				li_1 = ul_1.find_elements(By.XPATH, "li")
				num_1 = random.randint(0, len(li_1)-1)
				li_1[num_1].click()
				time.sleep(62)
				logTest.log(li_1[num_1].text)

			else:
				div_2 = self.driver.find_element(By.CLASS_NAME, "tags-notice-b")
				ul_2 = div_2.find_element(By.XPATH, "ul")
				li_2 = ul_2.find_elements(By.XPATH, "li")
				num_2 = random.randint(0, len(li_2) - 1)
				li_2[num_2].click()
				time.sleep(62)
				logTest.log(li_2[num_2].text)

		clear(self)
		time.sleep(5)
		btn1 = self.driver.find_element(By.CSS_SELECTOR, ".one1.right20")
		btn1.click()
		time.sleep(61)
		try:
			self.driver.switch_to.default_content()
			btn_del = self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-del.right30")
			btn_del.click()
			logTest.log("很抱歉，请求超时请重新搜索")
		except:
			logTest.log("successful")

	def test_006_00advsearch(self):
		'''A股'''
		logTest.log("开始测试A股：")
		label(self, 0)
		div_a = self.driver.find_element(By.CLASS_NAME, "block")
		a = div_a.find_element(By.XPATH, "a")
		a.click()
		logTest.log(a.text)
		self.driver.switch_to.default_content()
		nav(self)
		if index_nav == "搜索范围":
			cont(self)
			time.sleep(5)
			if index_cont == "章节":
				cont(self)
				text = content.content()
				logTest.log(text)
				inp(self, text)
			else:
				text = content.content()
				logTest.log(text)
				inp(self, text)
		elif index_nav == "公司":
			a_company(self)
		elif index_nav == "发布日期":
			date(self)
		elif index_nav == "证券组合":
			cont(self)
		else:
			cont(self)
			time.sleep(5)
			button = self.driver.find_elements(By.CSS_SELECTOR, ".new-built.right")
			button[1].click()

		time.sleep(5)
		# clear(self)  # 清除
		# time.sleep(5)
		btn1 = self.driver.find_element(By.CSS_SELECTOR, ".one1.right20")
		btn1.click()
		time.sleep(62)
		try:
			self.driver.switch_to.default_content()
			btn_del = self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-del.right30")
			btn_del.click()
			logTest.log("很抱歉，请求超时请重新搜索")
		except:
			logTest.log("successful")
		logTest.log("A股搜索测试结束")

	def test_006_01load(self):
		# 下载
		logTest.log("搜索公告结果测试开始：")
		result_load(self)

	def test_006_02sort(self):
		# 排序
		result_sort(self)

	def test_006_03collection(self):
		# 收藏
		result_collection(self)

	def test_006_04analyze(self):
		# 切换到分析
		result_analyze(self)

	def test_006_05title(self):
		# 只看标题
		result_title(self)
		logTest.log("搜索结果测试结束。")

	def test_006_06company(self):
		'''搜索公司'''
		logTest.log("测试搜索公司结果开始：")
		# 点击切换到公司
		company_bg = self.driver.find_element(By.CLASS_NAME, "search_bg")
		company_list = company_bg.find_element(By.CSS_SELECTOR, ".cond.left.mar30")
		company_li = company_list.find_elements(By.XPATH, "li")
		logTest.log(company_li[1].text)
		company_li[1].click()
		# 点击搜索
		btn = self.driver.find_element(By.CSS_SELECTOR, ".one1.right20")
		btn.click()
		time.sleep(61)
		try:
			self.driver.switch_to.default_content()
			btn_del = self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-del.right30")
			btn_del.click()
			logTest.log("很抱歉，请求超时请重新搜索")
		except:
			logTest.log("successful")

	# def test_006_07company(self):
	# 	# 自定义
	# 	logTest.log("测试自定义")
	# 	qicon = self.driver.find_element(By.CSS_SELECTOR, ".qicon.ques_10.mar")
	# 	qicon.click()
	# 	time.sleep(5)
	# 	self.driver.switch_to.default_content()
	# 	import pdb
	# 	pdb.set_trace()
	# 	c2 = self.driver.find_elements(By.CLASS_NAME, "c2")
	# 	i = random.randint(0, len(c2)-1)
	# 	c2[i].cick()
	# 	btn = self.driver.find_element(By.CSS_SELECTOR, ".new-built.right")
	# 	btn.click()
	# 	time.sleep(5)
	# 	logTest.log("自定义测试结束")

	def test_006_08company(self):
		'''导出公司信息'''
		logTest.log("导出公司信息")
		export = self.driver.find_element(By.CSS_SELECTOR, ".catalog-icon.cata-f")
		export.click()
		time.sleep(5)
		dele = self.driver.find_elements(By.CSS_SELECTOR, ".btn.btn-del.right30")
		dele[0].click()
		logTest.log("已导出公司信息")
		time.sleep(61)

	def test_006_09company(self):
		'''公司信息排序'''
		logTest.log("开始排序：")
		try:
			up = self.driver.find_elements(By.CSS_SELECTOR, ".icofont-caret-up")
			n = random.randint(0, len(up)-1)
			up[n].click()
			logTest.log("正序排列")
			time.sleep(5)
			down = self.driver.find_elements(By.CSS_SELECTOR, ".icofont-caret-down")
			n2 = random.randint(0, len(down)-1)
			down[n2].click()
			time.sleep(5)
			logTest.log("倒序排列")
			logTest.log("成功排序")
		except:
			logTest.log("没有搜索结果")

	def test_006_10company(self):
		'''微信分享'''
		logTest.log("测试微信分享：")
		company_share = self.driver.find_element(By.CSS_SELECTOR, ".catalog-icon.cata-share")
		company_share.click()
		time.sleep(3)
		share_inp = self.driver.find_element(By.CSS_SELECTOR, ".input-describe")
		share_inp.send_keys("分享搜索的公司信息")
		time.sleep(5)
		btn = self.driver.find_element(By.CSS_SELECTOR, ".search-describe")
		btn.click()
		time.sleep(5)
		ActionChains(self.driver).move_by_offset(0, 0).click().perform()
		logTest.log("微信分享成功")

	def test_006_11company(self):
		'''区间分析'''
		logTest.log("测试区间分析：")
		mor = self.driver.find_element(By.CSS_SELECTOR, ".small-mor.small-mar")
		mor.click()
		time.sleep(5)
		mor_ul = self.driver.find_element(By.CSS_SELECTOR, ".dropdown-menu.lanmu")
		mor_li = mor_ul.find_elements(By.XPATH, "li")
		n = random.randint(0, len(mor_li)-1)
		mor_a = mor_li[n].find_element(By.XPATH, "a")
		logTest.log(mor_a.text)
		mor_a.click()
		time.sleep(5)
		logTest.log("区间分析测试结束")

	def test_006_12company(self):
		'''财务分析'''
		logTest.log("开始测试财务分析：")
		try:
			select = self.driver.find_elements(By.CSS_SELECTOR, ".el-checkbox-input.input-s")
			n = random.randint(0, len(select)-1)
			select[n].click()
			time.sleep(5)
			logTest.log("选中公司")
		except:
			logTest.log("没有公司")
		contrast_btn = self.driver.find_element(By.CSS_SELECTOR, ".company-contrast-btn")
		self.driver.execute_script("arguments[0].scrollIntoView();", contrast_btn)
		logTest.log("下拉至当前元素所在位置处")
		contrast_btn.click()
		time.sleep(5)
		global current_window
		current_window = self.driver.current_window_handle
		handles = self.driver.window_handles
		self.driver.switch_to.window(self.driver.window_handles[len(handles)-1])
		logTest.log("跳转至财务分析页面")
		time.sleep(60)

	def test_006_13company(self):
		'''财务分析页'''
		logTest.log("成功跳转至财务分析页面")
		logTest.log("测试按季度切换为按年度")
		year_ul = self.driver.find_element(By.CSS_SELECTOR, ".personnel")
		year_li = year_ul.find_elements(By.XPATH, "li")
		year_li[1].click()
		time.sleep(5)
		logTest.log("成功将季度切换为按年度")

	def test_006_14company(self):
		'''添加可比公司'''
		logTest.log("开始添加可比公司")
		company = companyInfo.AcompanyInfo(2)
		tags = self.driver.find_elements(By.CLASS_NAME, "tags-input")
		tags[0].send_keys(company)
		time.sleep(5)
		company_menu = self.driver.find_element(By.CLASS_NAME, "company-menu")
		company_li = company_menu.find_element(By.XPATH, "li")
		company_li.click()
		logTest.log("成功添加可比公司")

	def test_006_15company(self):
		'''添加财务指标'''
		logTest.log("开始添加财务指标")
		tags = self.driver.find_elements(By.CLASS_NAME, "tags-input")
		tags[1].click()
		time.sleep(5)
		lis = self.driver.find_elements(By.CLASS_NAME, "small-top")
		t = random.randint(0, len(lis)-1)
		lis[t].click()
		time.sleep(5)
		index_ul = self.driver.find_element(By.CLASS_NAME, "justforshow")
		index_li = index_ul.find_elements(By.XPATH, "li")
		n = random.randint(0, len(index_li)-1)
		index_a = index_li[n].find_element(By.XPATH, "a")
		index_a.click()
		time.sleep(5)
		logTest.log("成功添加财务指标")

	def test_006_16company(self):
		'''指标切换'''
		logTest.log("开始测试指标切换")
		alter_index = self.driver.find_element(By.CSS_SELECTOR, ".small-mor.small-mar")
		alter_index.click()
		time.sleep(5)
		alter_ul = self.driver.find_element(By.CSS_SELECTOR, ".dropdown-menu.lanmu")
		alter_li = alter_ul.find_elements(By.XPATH, "li")
		index = random.randint(0, len(alter_li)-1)
		index_a = alter_li[index].find_element(By.XPATH, "a")
		index_a.click()
		time.sleep(5)
		logTest.log("指标切换成功")

	def test_006_17company(self):
		'''删除添加的可比公司'''
		logTest.log("开始测试删除添加的可比公司")
		del_div = self.driver.find_element(By.CLASS_NAME, "Switching-comparison")
		del_ul = del_div.find_element(By.XPATH, "ul")
		del_li = del_ul.find_elements(By.XPATH, "li")
		t = random.randint(0, len(del_li)-1)
		ActionChains(self.driver).move_to_element(del_li[t]).perform()
		time.sleep(3)
		del_delete = del_li[t].find_element(By.CLASS_NAME, "Switching-delete")
		del_delete.click()
		time.sleep(5)
		logTest.log("成功删除添加的可比公司")

	def test_006_18company(self):
		'''删除添加的财务指标'''
		logTest.log("开始测试删除添加的财务指标")
		del_index = self.driver.find_element(By.CLASS_NAME, "Switching-Event-cont")
		del_ul = del_index.find_element(By.XPATH, "ul")
		del_li = del_ul.find_elements(By.XPATH, "li")
		t = random.randint(0, len(del_li) - 1)
		ActionChains(self.driver).move_to_element(del_li[t]).perform()
		time.sleep(3)
		del_delete = del_li[t].find_element(By.CLASS_NAME, "Switching-delete")
		del_delete.click()
		time.sleep(5)
		logTest.log("成功删除添加的财务指标")

	def test_006_19company(self):
		'''页面跳转至搜索结果页'''
		logTest.log("开始测试页面跳转至搜索结果页")
		self.driver.close()
		self.driver.switch_to.window(current_window)
		time.sleep(15)
		logTest.log("成功测试页面跳转至搜索结果页")

	# def test_006_advsearch2(self):
	# 	# 	'''A股搜索结果的测试'''
	# 	# 	logTest.log("开始测试A股搜索结果：")

	def test_007_advsearch(self):
		'''测试N3B'''
		clear(self)
		time.sleep(5)
		# 点击切换到公告
		logTest.log("点击切换到公告")
		company_bg = self.driver.find_element(By.CLASS_NAME, "search_bg")
		company_list = company_bg.find_element(By.CSS_SELECTOR, ".cond.left.mar30")
		company_li = company_list.find_elements(By.XPATH, "li")
		logTest.log(company_li[1].text)
		company_li[0].click()
		time.sleep(3)
		logTest.log("成功点击切换到公告")
		label(self, 1)
		logTest.log("开始测试N3B：")
		add_tra(self)
		self.driver.switch_to.default_content()
		nav(self)
		if index_nav == "板块类型":
			cont(self)
			if index_cont == "挂牌公司":
				cont(self)

		elif index_nav == "搜索范围":
			cont(self)
			time.sleep(5)
			if index_cont == "章节":
				cont(self)
				time.sleep(3)
				text = content.content()
				logTest.log(text)
				inp(self, text)
			else:
				text = content.content()
				logTest.log(text)
				inp(self, text)
		elif index_nav == "公司":
			n3b_company(self)
		elif index_nav == "发布日期":
			date(self)
		elif index_nav == "证券组合":
			cont(self)
		else:
			cont(self)
			button = self.driver.find_elements(By.CSS_SELECTOR, ".new-built.right")
			button[1].click()

		time.sleep(5)
		btn1 = self.driver.find_element(By.CSS_SELECTOR, ".one1.right20")
		btn1.click()
		time.sleep(62)
		try:
			self.driver.switch_to.default_content()
			btn_del = self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-del.right30")
			btn_del.click()
			logTest.log("很抱歉，请求超时请重新搜索")
		except:
			logTest.log("successful")
		logTest.log("N3B测试结束")

	def test_008_advsearch(self):
		'''债券'''
		clear(self)
		time.sleep(5)
		label(self, 2)
		logTest.log("开始测试债券：")
		add_tra(self)
		self.driver.switch_to.default_content()
		nav(self)
		if index_nav == "搜索范围":
			cont(self)
			time.sleep(5)
			if index_cont == "章节":
				cont(self)
				keys = securities.Bondsecurities()
				logTest.log(keys)
				inp(self, keys)
			else:
				key = securities.Bondsecurities()
				logTest.log(key)
				inp(self, key)
		elif index_nav == "发布日期":
			date(self)
		elif index_nav == "证券组合":
			cont(self)
		else:
			cont(self)
			button = self.driver.find_elements(By.CSS_SELECTOR, ".new-built.right")
			button[1].click()

		time.sleep(5)
		btn1 = self.driver.find_element(By.CSS_SELECTOR, ".one1.right20")
		btn1.click()
		time.sleep(62)
		try:
			self.driver.switch_to.default_content()
			btn_del = self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-del.right30")
			btn_del.click()
			logTest.log("很抱歉，请求超时请重新搜索")
		except:
			logTest.log("successful")
		logTest.log("债券测试结束")

	def test_009_advsearch(self):
		'''研报'''
		clear(self)
		time.sleep(5)
		label(self, 3)
		logTest.log("开始测试研报：")
		add_tra(self)
		self.driver.switch_to.default_content()
		nav(self)
		if index_nav == "搜索范围":
			cont(self)
			time.sleep(5)
			if index_cont == "章节":
				cont(self)
				time.sleep(5)
				text = content.content()
				logTest.log(text)
				inp(self, text)
			else:
				text = content.content()
				logTest.log(text)
				inp(self, text)
		elif index_nav == "公司":
			a_company(self)
		elif index_nav == "发布日期":
			date(self)
		else:
			cont(self)

		time.sleep(5)
		btn1 = self.driver.find_element(By.CSS_SELECTOR, ".one1.right20")
		btn1.click()
		time.sleep(62)
		try:
			self.driver.switch_to.default_content()
			btn_del = self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-del.right30")
			btn_del.click()
			logTest.log("很抱歉，请求超时请重新搜索")
		except:
			logTest.log("successful")
		logTest.log("研报测试结束")

	def test_010_advsearch(self):
		'''H股'''
		clear(self)
		time.sleep(5)
		label(self, 4)
		logTest.log("开始测试H股：")
		add_tra(self)
		self.driver.switch_to.default_content()
		nav(self)
		if index_nav == "搜索范围":
			cont(self)
			time.sleep(5)
			if index_cont == "章节":
				cont(self)
				time.sleep(5)
				content = companyInfo.HKcompanyInfo(2)
				logTest.log(content)
				inp(self, content)
			else:
				content = companyInfo.HKcompanyInfo(2)
				logTest.log(content)
				inp(self, content)
		elif index_nav == "公司":
			h_company(self)
		elif index_nav == "发布日期":
			date(self)
		else:
			cont(self)

		time.sleep(5)
		btn1 = self.driver.find_element(By.CSS_SELECTOR, ".one1.right20")
		btn1.click()
		time.sleep(62)
		try:
			self.driver.switch_to.default_content()
			btn_del = self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-del.right30")
			btn_del.click()
			logTest.log("很抱歉，请求超时请重新搜索")
		except:
			logTest.log("successful")
		logTest.log("H股测试结束")


if __name__ == "__main__":
	unittest.main(verbosity=2)
