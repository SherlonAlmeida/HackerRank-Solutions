#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(n, q):
    d = [0 for i in range(n)]
    sum = 0; flag = 0;
    for i in range(n):
        d[i] = q[i] - i - 1
        if d[i] > 2:
            flag = 1
            break
        for j in range(max(q[i]-2, 0), i):
            if q[j] > q[i]:
                sum += 1    
    #print(n, q, d)
    
    if flag == 1:
        return 0
    return sum

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        q = list(map(int, input().rstrip().split()))
        result = minimumBribes(n, q)
        if result == 0:
            print("Too chaotic")
        else:
            print(result)