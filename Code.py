# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 21:11:01 2019

@author: llllewellyn
"""
import csv
fileName =  "capstoneCSVnoAschool.csv"

with open(fileName) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    line_count = 0
    emplidSet = set()
    compSet = set()
    posNumSet = set()
    posTitleSet = set()
    jobFamSet = set()
    
    for row in csv_reader:
        if line_count == 0:
            print('Column names are {", ".join(row)}')
            line_count = 1
        else:
            emplidSet.add(str(row[0]))
            compSet.add(str(row[1]))
            posNumSet.add(str(row[2]))
            posTitleSet.add(str(row[3]))
            jobFamSet.add(str(row[4]))
        

    print("Processed {line_count} lines. ")
    print("emplidSet", len(emplidSet))
    print("compSet", len(compSet))
    print("posNumSet", len(posNumSet))
    print("posTitleSet", len(posTitleSet))
    print("jobFamSet", len(jobFamSet))
    