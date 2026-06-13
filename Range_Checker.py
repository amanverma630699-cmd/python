# Read input
num = int(input())
low = int(input())
high = int(input())

# Check and print
if num in range(low, high):
    print("In range")
else:
  print("Out of range")