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
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = local_config.get_url_path

    def setUp(self) -> None:
        self.base_page = BasePage(Browser().get_driver())
        self.base_page.implicitly()
        self.base_page.set_browser_max()
        self.base_page.open_url(self.url)

    def tearDown(self) -> None:
        # 测试用例失败截图
        # errors = self._outcome.errors
        # for test, error in errors:
        #     if error:
        #         self.base_page.screentshot_as_file_report()
        self.base_page.close_table()

    @classmethod
    def tearDownClass(cls) -> None:
        pass
