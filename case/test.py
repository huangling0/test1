# # !/user/bin/env python
# # -*-coding:gbk-*-
# # author��mlh
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
# 	'''��ȡ���ָ��'''
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
# 	'''�Ҳ�ָ��'''
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
# 	'''����'''
# 	w_search = self.driver.find_element(By.CSS_SELECTOR, ".w-search.a1")
# 	w_search.send_keys(keys)
#
#
# def date(self):
# 	'''����'''
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
# 	'''��ǩΪ��˾'''
# 	cont(self)
# 	time.sleep(5)
# 	if index_cont == "������Ϣ":
# 		cont(self)
# 		time.sleep(5)
# 		if index_cont == "��˾����":
# 			company_a = companyInfo.AcompanyInfo(1)
# 			inp(self, company_a)
# 		elif index_cont == "֤ȯ���":
# 			a_securities = companyInfo.AcompanyInfo(2)
# 			inp(self, a_securities)
# 		elif index_cont == "����":
# 			cont(self)
# 			btn1 = self.driver.find_elements(By.CSS_SELECTOR, ".new-built.right")
# 			btn1[1].click()
# 		elif index_cont == "ע���ʱ�":
# 			a_finical = companyInfo.AcompanyInfo(6)
# 			inp(self, a_finical)
# 		elif index_cont == "ע���ַ":
# 			a_local = companyInfo.AcompanyInfo(4)
# 			inp(self, a_local)
# 		elif index_cont == "��ֵ":
# 			a_shizhi = companyInfo.AcompanyInfo(7)
# 			inp(self, a_shizhi)
# 		elif index_cont == "��ӯ��":
# 			a_shiyinglv = companyInfo.AcompanyInfo(8)
# 			inp(self, a_shiyinglv)
# 		elif index_cont == "��Ʊ����":
# 			a_code = companyInfo.AcompanyInfo(3)
# 			inp(self, a_code)
# 		elif index_cont == "��Ӫҵ��":
# 			a_hangye = companyInfo.AcompanyInfo(5)
# 			inp(self, a_hangye)
# 		elif index_cont == "��˾����":
# 			cont(self)
# 			btn1 = self.driver.find_elements(By.CSS_SELECTOR, ".new-built.right")
# 			btn1[1].click()
# 		elif index_cont == "��ҵ����":
# 			cont(self)
# 			time.sleep(5)
# 			cont(self)
# 			btn1 = self.driver.find_elements(By.CSS_SELECTOR, ".new-built.right")
# 			btn1[1].click()
# 		elif index_cont == "ȫ����Ѻ����":
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
# 		print("j=��", j)
# 		time.sleep(5)
# 		data = financial_data.financial(i+1, j+1)
# 		print("data=", data)
# 		inp(self, data)
#
#
# class advsearch(InitTest):
# 	'''�����������'''
#
# 	def test_001_advsearch(self):
# 		'''��½'''
# 		self.driver.get("http://ibdata.cn/#!/advsearch")
# 		self.driver.find_element(By.CLASS_NAME, "head-img").click()
# 		login.login(self)
# 		logTest.log("��½�ɹ�")
#
# 	def test_006_advsearch(self):
# 		'''A��'''
# 		logTest.log("��ʼ����A�ɣ�")
# 		div_a = self.driver.find_element(By.CLASS_NAME, "block")
# 		a = div_a.find_element(By.XPATH, "a")
# 		a.click()
# 		logTest.log(a.text)
# 		self.driver.switch_to.default_content()
# 		nav(self)
# 		if index_nav == "������Χ":
# 			cont(self)
# 			time.sleep(5)
# 			if index_cont == "�½�":
# 				cont(self)
# 				inp(self, "��Ӫҵ��")
# 			else:
# 				inp(self, "��Ӫҵ��")
# 		elif index_nav == "��˾":
# 			a_company(self)
# 		elif index_nav == "��������":
# 			date(self)
# 		elif index_nav == "֤ȯ���":
# 			cont(self)
# 		else:
# 			cont(self)
# 			time.sleep(5)
# 			button = self.driver.find_elements(By.CSS_SELECTOR, ".new-built.right")
# 			button[1].click()
#
# 		time.sleep(5)
# 		# clear(self)  # ���
# 		# time.sleep(5)
# 		btn1 = self.driver.find_element(By.CSS_SELECTOR, ".one1.right20")
# 		btn1.click()
# 		time.sleep(62)
# 		try:
# 			self.driver.switch_to.default_content()
# 			btn_del = self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-del.right30")
# 			btn_del.click()
# 			logTest.log("�ܱ�Ǹ������ʱ����������")
# 		except:
# 			logTest.log("successful")
# 		logTest.log("A�ɲ��Խ���")
#
#
# if __name__ == "__main__":
# 	unittest.main(verbosity=2)
#


import random
print(random.randint(0, 3))
