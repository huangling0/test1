#! /usr/bin/env python
# -*- coding:utf-8
# author:mlh
# datetime:2019/6/18 下午3:16

import logging


def log(log_content):
    # 定义文件
    logFile = logging.FileHandler('..\\log\\logInfo.md', 'a')
    # log格式
    fmt = logging.Formatter(fmt="%(asctime)s-%(name)s-%(levelname)s-%(module)s:%(message)s")
    logFile.setFormatter(fmt)

    # 定义日志
    logger1 = logging.Logger("logTest", level=logging.DEBUG)
    logger1.addHandler(logFile)
    logger1.info(log_content)
