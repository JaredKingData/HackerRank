def superDigit(n, k):
    def helper(n):
        total = 0
        for num in n:
            total += int(num)
        total = str(total)
        if len(total) == 1:
            return total
        else: 
            return helper(total)
    
    p = str(helper(n) * k)
    return helper(p)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()