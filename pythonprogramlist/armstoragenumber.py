num1 =int(input("Enter the numbr :"))

temp=0
sum=0

while temp>0:
    digit=temp%10
    sum+= digit**3
    temp//=10

if num1 ==sum:
    print(num1,"Armstorage")
else:
    print(num1,"not Armstorage ")