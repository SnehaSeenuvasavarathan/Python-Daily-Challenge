#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    s=s.replace(" ","")
    n=math.sqrt(len(s))
    r=math.floor(n)
    c=math.ceil(n)

    while (r*c < len(s)):
        r+=1
    ns=[]
    rc=0
    cc=c
    for i in range(r):
        if cc>len(s):
            ns.append(s[rc:])
        else:
            ns.append(s[rc:cc])
            rc=cc
            cc+=c
    
    result=['']*c
    for i in range(r):
        for j in range(len(ns[i])):
            result[j]+=ns[i][j]
    return ' '.join(result)  

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
