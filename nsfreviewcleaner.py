#/usr/bin/python3
#
#    Clean up text mousing from NSF reviews
#

import sys
import re as re
from datetime import date


f = open(sys.argv[1]) 
titlemode = False

iglines = [r'Agency Tracking Number:',r'Agency Name:',r'Review',r'National Science Foundation',r'Organization:']
rev = 0
outputlines = []
ParaMode = True
para = ''  # current paragraph being collected.
for line in f:
    line = line.strip()
    EmptyLine = False

    #Proposal Review 4 : 1931699
    
        
    if line.isspace() or (len(line) == 0) or (line=='\n'):
        line = ''
        EmptyLine = True
        # end of paragraph

    #   Output a break between reviews
    
    if re.match(r'^Proposal',line):
        rev += 1
        outputlines.append('\n----------------------------------------------------------------------\n')
    # collect some stuff for output header and do not output it.
    if re.match(r'^[0-9]{5,10}',line):
        prop_number = line.strip()
        continue 
    if re.match(r'^Application Title:',line):
        titlemode = True
        continue
    if titlemode and not EmptyLine:
        title = line
        titlemode = False
        continue
        
    # just skip repetitive junk
    junkline = False
    for l in iglines:
        if re.match(l,line):
            junkline=True
            
    # if at end of paragraph, 
    
    if (not junkline) and (not EmptyLine):
        para += line + ' ' # got rid of newlines.

    if EmptyLine and (len(para) > 0):
        outputlines += [para + '\n']
        para = ''
        
print ('NSF Proposal Reviews ', date.today())
print ('Proposal number: ', prop_number)
print ('title:       ', title)
print ('\n')
for l in outputlines:
    print(l)
