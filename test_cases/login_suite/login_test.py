#!/usr/bin/env python
# encoding: utf-8
# @author: yeguanzhou
# @file: login_test.py
# @time: 2023/3/21 13:19

import unittest
from common.selenium_base_case import SeleniumBaseCase
from actions.login_action import LoginAction
from common.wrapper_log import wrapper_log
from common.case_data_utils import CaseDataUtils


class LogingTest(SeleniumBaseCase):
    case_data = CaseDataUtils('login_suite').convert_exceldata_to_casedata('LoginTest')

    def setUp(self) -> None:
        super().setUp()

    @wrapper_log
    @unittest.skipIf(case_data['test_login_success']['run_or_skip'], '')
    def test_login_success(self):
        case_function_data = self.case_data['test_login_success']
        self._testMethodDoc = case_function_data['test_case_name']
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.login_success(case_function_data['test_parameter'].get('username'),
                                               case_function_data['test_parameter'].get('password'))
        self.assertEqual(main_page.get_username(), case_function_data['expected_result'], '测试不通过，名称不匹配')

    @wrapper_log
    @unittest.skipIf(case_data['test_login_fail']['run_or_skip'], '')
    def test_login_fail(self):
        case_function_data = self.case_data['test_login_fail']
        self._testMethodDoc = case_function_data['test_case_name']
        login_action = LoginAction(self.base_page.driver)
        actual_result = login_action.login_fail(case_function_data['test_parameter'].get('username'),
                                                case_function_data['test_parameter'].get('password'))
        self.assertEqual(actual_result, '登录失败，请检查您的用户名或密码是否填写正确。', '测试不通过，结果不匹配')


if __name__ == '__main__':
    unittest.main(verbosity=2)
