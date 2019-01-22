# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 08:39:56 2019

@author: JLLambert
"""
from collections import Counter
import csv
    
with open('capstoneCSV.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
        
# INIT SETS OF EVERY COLUMN IN THE CSV
    emplidSet = set()
    compSet = set()
    posNumSet = set()
    posTitleSet = set()
    jobFamSet = set()
    
# INIT LISTS OF EVERY COLUMN IN THE CSV
    emplidList = []
    compList = []
    posNumList = []
    posTitleList = []
    jobFamList = []
    
# ADD ELEM TO SETS AND TO LISTS
    for row in csv_reader:
        
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count = 1
        else:
            emplidSet.add(str(row[0]))
            compSet.add(str(row[1]))
            posNumSet.add(str(row[2]))
            posTitleSet.add(str(row[3]))
            jobFamSet.add(str(row[4]))
            
            emplidList.append(str(row[0]))
            compList.append(str(row[1]))
            posNumList.append(str(row[2]))
            posTitleList.append(str(row[3]))
            jobFamList.append(str(row[4]))
                        
    print("emplidSet",len(emplidSet))
    print("compSet",len(compSet))
    print("posNumSet",len(posNumSet))
    print("posTitleSet",len(posTitleSet))
    print("jobFamSet",len(jobFamSet))
    
    print("emplidList",len(emplidList))
    print("compList",len(compList))
    print("posNumList",len(posNumList))
    print("posTitleList",len(posTitleList))
    print("jobFamList",len(jobFamList))

    print(jobFamSet)
    
    jobFamCount = Counter(jobFamList)
    print(jobFamCount)

#    for i in jobFamSet:
#        print(i)
        


# WRITES LIST/SET TO NEW CSV FILES
    with open('counterJobFam.csv',mode='w') as csv_file:
        writer = csv.writer(csv_file)        
        writer.writerow(['jobFam','count'])
        for key, count in jobFamCount.items():
            job = key
            writer.writerow([job, count])
    
    posTitleCount = Counter(posTitleList)        
            
    with open('counterPosTitle.csv',mode='w') as csv_file:
        writer = csv.writer(csv_file)        
        writer.writerow(['posTitle','count'])
        for key, count in posTitleCount.items():
            posTitle = key
            writer.writerow([posTitle, count])
