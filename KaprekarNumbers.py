#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    # Write your code here
    ct=0
    
    for i in range(p,q+1):
        val=i**2
        l=len(str(i))
        div=10**l
        res=(val//div)+(val%div)
        if res==i:
            print(i, end=' ')
            ct+=1
    if ct==0:
        print('INVALID RANGE')
            
if __name__== '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
