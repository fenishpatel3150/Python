def palidrom(string):

    if (string==string[::-1]):
        print("This palidrom")
    else:
        print("This not palidrom")
        
string = input("Enter the string :")

print(palidrom(string))