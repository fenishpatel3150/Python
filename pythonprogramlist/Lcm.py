def lcm(a,b):
    num=0
    if a>b:
        num=a
    else:
        num=b
    
    while(True):
        if(num%a==0 and num%b==0):
            comlcm=num
        break
    num+=1
    return comlcm

num1=int(input('enter the first number:'))
num2=int(input('enter the second number:'))

print(lcm(num1,num2))