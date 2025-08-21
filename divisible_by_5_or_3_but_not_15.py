num = int(input("Enter a number: "))
if (num>0):
    if(num%3==0 or num%5==0):
        if(num%15!=0):
            print(num, "is divisible by 3 or 5 but not 15")
        else:
            print(num, "is divisible by 3 or 5 and 15")
    else:
        print(num, "is not divisible by 3 or 5")
else:
    print("Invalid Input")