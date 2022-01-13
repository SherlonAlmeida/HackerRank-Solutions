#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    m = {}
    
    for w in magazine:
        if w in m:
            m[w] += 1
        else:
            m[w] = 1

    N = len(note)
    for i in range(N):
        #print(w, m)
        w = note[i]
        if (w not in m) or (m[w] <= 0):
            return "No"
        else:
            if m[w] > 0:
                m[w] -= 1
    return "Yes"

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    result = checkMagazine(magazine, note)
    print(result)
