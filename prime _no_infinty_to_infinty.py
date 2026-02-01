#Print numbers from infinty to infinty using a for loop
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for num in range(start, end + 1):
    if num>1:
        Nreminder=0
        for i in range(1,num+1):
            if num%i==0:
                Nreminder+=1
        if Nreminder==2:
            print(num,end="  ")