import math 
print("the geranal quadratic equation form is [ ax^2 + bx +c ] ")
q1= int(input("the values of a in ax^2 is :"))
q2= int(input("the values of b in bx is :"))
q3= int(input("the values of c in c is :"))
# Python program to find roots of quadratic equation


# function for finding roots
def equationroots( q1, q2, q3): 

    # calculating discriminant using formula
    dis = q2 * q2- 4 * q1 * q3 
    sqrt_val = math.sqrt(abs(dis)) 
    
    # checking condition for discriminant
    if dis > 0: 
        print("real and different roots") 
        print((-q2 + sqrt_val)/(2 * q1)) 
        print((-q2 - sqrt_val)/(2 * q1)) 
    
    elif dis == 0: 
        print("real and same roots") 
        print(-q2 / (2 * q1)) 

if q1 == 0: 
        print("Input correct quadratic equation") 

else:
    print (equationroots(q1, q2, q3))