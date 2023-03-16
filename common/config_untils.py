#!/usr/bin/env python
# encoding: utf-8
# @author: yeguanzhou
# @file: config_untils.py
# @time: 2023/3/16 21:06

import os
import configparser

current = os.path.dirname(__file__)
conf_filepath = os.path.join(current, '../conf/config.ini')
class ConfigUntils:
    def __init__(self,config_path = conf_filepath):
        self.config_path = config_path
