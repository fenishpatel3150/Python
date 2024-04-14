def root(n):
    if(n==0 or n==1):
        return n
    i=1
    root=1
    while(root<=n):
        i+=1
        root=i*i
    return i-1

num =int(input("Enter the value :"))
print(root(num))