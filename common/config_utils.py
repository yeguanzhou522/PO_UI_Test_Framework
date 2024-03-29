#!/usr/bin/env python
# encoding: utf-8
# @author: yeguanzhou
# @file: config_utils.py
# @time: 2023/3/16 21:06

import os
import configparser

current = os.path.dirname(__file__)
conf_filepath = os.path.join(current, '../conf/config.ini')


class ConfigUtils:
    def __init__(self, config_path=conf_filepath):
        self.__conf = configparser.ConfigParser()
        self.__conf.read(config_path, encoding='utf-8')

    def __get_config(self, section, option):
        return self.__conf.get(section, option)

    @property
    def get_url_path(self):
        url_path = self.__get_config('default', 'url_test_path')
        return url_path

    @property
    def get_driver_path(self):
        driver_path = self.__get_config('default', 'driver_path')
        return driver_path

    @property
    def get_excel_path(self):
        excel_path = self.__get_config('default', 'excel_path')
        return excel_path

    @property
    def get_log_path(self):
        log_path = self.__get_config('default', 'log_path')
        return log_path

    @property
    def get_report_path(self):
        report_path = self.__get_config('default', 'report_path')
        return report_path

    @property
    def get_testcase_path(self):
        testcase_path = self.__get_config('default', 'testcase_path')
        return testcase_path

    @property
    def get_case_path(self):
        case_path = self.__get_config('default', 'case_path')
        return case_path

    @property
    def get_driver_name(self):
        driver_name = self.__get_config('default', 'driver_name')
        return driver_name

    @property
    def get_default_username(self):
        default_username = self.__get_config('default', 'default_username')
        return default_username

    @property
    def get_default_password(self):
        default_password = self.__get_config('default', 'default_password')
        return default_password

    @property
    def get_time_out(self):
        time_out = float(self.__get_config('default', 'time_out'))
        return time_out

    @property
    def get_screentshot_path(self):
        screentshot = self.__get_config('default', 'screentshot_path')
        return screentshot


local_config = ConfigUtils()
if __name__ == '__main__':
    print(local_config.get_excel_path)
