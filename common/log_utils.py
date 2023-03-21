#!/usr/bin/env python
# encoding: utf-8
# @author: yeguanzhou
# @file: log_utils.py
# @time: 2023/3/21 16:33

import os
import time
import traceback
from loguru import logger
from common.config_utils import local_config

now = time.strftime("%Y_%m_%d")


class Logger:
    """
        严重等级：...
    """
    def __init__(self, need_log=True):
        self.my_logger = logger
        if need_log is True:  # 判断是否需要写入日志
            self.my_logger.add(
                os.path.join(os.path.dirname(__file__), local_config.get_log_path, f'UITest_log_{now}.log'),
                encoding='utf-8', retention='10 days')

    def info(self, content):
        self.my_logger.info(content)

    def debug(self, content):
        self.my_logger.debug(content)

    def error(self, content):
        self.my_logger.error(content)

    def critical(self, content):
        self.my_logger.critical(content)

    def warning(self, content):
        self.my_logger.warning(content)

    def success(self, content):
        self.my_logger.success(content)

    def trace(self, content):
        self.my_logger.trace(content)

    def traceback(self):
        self.my_logger.error(f'执行失败！！！失败信息：\n {traceback.format_exc()}')


local_logger = Logger()
