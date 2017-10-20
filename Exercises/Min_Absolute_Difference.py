#!/bin/python3

import sys

def minimumAbsoluteDifference(n, arr):
    # Complete this function
    arr.sort()
    # We define this value just by checking the problem description, in this case:     x<=1000000000
    me=1000000000
    for i in range(n-1):
        dif=abs(arr[i+1]-arr[i])
        if dif<me:
            me=dif
    return me



if __name__ == "__main__":
    number = int(input().strip())
    array = list(map(int, input().strip().split(' ')))
    result = minimumAbsoluteDifference(number, array)
    print(result)


# 10
# -59 -36 -13 1 -53 -92 -2 -96 -54 75

# 1
