#!/usr/bin/env python
# encoding: utf-8
# @author: yeguanzhou
# @file: demo_01.py
# @time: 2023/3/16 21:47

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://127.0.0.1/zentao/my.html')
# driver.get('https://www.baidu.com/')
time.sleep(10)
print(123456)
driver.refresh()
time.sleep(2)