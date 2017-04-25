#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import codecs

rootPath = "./"
inputFile = "strings.csv"
outputFile = "strings.xml"

csv_reader = csv.reader(open(rootPath + inputFile, encoding='utf-8'))
with codecs.open(outputFile, 'w', "utf-8") as out:
    s = 0
    out.write("<resources>\n")
    for row in csv_reader:
        s += 1
        if s == 1:
            continue
        out.write("  <string name=\"%s\">%s</string>" % ((row[0]), row[2]))
        out.write("\n")
    out.write("</resources>")
    out.flush()
