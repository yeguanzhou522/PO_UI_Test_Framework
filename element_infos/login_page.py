#!/usr/bin/env python
# encoding: utf-8
# @author: yeguanzhou
# @file: login_page.py
# @time: 2023/3/16 21:17

import os
import time
from selenium import webdriver
from common.base_page import BasePage
from common.element_data_utils import ElementdataUtils
from common.config_utils import local_config
from common.browser import Browser

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        elements = ElementdataUtils('login').get_element_info()
        self.username_inputbox = elements['username_inputbox']
        self.password_inputbox = elements['password_inputbox']
        self.login_button = elements['login_button']
        self.keeplogin_checkbox = elements['keeplogin_checkbox']

    def input_username(self, username):
        self.input(self.username_inputbox, username)

    def input_password(self, password):
        self.input(self.password_inputbox, password)

    def click_login(self):
        self.click(self.login_button)

    def click_keeplogin(self):
        self.click(self.keeplogin_checkbox)


if __name__ == '__main__':
    driver = Browser().get_driver()
    login_page = LoginPage(driver)
    login_page.set_browser_max()
    login_page.time()
    login_page.open_url('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
    login_page.input_username('test01')
    login_page.input_password('newdream123')
    login_page.click_login()
    time.sleep(5)

