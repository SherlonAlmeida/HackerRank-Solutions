#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    #Initially, a hash table is created and its size is 26. Its function map is given by the ascII code.
    deletions = 0
    begin = ord('a')
    end   = ord('z')
    hash_size = end-begin+1
    letters_a = [ 0 for i in range(hash_size)]
    letters_b = [ 0 for i in range(hash_size)]
    n_a = len(a)
    n_b = len(b)

    #Here, the arrays of letters are populated
    for i in range(n_a):
        index = ord(a[i])-begin
        letters_a[index] += 1
    for i in range(n_b):
        index = ord(b[i])-begin
        letters_b[index] += 1
    
    #Now, a simple subtraction allows to identify the necessary deletions.
    for i in range(hash_size):
        deletions += abs(letters_a[i] - letters_b[i]) #here the complexity time is constant O(26), thus it is not considered in the total complexity

    #Thus, the runtime complexity is O(|a| + |b|)

    #print(letters_a)
    #print(letters_b)
    return deletions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
