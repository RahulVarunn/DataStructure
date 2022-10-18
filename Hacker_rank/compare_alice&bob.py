#!/bin/python3
# Allce and Bob each created one problem for Hacker Rank. A revlewer rates the two challenges, awardin8 points on
# a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.
# The rating for Alice's challenge is the triplet a = (a[0], a[1], a[2]), and the rating for Bob's challenge Is the triplet b =
# (b[O], b[T], D[2]).
# The task is to find their comparison points by comparling a[0] with b[o], af1] with b[1], and a[2] with b[2].
# If a> b[I, then Allce is awarded 1 point.
# If a<b[I, then Bob Is awarded1 point.
# f a=b[I, then nelther person recelves a point.
# Comparison points is the total points a person earned.
# Given a and b, determine thelr respective comparison points.
# Example
# a = [1,2,3]
# b=B,2,11
# For elements *0*, Bob is awarded a point because a[o].
# For the equal elements af1] and b[1], no points are earned.
# Finally, for elements 2, a[2] > b[2] so Allce recelves a point.
# The return array is [1, 1] with Alice's score first and Bob's second.
# Function Description
# Complete the function compareTriplets in the editor below.
# compareTriplets has the following parameter(s):
# int a[3]: Alice's challenge rating
# Int b3]: Bob's challenge rating
# Return
# int[2]: Alice's score is in the first position, and Bob's score is in the second.
# Input Format
# The first llne contalns 3 space-separated integers, a[0], a[1], and a[2], the respective values in triplet a.
# The second line contains 3 space-separated integers, b[o], b[1], and b[2], the respective values in triplet b.



import math
import os
import random
import re
import sys



def compareTriplets(a, b):
    # Write your code here
    score=[0,0]#0,1
    
    for i,j in zip(a,b):
        if i>j:
            score[0]=score[0]+1
        elif i<j:
            score[1]=score[1]+1
    
    return score
            
a=[5, 6, 7] #alice
b=[3, 6, 10]  #bob        
print(compareTriplets(a,b))       
            
     




