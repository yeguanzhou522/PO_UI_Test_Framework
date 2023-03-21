#!/usr/bin/env python
# encoding: utf-8
# @author: yeguanzhou
# @file: wrapper_log.py
# @time: 2023/3/21 22:01

import time
from common.log_utils import local_logger
from functools import wraps


def wrapper_log(func):
    """
    无参装饰器，也可以写成有参装饰器，True或Flase标记是否调用日志模块
    功能一：执行失败，打印并记录错误日志信息，定位bug
    功能二：记录用例执行时间
    """

    @wraps(func)  # wraps使inner装的更像一个func
    def inner(*args, **kwargs):

        local_logger.info(f'{func.__name__}用例执行开始')
        now1 = time.time()

        try:
            func(*args, **kwargs)
        except Exception as e:
            local_logger.error(f'用例执行失败，失败原因：{e}')
            local_logger.traceback()
            raise e

        now2 = time.time()
        local_logger.success(f'{func.__name__}用例执行成功！！！，用例执行用时:{now2 - now1}ms')
        return func

    return inner
