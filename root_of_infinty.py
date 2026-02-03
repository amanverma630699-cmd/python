#Even numbers from infinty to infinty using a for loop
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
root=int(input("Enter the number to find the root: "))


for num in range(start, end + 1):
        print(num**root,end="  ")