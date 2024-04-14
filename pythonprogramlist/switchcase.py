def Adittion(num1,num2):
    return num1+num2
def substraction(num1,num2):
    return num1-num2
def divistion(num1,num2):
    return num1/num2
def multiple(num1,num2):
    return num1*num2
def default(num1,num2):
    return "Incorrect day "

switcher={
    1:Adittion,
    2:substraction,
    3:divistion,
    4:multiple,
}

def switch(opetion,num1,num2):
    return switcher.get(opetion,default)(num1,num2)

print('''
    1:Adittion,
    2:substraction,
    3:divistion,
    4:multiple,
      ''')

choice = int(input("Enter the Number :"))
num1 =int(input("Enter the value :"))
num2 =int(input("Enter the value : "))

print(switch(choice,num1,num2))