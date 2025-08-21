num = int(input("Enter a number: "))
if (num>0):
    if(num>99 and num<1000):
        print("Three digit number")
    else:
        print("Not a three digit number")
else:
    print("Invalid Input")