#!/usr/bin/env python
# encoding: utf-8
# @author: yeguanzhou
# @file: login_test.py
# @time: 2023/3/21 13:19

import unittest
from common.selenium_base_case import SeleniumBaseCase
from actions.login_action import LoginAction
from common.wrapper_log import wrapper_log


class LogingTest(SeleniumBaseCase):
    @wrapper_log
    def test_login_success(self):
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.login_success('test01', 'newdream123')
        self.assertEqual(main_page.get_username(), 'test012', '测试不通过，名称不匹配')


if __name__ == '__main__':
    unittest.main()
