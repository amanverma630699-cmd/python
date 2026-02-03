#evenand odd from infinty to infinty and there sum of list  using a for loop
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
l=[]
for i in range(start, end + 1):
    l.append(i)
print(l,"\n")
even=0
odd=0
e=[]
o=[]
for num in l:
    if num % 2==0:
        even+=1
        e.append(num)
    else:
        odd+=1
        o.append(num)
print(f"The even numbers in the list are:",e,"\n   ")
print(f"The number of  even number in list  is:",{even},"\n   ")
print("the sum fo all even number in list is :",sum(e),"\n   ")
print(f"The odd numbers in the list are:",o,"\n   ")
print(f"The number of  odd number in list  is:",{odd})
print("the sum fo all odd number in list is :",sum(o))
