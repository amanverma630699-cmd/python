l=list(map(int,input("enter the list").split()))
target=int(input("the number :"))
for i in range(len(l)):
  for j in range(i+1,len(l)):
    if l[i]+l[j]==target:
      print(f"the Addition of two element for a list to find traget  value is :", i,j)
    if l[i]-l[j]==target:
      print(f"the Subtraction of two element for a list to find traget  value is :", i,j)
    if l[i]*l[j]==target:
      print(f"the Multiplication of two element for a list to find traget  value is :", i,j)
    if l[i]+l[j]==target:
      print(f"the Division of two element for a list to find traget  value is :", i,j)
else:
   print("no other match has benen found match has been found")


