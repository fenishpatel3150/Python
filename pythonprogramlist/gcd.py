def gcd(a,b):
    if b==0:
        return 1
    else:
        return gcd(b,a%b)

a =int(input("Enter the value :"))
b =int(input("Enter the value :"))

print(gcd(a,b))