a = int(input("Enter the value "))

if a == 1:
    print(a,"is not prime number")
elif a > 1:
    b = False
    for i in range(2,a):
        if a % i==0:
            b=True
        break
if b:
    print(a,"is not prime number")
else:
    print(a,"is a prime number")
    