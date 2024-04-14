num1 =int(input("Enter the value :"))
reverce=0   

while num1!=0:
    digit=num1%10
    reverce=reverce*10+digit
    num1//=10
    
print("reverce :" + str(reverce))