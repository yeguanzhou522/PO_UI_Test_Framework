#!/usr/bin/env python
# encoding: utf-8
# @author: yeguanzhou
# @file: selenium_base_case.py
# @time: 2023/3/21 13:55

import unittest
from common.base_page import BasePage
from common.browser import Browser
from common.config_utils import local_config


class SeleniumBaseCase(unittest.TestCase):
    def setUp(self) -> None:
        self.base_page = BasePage(Browser().get_driver())
        self.base_page.implicitly()
        self.base_page.set_browser_max()
        self.base_page.open_url(local_config.get_url_path)

    def tearDown(self) -> None:
        self.base_page.close_table()
