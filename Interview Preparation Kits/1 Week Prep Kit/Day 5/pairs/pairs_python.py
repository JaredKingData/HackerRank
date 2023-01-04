from collections import Counter

def pairs(k, arr):
    d = Counter(arr)
    pairs = 0
    
    # main logic
    for i in arr:
        if i+k in d:
            pairs += 1
        if i-k in d:
            pairs += 1
        del d[i]
        
    return pairs
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()