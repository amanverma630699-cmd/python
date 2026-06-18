# nstructions
# Read a number N from input.

# Print every number from 1 to N, but:

# If the number is divisible by both 3 and 5, print FizzBuzz instead
# If the number is divisible by 3, print Fizz instead
# If the number is divisible by 5, print Buzz instead 
# Read input
# Read N
n = int(input())


for r in range(1,n+1):
 
     if r%5 ==0 and r%3==0:
           print("FizzBuzz")
     elif r%3==0:
           print("Fizz")
     elif r%5==0:
           print("Buzz")
     else:
           print(r)