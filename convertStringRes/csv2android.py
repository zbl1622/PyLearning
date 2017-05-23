#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import codecs
import os

rootPath = "./"
inputFile = rootPath + "v6Strings.csv"
targetPath = "E:/WorkProject/SmartHomeV6Code_andriod/SmartHome/src/main/res/"
# targetPath = rootPath
outputFileData = [
    ["values/", "strings.xml", 3],
    ["values-zh-rCN/", "strings.xml", 4]
]

for outputFile in outputFileData:
    targetFilePath = targetPath + outputFile[0]
    targetFile = targetFilePath + outputFile[1]
    column_index = outputFile[2]
    if not os.path.exists(targetFilePath):
        os.makedirs(targetFilePath)
    with codecs.open(targetFile, 'w', "utf-8") as out:
        s = 0
        csv_reader = csv.reader(open(inputFile, encoding='GBK'))
        out.write("<resources>\n")
        for row in csv_reader:
            s += 1
            if s == 1:
                continue
            out.write("  <string name=\"%s\">%s</string>" % ((row[1]), row[column_index]))
            out.write("\n")
        out.write("</resources>")
        out.flush()
