#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 表结构 id,group,Key,Translatable,Values,Values-zh-rCN
import csv
import codecs
import os

rootPath = "./"
inputFile = rootPath + "v6Strings.csv"
targetPath = "D:/WorkProject/SmartHomeV6Code_andriod/SmartHome/src/main/res/"
# targetPath = rootPath
outputFileData = [
    ["values/", "strings.xml", 5],
    ["values-zh-rCN/", "strings.xml", 4]
]
moduleIndex = 1
keyIndex = 2

def convertSafeString(text):
    return text.replace('<font>','[font]').replace('</font>','[/font]')\
        .replace('\n', '\\n')\
        .replace('\'', '\\\'')\
        .replace('&','&#038;')

for outputFile in outputFileData:
    targetFilePath = targetPath + outputFile[0]
    targetFile = targetFilePath + outputFile[1]
    column_index = outputFile[2]
    if not os.path.exists(targetFilePath):
        os.makedirs(targetFilePath)
    with codecs.open(targetFile, 'w', "utf-8") as out:
        s = 0
        csv_reader = csv.reader(open(inputFile, encoding='GBK'))

        dataMap = {}
        for row in csv_reader:
            s += 1
            if s == 1:
                continue
            moduleName = row[moduleIndex]
            dataList = []
            if moduleName in dataMap:
                dataList = dataMap[moduleName]
            else:
                dataMap[moduleName] = dataList
            dataList.append(row)

        out.write("<resources>\n")
        keysList = list(dataMap.keys())
        keysList.sort()
        for moduleName in keysList:
            dataList = dataMap[moduleName]
            out.write("\n")
            out.write("  <!-- %s -->" % (moduleName))
            out.write("\n")
            for row in dataList:
                valueLength = len(row[column_index])
                if valueLength == 0:
                    if len(row[0]) > 5:
                        out.write("  <!-- %s -->" % (row[0]))
                    else:
                        out.write("  <string name=\"%s\">%s</string>" % (
                            (row[2].replace('\n', '')), convertSafeString(row[4])))
                    out.write("\n")
                else:
                    out.write("  <string name=\"%s\">%s</string>" % (
                        (row[2].replace('\n', '')), convertSafeString(row[column_index])))
                    out.write("\n")
        out.write("</resources>")
        out.flush()
