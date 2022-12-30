import math
import os
import random
import re
import sys

def lonelyinteger(a):
    # Sort the list in ascending order
    a = sorted(a)

    # Check for the lonely integer by iterating through the list
    for i in range(0, len(a), 2):
        # If we reach the end of the list, return the last element
        if i == len(a) - 1:
            return a[i]
        # If the current element is not equal to the next element, return it
        elif a[i] != a[i+1]:
            return a[i]
    # If no lonely integer is found, return None
    return None

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
    


'''Alternatively, there is a more efficient way to define lonelyinteger, such 
that you pass through the array once and keep track of any recurring integers.'''

def lonelyinteger(a):
    # Create a dictionary to count the occurrences of each element in the list
    counts = {}
    for i in a:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1

    # Iterate through the dictionary and return the first element with a count of 1
    for i, count in counts.items():
        if count == 1:
            return i

    # If no lonely integer is found, return None
    return None

















