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
        self.__conf_path = config_path
        self.__conf = configparser.ConfigParser()
        self.__conf.read(self.__conf_path, encoding='utf-8')

    def __get_config(self, section, option):
        return self.__conf.get(section, option)


    @property
    def get_url_path(self):
        url_path = self.__get_config('default', 'url_test_path')
        return url_path

    @property
    def get_chromedriver_path(self):
        chromedriver_path = self.__get_config('default', 'chrome_driver_path')
        return chromedriver_path

    @property
    def get_excel_path(self):
        excel_path = self.__get_config('default', 'excel_path')
        return excel_path

config = ConfigUtils()
if __name__ == '__main__':
    print(config.get_excel_path)
