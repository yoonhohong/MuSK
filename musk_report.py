#! /usr/bin/python
#-*- coding: utf-8 -*-
import csv

with open("musk_20180831.csv", "r") as f:
    f1 = csv.reader(f)
    lines = list(f1)[1:]
    for line in lines:
        data = line
        f2name = "{0}_{1}_{2}".format(data[0], data[2], data[1])
        with open("{0}.md".format(f2name), "w") as f2:
            f2.write('''
## MuSK-Ab Report

Hospital:{2}  \r
Patient name:{0}  \r
Date of sample arrival:{1}  \r
Date of MusK-Ab test: {3}  \r

Result:  \r
{4}  \r
concentration = {5} IU/mL  \r

Note: For research use only, not for use in diagnostic procedures.  \r
If you have any question, contact at nrhong@gmail.com.  \r

HongLab  \r
Neurology  \r
Seoul National University College of Medicine  \r
SNU SMG Boramae Medical Center  \r
            '''.format(data[0], data[1], data[2], data[3], data[4], data[5])
            )
