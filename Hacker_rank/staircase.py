
#!/bin/python3


# Staircase detail
# This is a stalrcase of size n= 4:
# #
# ###"
# Its base and helght are both equal to 7n. It is drawn using # symbols and spaces. The last line is not preceded by any spaces.
# Write a program that prints a stalrcase of slze n.
# Function Description
# Complete the staircase function in the editor below.
# staircase has the following parameter(s):
# int m an integer
# Print
# Print a staircase as described above.
# Input Format
# A single Integer, n, denoting the size of the staircas.
# Constraints
# 0n100
# Output Format
# Printa stalrcase of size n using # symbols and spaces.
# Note: The last line must have 0 spaces in it.
# Sample Input









import math
import os
import random
import re
import sys


def staircase(n):
    for i in range( 1 ,n+1):
        print(" "*(n-i) + '#'*i)        



staircase(6)




