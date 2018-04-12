# 转换APP国际化翻译字符重构汇总.xlsx文件中的简体中文到繁体中文

import re
import xlrd
import xlwt
import codecs
import os
from langconv import *


def Simplified2Traditional(sentence):
    sentence = Converter('zh-hant').convert(sentence)
    return sentence


target_path = 'D:/WorkProjects/SmartHomeV6Code_andriod_develop/SmartHome/src/main/res/'
app_source_file = './APP国际化翻译字符重构汇总.xlsx'
app_zh_column = 4
h5_source_file = './H5国际化翻译字符重构汇总.xlsx'
h5_zh_column = 3


def convert_safe_string(text):
    s = str(text).replace('<font>', '[font]').replace('</font>', '[/font]') \
        .replace('\n', '\\n') \
        .replace('\'', '\\\'') \
        .replace('&', '&#038;')
    return re.sub('%\D|%$', lambda x: "%%" + x.group()[1:], s)


def read_excel():
    outfile = xlwt.Workbook()
    # 新建一个sheet
    wtable = outfile.add_sheet('info', cell_overwrite_ok=True)

    data = xlrd.open_workbook(app_source_file)
    table = data.sheets()[0]
    nrows = table.nrows
    write_column = 0
    wtable.write(0, write_column, "APP")
    for i in range(1, nrows):
        value = str(table.row_values(i)[app_zh_column])
        # 写入数据table.write(行,列,value)
        wtable.write(i, write_column, Simplified2Traditional(value))
    print('读取完毕 app')

    data = xlrd.open_workbook(h5_source_file)
    table = data.sheets()[0]
    nrows = table.nrows
    write_column = 1
    wtable.write(0, write_column, "H5")
    for i in range(1, nrows):
        value = str(table.row_values(i)[h5_zh_column])
        # 写入数据table.write(行,列,value)
        wtable.write(i, write_column, Simplified2Traditional(value))
    print('读取完毕 h5')
    # 保存文件
    outfile.save('zht.xls')


if __name__ == '__main__':
    read_excel()
