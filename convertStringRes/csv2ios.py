#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import codecs
import os

rootPath = "./"
inputFile = rootPath + "v6Strings.csv"
targetPath = "E:/WorkProject/iosV6/"
# targetPath = rootPath
outputFileData = [["en.lproj/", "Localizable.strings", 3], ["zh-Hans.lproj/", "Localizable.strings", 4]]

for outputFile in outputFileData:
    targetFilePath = targetPath + outputFile[0]
    targetFile = targetFilePath + outputFile[1]
    column_index = outputFile[2]
    if not os.path.exists(targetFilePath):
        os.makedirs(targetFilePath)
    with codecs.open(targetFile, 'w', "utf-8") as out:
        s = 0
        csv_reader = csv.reader(open(inputFile, encoding='GBK'))
        for row in csv_reader:
            s += 1
            if s == 1:
                continue
            out.write("\"%s=   \"%s\"" % ((row[1] + "\"").ljust(60), row[column_index]))
            out.write("\n")
        out.flush()
