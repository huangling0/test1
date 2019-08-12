# !/user/bin/env python
# -*- coding:utf-8 -*-
# author：mlh

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://quote.eastmoney.com/hk/HStock_list.html")
driver.maximize_window()
driver.implicitly_wait(30)
div = driver.find_element_by_class_name("hklists")
ul = div.find_element_by_xpath("ul")
lis = ul.find_elements_by_xpath("li")
for i in range(len(lis)):
	text = lis[i].get_attribute('textContent')
	print(text)
