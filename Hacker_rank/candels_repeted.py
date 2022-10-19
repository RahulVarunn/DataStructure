#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    n=candles[0]
    coun=0
    for i in range(len(candles)):
        if n<candles[i]:
            n=candles[i]
            coun=1
        elif n==candles[i]:
            coun+=1
    return coun
        


candles = [1,2,3,3,6]
print(birthdayCakeCandles(candles))


