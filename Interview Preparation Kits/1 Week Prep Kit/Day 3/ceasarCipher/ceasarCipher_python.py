import math
import os
import random
import re
import sys

def caesarCipher(s, k):
    # ascii values for characters
    temp = []
        
    # convert char to ascii value
    for char in s:
        temp.append(ord(char))
            
    # main logic - shifting
    for i in range(len(temp)):
        # uppercase - 65 - 90
        if 65 <= temp[i] <= 90:
            temp[i] = (65 + (temp[i] - 65 + k) % 26)
            
        # lowercase - 97 - 122
        elif 97 <= temp[i] <= 122:
            temp[i] = (97 + (temp[i] - 97 + k) % 26)
            
    return "".join(map(chr,temp))     
        
        
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()