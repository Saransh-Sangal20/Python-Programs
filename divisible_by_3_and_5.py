num = int(input("Enter a number: "))
if (num>0):
    if (num%3==0 and num%5==0):
        print("Divisible by 3 and 5")
    else:
        print("Not divisible by 3 and 5")
else:
    print("Invalid Input")