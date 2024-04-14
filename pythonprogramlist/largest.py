num = input("Enter the array :")

array = list(map(int, num.split()))
max = array[0]
for i in array:
    if i > max:
        max = i;
print("Largest number :",max)