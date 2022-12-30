# Use this if the array has an odd number of elements:

def findMedian(arr):
    arr.sort()
    n = len(arr) //2
    return arr(n)


# Use this if the array has an even number of elements:
def findMedian(arr):
    arr.sort()
    n = len(arr) // 2
    if len(arr) % 2 == 0:
        # If the number of elements is even, return the average of the two middle elements
        return (arr[n-1] + arr[n]) / 2
    else:
        # If the number of elements is odd, return the middle element
        return arr[n]