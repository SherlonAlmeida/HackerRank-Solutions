#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(n, c):
    #The runtime complexity is O(n)
    minJumps = 0
    i = 0
    while i < (n-2):
        if (c[i+1] == 0) and ((c[i+2] == 0)):
            i += 2
            minJumps += 1
        elif (c[i+1] == 0) and (c[i+2] == 1):
            i += 1
            minJumps += 1
        elif (c[i+1] == 1):
            i += 2
            minJumps += 1
        #print(i)
    #Considering that the player wins always, if the current position is the n-2 index, so the next (last) position is always 0. Thus is necessary to increase the jumps in 1.
    if i == (n-2):
        i += 1
        minJumps += 1
    return minJumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
