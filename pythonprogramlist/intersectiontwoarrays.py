num1 =input("Enter the 1 array :")
num2= input("Enter the 2 array :")
array1 = list(map(int, num1.split()))
array2 =list(map(int, num2.split()))

intersection =[ x for x in array1 if x in array2]
print(intersection)