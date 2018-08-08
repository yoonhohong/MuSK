#! /usr/bin/python
#-*- coding: utf-8 -*-

with open("musk_result.txt", "r") as f:
    f1 = f.read()
    lines = f1.splitlines()
    for line in lines:
        data = line.split()
        f2name = "20170529_{0}_{1}".format(data[2], data[1])
        with open("{0}.md".format(f2name), "w") as f2:
            f2.write('''
## MuSK-Ab Report

Hospital:{0}  \r
Patient name:{1}  \r
Date of sample arrival:20{2}  \r
Date of MusK-Ab test: 2017.05.24  \r
Date of report: 2017.05.29  \r

Result:  \r
{3}  \r
concentration = {4} IU/mL  \r

Note: For research use only, not for use in diagnostic procedures.  \r
If you have any question, contact at nrhong@gmail.com.  \r

HongLab  \r
Neurology  \r
Seoul National University College of Medicine  \r
SNU SMG Boramae Medical Center  \r
            '''.format(data[1], data[2], data[0], data[3], data[4]))
