#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#

def workbook(n, k, arr):
    # Write your code here
    generator=pg=1
    ct=0
    for i in arr:
        t=i
        if t>0 and t<k:
            if pg in [item for item in range(1,t+1)]:
                ct+=1
            pg+=1
        else:
            while(t>0 and t>=k):
                t-=k
                generator+=k
                if pg in [item for item in range(generator-k, generator)]:
                    ct+=1
                pg+=1
            
            if t>0 and t<k:
                if pg in [item for item in range(i-t+1,i+1)]:
                
                    ct+=1
                    print(i,ct,pg)
                pg+=1
        generator=1
    return ct

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
