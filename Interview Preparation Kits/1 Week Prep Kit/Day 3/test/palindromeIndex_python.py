# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 16:05:13 2022

@author: 15414
"""
# define Palendrome Index
def palindromeIndex(s):
    # check if string is palindrome
    if s == s[::-1]:
        return -1

    n = len(s)
    # main logic
    for i in range(n//2):
        # check if first and last are different
        if s[i] != s[n-1-i]:
            if s[i+1:n-i] == s[i+1:n-i][::-1]:
                return i
            elif s[i:n-1-i] == s[i:n-1-i][::-1]:
                return n-1-i
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
