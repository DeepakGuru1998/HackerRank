#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    sum = math.fsum(arr) 
    mean = sum/len(arr)
    sd = 0
    for x in arr:
        sd += math.pow(x-mean,2)
    sd=math.sqrt(sd/len(arr))
    ans= "{:.1f}".format(sd)
    print(ans)
        
    
if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
