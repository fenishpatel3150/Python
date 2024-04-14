def circle(n):
    ans=1
    if(n>0):
        ans=3.14*n*n
        return ans
    
num = int(input("Enter the value: "))
print(circle(num))