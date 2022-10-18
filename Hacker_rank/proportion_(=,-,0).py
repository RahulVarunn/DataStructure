#!/bin/python3

# Given an array of integers, calculate the ratlos of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with 6 places after the
# decimal.
# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to 10 are acceptable
# Example
# arr = |1,1,0,-1,-1
# There are n5 elements, two postive, two negative and one zero. Their ratios are=0.400000, 0.400000 and 0.200000. Results are printed as:
# 400000
# 40006
# .2 200000
# Function Description
# Complete the plusMinus function in the editor below.
# plusMinus has the following parameter(s):
# int arrlnt an array of integers
# Print
# Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with 6 digits after the decimal. The function should not return
# value.
# Input Format
# The first line contains an integer, n, the size of the array.
# The second line contains n space-separated Integers that describe arr|n|.
# Constraints
# 0<n 100
# -100 arrlil < 100
# Output Format
# Print the following 3 lines, each to6 decimals




import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positive=0
    negative=0#
    zero=0
    n=len(arr)
    for i in arr:
        if i>0:
            positive=positive+1
        elif i<0:
            negative=negative+1
        elif i==0:
            zero=zero+1
    print("{}\n{}\n{}".format(positive/n,negative/n,zero/n))
        
    
        
    
    
arr=[-4, 3, -9, 0, 4, 1]
plusMinus(arr)
