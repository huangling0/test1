# !/user/bin/env python
# -*- coding:utf-8 -*-
# author：mlh

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://data.eastmoney.com/gpzy/pledgeRatio.aspx")
driver.maximize_window()
driver.implicitly_wait(30)
lis = driver.find_elements_by_class_name("col")
for i in range(len(lis)):
	t = lis[i].get_attribute('textContent')
	print(t)
for j in range(65):
	driver.find_element_by_css_selector("#PageCont > a:nth-child(9)").click()
	for i in range(len(lis)):
		t1 = lis[i].get_attribute('textContent')
		print(t1)



