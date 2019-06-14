import csv
import os
import fnmatch
import datetime

                                              

fullpath1 = input("Full path to File 1: ")
type(fullpath1)

fullpath2 = input("Full path to File 2: ")
type(fullpath2)

local = input("Where should the compare report drop to: ")
type(local)


with open(fullpath1, 'r', errors='ignore') as t1, open(fullpath2, 'r', errors='ignore') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

os.chdir(local)
with open('Differences.csv', 'w') as outFile:
    for line in filetwo:
        if line not in fileone:
            outFile.write(line)
