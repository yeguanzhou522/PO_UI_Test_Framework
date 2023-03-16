#!/usr/bin/env python
# encoding: utf-8
# @author: yeguanzhou
# @file: base_page.py
# @time: 2023/3/16 22:55

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def set_browser_max(self):
        self.driver.maximize_window()

    def set_browser_min(self):
        self.driver.minimize_window()

    def refresh(self):
        self.driver.refresh()

    def get_tittle(self):
        value = self.driver.title
        return value

    # 封装元素操作
    def find_element(self, element_info):
        locator_type_name = element_info['locator_type']
        locator_value_info = element_info['locator_value']
        locator_timeout = element_info['timeout']
        if locator_type_name == 'id':
            locator_type = By.ID
        elif locator_type_name == 'xpath':
            locator_type = By.XPATH
        elif locator_type_name == 'css_selector':
            locator_type = By.CSS_SELECTOR
        elif locator_type_name == 'class':
            locator_type = By.CLASS_NAME
        element = WebDriverWait(self.driver, locator_timeout).until(lambda x:x.find_element(locator_type, locator_value_info))
        # element = WebDriverWait(self.driver, locator_timeout).until(EC.visibility_of_element_located(locator_type, locator_value_info))
        return element

    def click(self, element_info):
        element = self.find_element(element_info)
        element.click()

    def input(self, element_info, content):
        element = self.find_element(element_info)
        element.send_keys(content)
