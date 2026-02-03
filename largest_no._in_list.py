l=list(map(int,input("enterthe list:").split()))
for i in range(len(l)):
    if l[i]>l[0]:
        l[0]=l[i]   
print(f"the largest no. in the list is :{l[i]}")

