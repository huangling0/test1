# !/user/bin/env python
# -*- coding:utf-8 -*-
# author：mlh

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E5%9F%8E%E5%B8%82%E5%90%8D%E7%A7%B0%E5%A4%A7%E5%85%A8/14892072?fr=aladdin")

para = driver.find_elements_by_class_name("para")
for i in range(1, len(para)):
	print(para[i].text)
