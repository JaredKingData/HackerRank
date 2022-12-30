import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # If the time is 12:00:00AM, return 00:00:00
    if s[:2] == "12" and s[-2:] == "AM":
        return "00" + s[2:-2]
    # If the time is 12:00:00PM, return 12:00:00
    elif s[:2] == "12" and s[-2:] == "PM":
        return s[:-2]
    # If the time is AM and the hours part is less than 10, add a leading zero to the hours part
    elif s[-2:] == "AM" and int(s[:2]) < 10:
        return "{:02d}".format(int(s[:2])) + s[2:-2]
    # If the time is PM, add 12 to the hours part
    else:
        ans = int(s[:2])
        if s[-2:] == "PM":
            ans += 12
        # Return the modified time with a leading zero if the hours part is less than 10
        return "{:02d}".format(ans) + s[2:-2]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()