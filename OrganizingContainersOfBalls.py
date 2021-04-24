#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    
    # Write your code here
    noOfcontainers=len(container)
    noOfTypes=len(container[0])
    conCap=[0]*noOfcontainers
    typeVal=[0]*noOfTypes
    for i in range(len(container)):
        conCap[i]=sum(container[i])
        for j in range(noOfTypes):
            typeVal[i]+=container[j][i]
    for i in typeVal:
        if i not in conCap:
            return 'Impossible'
    return 'Possible'
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
