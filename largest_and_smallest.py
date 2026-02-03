#smallest and largest from infinty to infinty using a for loop
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
l=[]
for i in range(start, end + 1):
    l.append(i)
print(l)
print("The largest number is:", max(l))
print("The smallest number is:", min(l))