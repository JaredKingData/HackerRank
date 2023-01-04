def isBalanced(s):
    stack = []
    bracket = {'{': '}', '(': ')', '[': ']'}
    
    for char in s:
        if char in ['{', '(', '[']:
            stack.append(char)
        else:
            # if brackets are present
            if stack:
                top = stack.pop()
                if bracket[top] != char:
                    return 'NO'
            # stack is empty
            else:
                return 'NO'
            
    return 'NO' if stack else 'YES'
            