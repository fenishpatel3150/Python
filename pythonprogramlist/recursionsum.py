def sum(n):
    if n==0:
        return 0
    return(n%10+sum(int(n/10)))

num =int(input("Enter the value :"))
result =sum(num)
print(result)