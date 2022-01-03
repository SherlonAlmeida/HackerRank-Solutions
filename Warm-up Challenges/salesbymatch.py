#!binpython3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar)
    # Write your code here
    d = {} #dictionary to count the socks
    total = 0

    #The runtime complexity is O(n)
    for i in range(n)
        print(d)
        #Add in dictionary
        if ar[i] in d
            d[ar[i]] += 1
        else
            d[ar[i]] = 1
        
        #Sum the total number of socks
        if (d[ar[i]] != 0) and (d[ar[i]]%2==0)
            total += 1
    
    return total

if __name__ == '__main__'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + 'n')

    fptr.close()
