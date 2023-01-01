def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 1
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed + 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)
 
    
''' Here is the debugged version, where only 3 lines are altered to make the 
code work. No lines are added or removed'''
    
def findZigZagSequence(a, n):
    a.sort()
    mid = n//2 # This code actually finds the true halfway point
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2 # Need to move over to switch the next value
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1 # end minus one, there is no plus one

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)
