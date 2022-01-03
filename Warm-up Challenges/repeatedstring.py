#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    #The complexity is O(|s|)
    numberOfa_once = 0
    N = len(s)
    for i in range(N):
        if s[i] == 'a':
            numberOfa_once += 1
    
    #Calculate the known repetition in O(1)
    numberOfa_ntimes = math.floor(n/N)*numberOfa_once

    #Calculate the last round of data in O(|s|)
    iterations = n - math.floor(n/N)*N

    #print(numberOfa_once, numberOfa_ntimes, iterations)
    
    for i in range(iterations):
        if s[i] == 'a':
            numberOfa_ntimes += 1
    return numberOfa_ntimes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
