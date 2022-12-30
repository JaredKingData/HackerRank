import math
import os
import random
import re
import sys

def diagonalDifference(arr):
  # Initialize the sums of the two diagonals
  sum1 = 0
  sum2 = 0

  # Iterate over the rows and columns of the matrix
  for i in range(len(arr)):
    for j in range(len(arr[i])):
      # If the element is on the main diagonal, add it to sum1
      if i == j:
        sum1 += arr[i][j]
      # If the element is on the secondary diagonal, add it to sum2
      if i + j == len(arr) - 1:
        sum2 += arr[i][j]

  # Return the absolute difference between the two diagonal sums
  return abs(sum1 - sum2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
