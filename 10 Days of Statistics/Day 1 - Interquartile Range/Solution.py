#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    arr=[]
    for i,j in zip(values,freqs):
        temp = j*[i]
        arr.extend(temp)
    
    arr.sort()
    length = len(arr)
    
    if len(arr) % 2 == 0:
        L = arr[:int(length/2)]
        U = arr[int(length/2):]
    else:
        L = arr[:math.floor(length/2)]
        U = arr[math.ceil(length/2):]
        
    if len(L) %2 == 0:
        q1 = (L[int(len(L)/2) - 1] + L[int(len(L)/2)]) / 2
        q3 = (U[int(len(U)/2) - 1] + U[int(len(U)/2)]) / 2
        qr = q3-q1
        qr= "{:.1f}".format(qr)
        print(qr)
    else:
        q1 = L[int(len(L)/2)]
        q3 = U[int(len(U)/2)]
        qr = q3-q1
        qr= "{:.1f}".format(qr)
        print(qr)


if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
