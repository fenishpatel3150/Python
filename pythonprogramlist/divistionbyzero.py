def zero(a,b):
    try:
        result=a/b
        print(result)
    except ZeroDivisionError:
        print("the by zero opetion is not correct")

num1 = int(input("Enter the value :"))
num2 =int(input("Enter the avlue :"))

zero(num1,num2)