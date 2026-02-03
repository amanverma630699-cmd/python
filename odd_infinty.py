#Even numbers from infinty to infinty using a for loop
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for num in range(start, end + 1):
    if num%2!=0:
        print(num,end="  ")