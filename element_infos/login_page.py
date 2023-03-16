#!/usr/bin/env python
# encoding: utf-8
# @author: yeguanzhou
# @file: login_page.py
# @time: 2023/3/16 21:17

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_inputbox = {'element_name': '用户名输入框', 'locator_type': 'css_selector',
                                  'locator_value': 'input#account', 'timeout': 3}
        self.password_inputbox = {'element_name': '用户名输入框', 'locator_type': 'css_selector',
                                  'locator_value': 'input[name="password"]', 'timeout': 3}
        self.login_button = {'element_name': '用户名输入框', 'locator_type': 'css_selector',
                             'locator_value': 'button#submit', 'timeout': 3}
        self.keeplogin_checkbox = {'element_name': '用户名输入框', 'locator_type': 'css_selector',
                                   'locator_value': 'input#keepLoginon', 'timeout': 3}

    def input_username(self, username):
        self.input(self.username_inputbox, username)

    def input_password(self, password):
        self.input(self.password_inputbox, password)

    def click_login(self):
        self.click(self.login_button)

    def click_keeplogin(self):
        self.click(self.keeplogin_checkbox)


if __name__ == '__main__':
    current_path = os.path.dirname(__file__)
    webdriver_path = os.path.join(current_path, '../webdriver/chromedriver.exe')
    driver = webdriver.Chrome(executable_path=webdriver_path)
    login_page = LoginPage(driver)
    login_page.set_browser_max()
    login_page.open_url('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
    login_page.input_username('test01')
    login_page.input_password('newdream123')
    login_page.click_login()
    time.sleep(20)

