#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#表结构 id,group,Key,Translatable,Values,Values-zh-rCN
import csv
import codecs
import os

rootPath = "./"
inputFile = rootPath + "v6Strings.csv"
targetPath = "E:/WorkProject/SmartHomeV6Code_andriod/SmartHome/src/main/res/"
# targetPath = rootPath
outputFileData = [
    ["values/", "strings.xml", 4],
    ["values-zh-rCN/", "strings.xml", 5]
]
moduleIndex = 1
keyIndex = 2

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
                out.write("  <string name=\"%s\">%s</string>" % ((row[2]), row[column_index]))
                out.write("\n")
        out.write("</resources>")
        out.flush()
