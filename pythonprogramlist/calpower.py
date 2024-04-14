def calculator(a,b):
    p=1
    for i in range(1,a+1):
        p=p*a
    return p

a = int(input("Enter the value :"))
b= int(input("Enter the value :"))
print(calculator(a,b))