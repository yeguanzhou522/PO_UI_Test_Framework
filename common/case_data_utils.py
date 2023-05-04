#!/usr/bin/env python
# encoding: utf-8
# @author: yeguanzhou
# @file: case_data_utils.py
# @time: 2023/3/23 22:11

import os
from common.excel_utils import ExcelUtils
from common.config_utils import local_config


class CaseDataUtils:
    def __init__(self, case_suite_name,
                 case_path=os.path.join(os.path.dirname(__file__), local_config.get_testcase_path,
                                        'testcase_datas.xlsx')):
        self.__excel_data = ExcelUtils(sheet_name=case_suite_name, excel_path=case_path).get_sheet_data_by_list()

    def convert_exceldata_to_casedata(self, test_class_name):
        """
        {'test_login_success': {'test_case_name': '', 'run_or_stop': ’‘, 'expected_result': '', 'test_parameter': {'': '', '': ''}},
        'test_login_fail': {'test_case_name': '', 'run_or_stop': ’‘, 'expected_result': '', 'test_parameter': {'': '', '': ''}},}
        :param test_class_name: 所属测试类
        :return: 测试用例字典
        """
        test_data_infos = {}
        for i in range(0, len(self.__excel_data)):
            test_data_info = {}
            if self.__excel_data[i][2].__eq__(test_class_name):
                test_data_info['test_case_name'] = self.__excel_data[i][1]
                # False代表run，True代表skip
                test_data_info['run_or_skip'] = False if self.__excel_data[i][3].__eq__('是') else True
                test_data_info['expected_result'] = self.__excel_data[i][4]
                test_parameter = {}
                for j in range(5, len(self.__excel_data[i])):
                    if self.__excel_data[i][j].__contains__('=') and len(self.__excel_data[i][j]) > 2:
                        parameter_info = self.__excel_data[i][j].split('=')
                        test_parameter[parameter_info[0]] = parameter_info[1]
                test_data_info['test_parameter'] = test_parameter
            test_data_infos[self.__excel_data[i][0]] = test_data_info
        return test_data_infos


if __name__ == '__main__':
    a = CaseDataUtils('login_suite').convert_exceldata_to_casedata('LoginTest')
    print(a)
