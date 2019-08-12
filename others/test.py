# !/user/bin/env python
# -*- coding:utf-8 -*-
# author：mlh

# from selenium import webdriver
# import xlrd
# import openpyxl
# import random

#driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# driver.maximize_window()
# driver.implicitly_wait(30)
# inp = driver.find_element_by_id("kw")
# inp.send_keys("")
# btn = driver.find_element_by_id("su")
# btn.click()

# excel = openpyxl.load_workbook("data\\ibdata.xlsx")
# sheets = excel.sheetnames
# print(sheets)
# for i in range(len(sheets)):
# 	sheet = excel[sheets[i]]
#
# 	num = random.randint(1, sheet.max_row+1)
# 	print("".join([str(sheet.cell(row=num, column=1).value)]))
# 	# print(''.join([str(sheet.cell(row=j, column=c).value).ljust(20) for c in range(1, sheet.max_column + 1)]))

# excel = openpyxl.load_workbook("data\\chengzhangnengli.xlsx")
# sheets = excel.sheetnames
# print(sheets)
#
# excel = openpyxl.load_workbook("data\\changzhainengli.xlsx")
# sheets = excel.sheetnames
# print(sheets)


# class MyNumbers:
# 	def __iter__(self):
# 		self.a = 1
# 		return self
#
# 	def __next__(self):
# 		if self.a < 10:
# 			b = self.a
# 			self.a += 1
# 			return b
# 		else:
# 			raise StopIteration
#
#
# nums = MyNumbers()
# num = iter(nums)
# for i in num:
# 	print(i)

# a = [1, 2, 3, 4, 5, 5, 5, 5]
# b = [11, 22, 33]
# a.append(6)
# print(a)
# a.extend(b)
# print(a)
# a.insert(8, 7)
# print(a)
# a.remove(1)
# print(a)
# a.pop(8)
# print(a)
# a.index(11)
# print(a)
# a.count(5)
# print(a)
# a.sort()
# print(a)
# a.reverse()
# print(a)
# a.copy()
# print(a)
# a.clear()
# print(a)


# import os
# dir(os)
# print(dir(os))


import time

print(time.time())
t = int(time.mktime(time.strptime('2019-08-08 00:00:00', '%Y-%m-%d %H:%M:%S')))
print(t)
