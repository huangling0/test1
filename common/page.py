#! /usr/bin/env python
# -*- coding:utf-8
# author:mlh
# datetime:2019/6/11 上午9:58

import random
import time
from selenium.webdriver.common.by import By
from log import logTest


def page(self):
    try:
        ul = self.driver.find_element(By.CLASS_NAME, "pagination")
        lis = ul.find_elements(By.XPATH, "li")
        num = random.randint(0, len(lis)-1)
        if len(lis) == 1:
            logTest.log("只有当前页")
        else:
            lis[num].find_element(By.XPATH, "a").click()
            time.sleep(5)

    except Exception as e:
        logTest.log(e)






