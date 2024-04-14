num1 =input("Enter the 1 array :")
array1 = list(map(int, num1.split()))

num1 = list(dict.fromkeys(num1))
print(num1)