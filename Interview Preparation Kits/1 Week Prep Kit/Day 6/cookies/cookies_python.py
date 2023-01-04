from heapq import heapify, heappush, heappop

def cookies(k, A):
    
    heapify(A)
    result = 0
    
    # main logic
    while True:
        x = heappop(A)
        
        if x >= k:
            return result
        
        if A:
            y = heappop(A)
            s = x + 2 * y
            heappush(A, s)
            result += 1
            
        else:
            return -1
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()