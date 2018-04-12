# 转换APP国际化翻译字符重构汇总.xlsx文件中的简体中文到繁体中文

import re
import codecs
import os
from langconv import *

root_path = './values'
input_file = root_path + '/disclaimer_zh_cn.html'
output_file = root_path + '/disclaimer_zh_hk.html'


def simplified2traditional(sentence):
    sentence = Converter('zh-hant').convert(sentence)
    return sentence


def read_file_as_str(file_path):
    # 判断路径文件存在
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")

    all_the_text = codecs.open(file_path, 'r', 'utf-8').read()
    # print type(all_the_text)
    return all_the_text


def do_convert():
    text = read_file_as_str(input_file)
    convert_text = simplified2traditional(text)
    f = codecs.open(output_file, 'w', 'utf-8')
    f.write(convert_text)
    f.flush()
    f.close()


if __name__ == '__main__':
    do_convert()
