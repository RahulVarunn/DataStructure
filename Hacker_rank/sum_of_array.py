# Given an array of integers, find the sum of its elements.
# For example, If the array ar = [1,2, 3]., 1+2+3 6, so return 6.
# Function Description
# Complete the simpleArraySum function in the editor below. It must return the sum of the array elements as an
# integer.
# simpleArraySum has the following Parameter(s);
# ar: an array of integers
# Input Format
# The first line contalns an integer, 7, denoting the size of the array.
# The second line contains n space-separated Integers representing the array's elements.
# Constraints
# 0<7, arl< 1000
# Output Format
# Print the sum of the array's elements as a single integer.











import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#
#[1 ,2 ,3 ,4 ,10 ,11]
def simpleArraySum(ar):
 
    temp=0  
    for i in ar:
        temp=temp+i
         
    return temp
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
