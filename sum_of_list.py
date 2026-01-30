l=list(map(int,input("enter the list").split()))
target=int(input("the number :"))
for i in range(len(l)):
  for j in range(i+1,len(l)):
    if l[i]+l[j]==target:
      print(i,j)
else:
   print("no other match has benen found match has been found")


