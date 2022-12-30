import math
import os
import random
import re
import sys

def plusMinus(arr):
    pos_count, neg_count, zero_count = 0, 0, 0
    for i in range(0, len(arr)):
        if arr[i] > 0:
            pos_count = pos_count + 1
        elif arr[i] < 0:
            neg_count = neg_count + 1
        else:
            zero_count = zero_count + 1
            
    print(pos_count/len(arr))
    print(neg_count/len(arr))
    print(zero_count/len(arr))
    
if __name__ == '__main__':
    
    arr = list(map(int, input().rstrip().split()))
    
    plusMinus(arr)
