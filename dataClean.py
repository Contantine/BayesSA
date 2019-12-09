import numpy
import pandas as pd
from pandas import DataFrame, Series
import os
from openpyxl import Workbook
from openpyxl import load_workbook

file_name = u'book_info.xlsx'
dir_prefix = u'short_comments/'
target_dir = u'cleaned_data/'

if __name__ == '__main__':
    files = os.listdir(target_dir)
    for file in files:
        wb = load_workbook(target_dir + file)
        ws = wb.active
        ws['B1'] = '用户名'
        ws['C1'] = '短评内容'
        ws['D1'] = ''
        ws.delete_cols(1)
        wb.save(target_dir + file)
        print(f'{file}修改完成')
