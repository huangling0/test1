#! /usr/bin/env python
# -*- coding:utf-8
# author:mlh
# datetime:2019/6/19 下午4:03

import unittest
import os
import time
import HTMLTestRunner


def alltest():
    suite = unittest.TestLoader().discover(
        start_dir=os.path.dirname(__file__),
        pattern="test_*.py",
        top_level_dir=None)
    return suite


def getNow_time():
    return time.strftime("%Y-%m-%d,%H-%M-%S", time.localtime(time.time()))


def run():
    file = os.path.join(os.path.dirname(__file__), "report", getNow_time()+"testReport.html")
    fp = open(file, "wb")
    HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title="IBDATA_UI自动化测试报告",
        description="IBDATA自动化测试的详细信息"
    ).run(alltest())


if __name__ == "__main__":
    run()
