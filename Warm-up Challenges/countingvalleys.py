#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # The runtime complexity is O(steps)
    montains = 0
    valleys  = 0
    sea_lvl  = 0

    isValley = True
    totalValleys = 0

    for i in range(steps):
        #Check if is a Valley ( <= sea level )
        if sea_lvl < 0 and isValley:
            isValley = False
            totalValleys += 1
        
        #Increase | Decrease the sea level
        if path[i] == 'U':
            sea_lvl += 1
        else:
            sea_lvl -= 1
        
        #If is the end of a valley, looks for other valley
        if sea_lvl == 0:
            isValley = True
        
        #print(path[i], sea_lvl)
    
    return totalValleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
