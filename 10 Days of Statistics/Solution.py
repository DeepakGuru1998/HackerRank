#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    # Write your code here
    arr.sort()
    length = len(arr)

    if len(arr) % 2 == 0:
        L = arr[:int(length/2)]
        U = arr[int(length/2):]
        q2 = (arr[int(length/2) - 1] + arr[int(length/2)]) / 2
	
    else:
        L = arr[:math.floor(length/2)]
        U = arr[math.ceil(length/2):]
        q2 = arr[math.floor(length/2)]

    if len(L) %2 == 0:
        q1 = (L[int(len(L)/2) - 1] + L[int(len(L)/2)]) / 2
        q3 = (U[int(len(U)/2) - 1] + U[int(len(U)/2)]) / 2
        return (int(q1),int(q2),int(q3))
        
    else:
        q1 = L[int(len(L)/2)]
        q3 = U[int(len(U)/2)]
        return (int(q1),int(q2),int(q3))
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
