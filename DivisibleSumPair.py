#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    
    x=[0 for _ in range(k)]
    
    ct=0
    for i in ar:
        i=i%k
        r=k-i if i!=0 else 0
        ct+=x[r]
        x[i]+=1

        
    return ct    
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
