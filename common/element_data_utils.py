#!/usr/bin/env python
# encoding: utf-8
# @author: yeguanzhou
# @file: element_data_utils.py
# @time: 2023/3/17 19:02

import os
from common.excel_utils import ExcelUtils
from common.config_utils import local_config
from common.log_utils import local_logger


class ElementdataUtils:
    def __init__(self, module_name, element_path=os.path.join(os.path.dirname(__file__), local_config.get_excel_path, 'element_info_datas.xlsx')):
        self.__excel_utils = ExcelUtils(element_path, module_name)

    def get_element_info(self, page_name):
        """
        将excel数据转换成{{},{},{},...}格式
        :param page_name: excel数据的页面名称，如login_page
        :return:元素信息字典
        """
        element_info = self.__excel_utils.get_sheet_data_by_dict()
        element_infos = {}
        for name in element_info:
            if element_info[name]['page_name'] == page_name:  # 判断所属页面
                element_info[name]['timeout'] = element_info[name]['timeout'] if isinstance(
                    element_info[name]['timeout'], float) else local_config.get_time_out  # 如果time_out为空，则取默认超时时间
                element_infos[name] = element_info[name]
        local_logger.info('根据module：{},page_name:{} 获取元素信息：{}'.format(self.__excel_utils.sheet_name, page_name, element_info.keys()))
        return element_infos


if __name__ == '__main__':
    element_info_data = ElementdataUtils('login').get_element_info('login_page')
    print(element_info_data)
