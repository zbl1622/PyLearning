# 转换APP国际化翻译字符重构汇总.xlsx文件到项目中国际化文件的脚本
# 使用前先配置好target_path和source_file，以及output_strcut中国际化语言对应的列标题

import re
import xlrd
import codecs
import os

target_path = 'D:/WorkProjects/SmartHomeV6Code_andriod_develop/SmartHome/src/main/res/'
source_file = './APP国际化翻译字符重构汇总.xlsx'
output_strcut = [
    # 目标目录名，在表格中列数，在表格中标题，是否需要替换半角符号
    ["values", 0, "Wulian-EN", True],
    ["values-zh-rCN", 0, "Wulian-CN", False],
    ["values-ja", 0, "Wulian-JP", False]
]
key_list = list()


def convert_safe_string(text):
    s = str(text).replace('<font>', '[font]').replace('</font>', '[/font]') \
        .replace('\n', '\\n') \
        .replace('\'', '\\\'') \
        .replace('&', '&#038;')
    return re.sub('%\D|%$', lambda x: "%%" + x.group()[1:], s)


def read_excel():
    global key_list, output_strcut
    data = xlrd.open_workbook(source_file)
    table = data.sheets()[0]

    # 初始化翻译语言对应的列数
    head_row = table.row_values(0)
    for output_data in output_strcut:
        for i in range(0, len(head_row)):
            if output_data[2] == head_row[i]:
                output_data[1] = i
                break

    nrows = table.nrows
    key_list = list()
    for i in range(1, nrows):
        s = dict()
        s['group'] = table.row_values(i)[1]
        s['key'] = table.row_values(i)[2].strip()
        if not s['key']:
            continue
        for f in output_strcut:
            value = str(
                table.row_values(i)[f[1]] if table.row_values(i)[f[1]] else table.row_values(i)[output_strcut[0][1]])
            if f[3]:
                value = value.replace("，", ",").replace("“", "\"").replace("”", "\"")
            s[f[0]] = value
        key_list.append(s)
    key_list = sorted(key_list, key=lambda x: x['group'])
    print('读取完毕')


def convert_2_xml():
    global key_list, output_strcut
    for f in output_strcut:
        path = f[0]
        if not os.path.exists(target_path + path):
            os.makedirs(path)
        with codecs.open(target_path + path + '/strings.xml', 'w', "utf-8") as out:
            out.write("<resources>\n")
            last_group = None
            for s in key_list:
                if not s['group'] == last_group:
                    last_group = s['group']
                    out.write("\n")
                    out.write("\t<!-- %s -->" % last_group)
                    out.write("\n")
                out.write('\t<string name="%s">%s</string>' % (s['key'], convert_safe_string(s.get(path))))
                out.write('\n')
            out.write("</resources>")
            out.flush()


if __name__ == '__main__':
    read_excel()
    convert_2_xml()
