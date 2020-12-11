#!/usr/bin/env python

import sys

dep=[0,0]
arr=[0,0]

deptime=[0,0];arrtime=[0,0];air=[0,0];crselap=[0,0]
actelap=[0,0]

for line in sys.stdin:
    line=line.strip().split(',')
    line.pop()
    line=line[2:3] + line[5:8] + line[12:15] + line[18:22]

    if line[2]!='' and line[2]!='DEP_TIME':
        deptime[0]+=float(line[2])
        deptime[1]+=1

    if line[3]!='' and line[3]!='DEP_DELAY':
        dep[0]+=float(line[3])
        dep[1]+=1

    if line[5]!='' and line[5]!='ARR_TIME':
        arrtime[0]+=float(line[5])
        arrtime[1]+=1

    if line[6]!='' and line[6]!='ARR_DELAY':
        arr[0]+=float(line[6])
        arr[1]+=1

    if line[7]!='' and line[7]!='CRS_ELAPSED_TIME':
        crselap[0]+=float(line[7])
        crselap[1]+=1

    if line[8]!='' and line[8]!='ACTUAL_ELAPSED_TIME':
        actelap[0]+=float(line[8])
        actelap[1]+=1

    if line[9]!='' and line[9]!='AIR_TIME':
        air[0]+=float(line[9])
        air[1]+=1

    if line[0]=='OP_CARRIER_FL_NUM':
        print('001',' '.join(line).strip())
    else:
        print(','.join(line).strip())

dep=dep[0]/dep[1];arr=arr[0]/arr[1]

deptime=deptime[0]/deptime[1]
arrtime=arrtime[0]/arrtime[1]
crselap=crselap[0]/crselap[1]
actelap=actelap[0]/actelap[1]
air=air[0]/air[1]

print('000',deptime,dep,arrtime,arr,crselap,actelap,air)


    


    

        