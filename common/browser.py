#!/usr/bin/env python
# encoding: utf-8
# @author: yeguanzhou
# @file: browser.py
# @time: 2023/3/17 20:53
import os
from selenium import webdriver
from common.config_utils import local_config
from common.log_utils import local_logger

current = os.path.dirname(__file__)


class Browser:
    def __init__(self, driver_path=os.path.join(current, '..', local_config.get_driver_path),
                 driver_name=local_config.get_driver_name):
        self.__driver_path = driver_path
        self.__driver_name = driver_name

    def get_driver(self):
        if self.__driver_name.lower() == 'chrome':
            return self.__get_chrome_driver()
        else:
            return self.__get_firefox_driver()

    def __get_chrome_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避BUG
        chrome_options.add_argument('lang=zh_CN.UTF-8')  # 设置默认编码为utf-8
        chrome_options.add_experimental_option('useAutomationExtension', False)  # 取消chrome受自动控制的提醒
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])  # 取消chrome受自动控制的提醒
        driver = webdriver.Chrome(executable_path=os.path.join(self.__driver_path, 'chromedriver.exe'), options=chrome_options)
        local_logger.info('返回chrome driver')
        return driver

    def __get_firefox_driver(self):
        driver = webdriver.Firefox(executable_path=os.path.join(self.__driver_path, 'geckodriver.exe'))
        local_logger.info('返回firefox driver')
        return driver

    def __get_remote_driver(self):
        pass


if __name__ == '__main__':
    Browser().get_driver()
