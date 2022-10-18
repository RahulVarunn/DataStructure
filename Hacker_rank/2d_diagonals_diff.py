#!/bin/python3



# Given a square matrix, calculate the absolute difference between the sums of its dlagonals.
# For example, the square matrix arr is shown below:
# 123
# 4 5 6
# 989
# The left-to-right diagonal =1+5+9= 15. The right to left diagonal = 3 + 5+9 = 17. Thelr absolute
# difference is |15 - 17| = 2.
# Function description
# Complete the diagonalDyference function in the editor below.
# dlagonalDifference takes the following parameter
# int arrln]lm; an array of integers
# Return
# int: the absolute diagonal difference
# Input Format
# The first line contains a single integer, , the number of rows and columns In the square matrix arr.
# Each of the next n lines describes a row, arrli], and consists of n space-separated integers arr|i||i|
# Constraints
# -100 arr|i||i| s 100
# Output Format
# Return the absolute difference between the sums of the matrix's two diagonals as a single Integer.














import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    dig_1=0
    dig_2=0
    for i in range(len(arr)):
        dig_1+=arr[i][i]
        dig_2+=arr[i][len(arr)-i-1]
        
    return abs(dig_1-dig_2)
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
