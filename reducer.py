#!/usr/bin/env python

import sys

c=0

for line in sys.stdin:
    if c<1:
        mean=line.strip().split()[1:]
        for i in range(len(mean)):
            mean[i]=float(mean[i])
        c+=1

    elif c==1:
        cols=line.strip().split()[1:]
        cols.pop(6)
        cols.append('RESULT')
        print(','.join(cols).strip())
        c+=1

    else:
        line=line.strip().split(',')
        if line[2]=='':
            line[2]=str(mean[0])

        if line[3]=='':
            line[3]=str(mean[1])

        if line[5]=='':
            line[5]=str(mean[2])

        if line[6]=='':
            line[6]=str(mean[3])

        if line[7]=='':
            line[7]=str(mean[4])

        if line[8]=='':
            line[8]=str(mean[5])

        if line[9]=='':
            line[9]=str(mean[6])
     
        a=line.pop(6)

        if float(a)>15:
            line.append('1')

        else:
            line.append('0')

        print(','.join(line).strip())

