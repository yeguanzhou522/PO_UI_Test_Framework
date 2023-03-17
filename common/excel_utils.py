#!/usr/bin/env python
# encoding: utf-8
# @author: yeguanzhou
# @file: excel_utils.py
# @time: 2023/3/16 21:00

import os
import xlrd
from common.config_utils import local_config

class ExcelUtils(object):
    def __init__(self, excel_path=local_config.get_excel_path, sheet_name=None):
        self.excel_path = excel_path
        self.sheet_name = sheet_name
        self.sheet_data = self.__get_sheet_data()

    def __get_sheet_data(self):
        try:
            workbook = xlrd.open_workbook(self.excel_path)
        except xlrd.biffh.XLRDError:
            print('非Excel文件，请重新上传')
        except FileNotFoundError:
            print('文件不存在，请重新上传')
        except Exception as e:
            print('系统异常:', e)
        else:
            if self.sheet_name:  # 当sheet_name没有带参数时，默认取第一个sheet页
                sheet = workbook.sheet_by_name(self.sheet_name)
            else:
                sheet = workbook.sheet_by_index(0)
            return sheet

    @property
    def get_row_cont(self):
        row_cont = self.sheet_data.nrows
        return row_cont

    @property
    def get_col_cont(self):
        col_cont = self.sheet_data.ncols
        return col_cont

    def get_sheet_data_by_list(self):  # 把Excel的数据转换成[[],[],...],去除第一行数据
        all_excel_data = []
        for rownum in range(1, self.get_row_cont):
            row_excel_data = []
            for colnum in range(self.get_col_cont):
                row_excel_data.append(self.sheet_data.cell_value(rownum, colnum))
            all_excel_data.append(row_excel_data)
        return all_excel_data

    def get_sheet_data_by_dict(self):  # 把Excel的数据转换成{"var1":{}, "var2":{}, ...}
        all_excel_data = {}
        for rownum in range(1, self.get_row_cont):
            row_excel_data = {}
            for colnum in range(1, self.get_col_cont):
                row_excel_data[self.sheet_data.cell_value(0, colnum)] = self.sheet_data.cell_value(rownum, colnum)
            all_excel_data[self.sheet_data.cell_value(rownum, 0)] = row_excel_data
        return all_excel_data


if __name__ == '__main__':
    excel_until = ExcelUtils()
    print(excel_until.get_col_cont)
    print(excel_until.get_row_cont)
    print(excel_until.get_sheet_data_by_dict())
    for i in excel_until.get_sheet_data_by_dict():
        print(i, excel_until.get_sheet_data_by_dict()[i])