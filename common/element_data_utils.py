#!/usr/bin/env python
# encoding: utf-8
# @author: yeguanzhou
# @file: element_data_utils.py
# @time: 2023/3/17 19:02

import os
from common.excel_utils import ExcelUtils
from common.config_utils import config

class ElementdataUtils:
    def __init__(self,  sheet_name=None, element_path=config.get_excel_path):
        self.__excel_utils = ExcelUtils(element_path, sheet_name)

    def get_element_info(self, module_name=None):
        element_infos = self.__excel_utils.get_sheet_data_by_dict()
        return element_infos


if __name__ == '__main__':
    element_info_data = ElementdataUtils('login').get_element_info()
    print(element_info_data)