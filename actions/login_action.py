#!/usr/bin/env python
# encoding: utf-8
# @author: yeguanzhou
# @file: login_action.py
# @time: 2023/3/19 23:04

from element_infos.login.login_page import LoginPage
from element_infos.main.main_page import MainPage
from common.config_utils import local_config
from common.browser import Browser


class LoginAction:  # 登录常用业务功能
    def __init__(self, driver):
        self.login_page = LoginPage(driver)

    def login_action(self, username, password):
        self.login_page.input_username(username)
        self.login_page.input_password(password)
        self.login_page.click_login()

    def login_success(self, username, password):
        self.login_action(username, password)
        return MainPage(self.login_page.driver)

    def login_fail(self, username, password):
        self.login_action(username, password)
        return self.login_page.switch_to_alert()

    def default_login(self):
        self.login_success(local_config.get_default_username, local_config.get_default_password)

if __name__ == '__main__':
    driver = Browser().get_driver()
    login_action = LoginAction(driver)
    login_action.login_page.set_browser_max()
    login_action.login_page.open_url(local_config.get_url_path)
    login_action.default_login()
    login_action.login_page.wait()
