#!/usr/bin/env python
# encoding: utf-8
# @author: yeguanzhou
# @file: main_page.py
# @time: 2023/3/19 23:13
from common.element_data_utils import ElementdataUtils
from common.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        elements = ElementdataUtils('main').get_element_info('main_page')
        self.my_site_button = elements['my_site_button']
        self.produck_button = elements['produck_button']
        self.project_button = elements['project_button']
        self.qa_button = elements['qa_button']
        self.user_info_name_button = elements['user_info_name_button']
        self.longin_out_button = elements['longin_out_button']

    def goto_my_site(self):
        self.click(self.my_site_button)

    def goto_produck(self):
        self.click(self.produck_button)

    def goto_project(self):
        self.click(self.project_button)

    def goto_qa(self):
        self.click(self.qa_button)

    def click_user_info_name(self):
        self.click(self.user_info_name_button)

    def get_username(self):
        element = self.find_element(self.user_info_name_button)
        return element.text

    def login_out(self):
        self.click_user_info_name()
        self.click(self.longin_out_button)
