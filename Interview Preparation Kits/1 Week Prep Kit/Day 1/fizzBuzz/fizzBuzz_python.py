# Define the function FizzBuzz, which takes any number n and tests whether it is divisible by three and five. If so, it prints "FizzBuzz". If it is only divisible by 3, it prints "Fizz", and if it is only divisible by 5, it prints "Buzz". If none of these options are true, it prints the number.
def fizzBuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
                
if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
