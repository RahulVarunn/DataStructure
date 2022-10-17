# An array Is a type of data structure that stores elements of the same type in a contiguous block f memory. In an
# array, A, of size N, each memory location has some unique index, i (where 0 i< N), that can be referen ced
# as Ali] or Aj.
# Reverse an array of integers.
# Note: If you've already solved our C++ domain's Arrays Introduction challenge, you may want to skip this.
# Example
# A = [1,2,3]
# Return 3, 2, 1.
# Function Description
# Complete the function reverseArray in the editor below.
# reverseArray has the following parameter(s):
# int An]: the array to reverse
# Returns
# Intn: the reversed array
# Input Format
# The first line contains an integer, N, the number of Integers in A.
# The second line contalns N space-separated Integers that make up A.
# Constraints
# 1N 10
# 1 A|] < 10*, where A[i]| is the i" integer in A





import math
import os
import random
import re
import sys


def reverseArray(a):
    arr=[]
    print(len)
    for i in range(len(a)-1,-1,-1):
        arr.append(a[i])
    
    return arr
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))#[1,2,3,4]

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
