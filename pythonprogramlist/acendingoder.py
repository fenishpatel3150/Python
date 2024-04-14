num = input("Enter the array :")
array = list(map(int,num.split()))
swap = 0;

for i in range(0,len(array)):
    print(array[i],end=" ");
    

for i in range(0,len(array)):
    for j in range(i+1,len(array)):
        if(array[i]>array[j]):
            swap = array[i];
            array[i]=array[j];
            array[j]=swap;
print();


for i in range(0,len(array)):
    print(array[i],end=" ");
    



