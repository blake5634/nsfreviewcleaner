#/usr/bin/python3
#
#    Clean up text mousing from NSF reviews
#

import sys
import re as re
from datetime import date



f = open('rev1.txt')
titlemode = False

iglines = [r'Agency Tracking Number:',r'Agency Name:',r'Review',r'National Science Foundation',r'Organization:']
rev = 0
outputlines = []
for line in f:
    line = line.strip()
    
    #Proposal Review 4 : 1931699
    
    if re.match(r'^Proposal',line):
        rev += 1
        outputlines.append('\n----------------------------------------------------------------------\n')
    if line.isspace() or len(line) == 0:
        #print ('*',end='')
        continue
    if re.match(r'^[0-9]+',line):
        prop_number = line.strip()
        continue 
    if re.match(r'^Application Title:',line):
        titlemode = True
        continue
    if titlemode:
        title = line
        titlemode = False
    # just skip repetitive junk
    junkline = False
    for l in iglines:
        if re.match(l,line):
            junkline=True
            break
    if not junkline:
        outputlines.append(line)

print ('NSF Proposal Reviews ', date.today())
print ('Proposal number: ', prop_number)
print ('title:       ', title)
print ('\n')
for l in outputlines:
    print(l)
