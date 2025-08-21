num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))
num5 = int(input("Enter number 5: "))
div = int(input("Enter number to find multiple of: "))
count = 0
print("Multiples of", div, "are", end = " ")
if (num1%div==0):
    print(num1, end = " ")
    count+=1
elif (num2%div==0):
    print(num2, end = " ")
    count+=1
elif (num3%div==0):
    print(num3, end = " ")
    count+=1
elif (num4%div==0):
    print(num4, end = " ")
    count+=1
elif (num5%div==0):
    print(num5, end = " ")
    count+=1
print()
print("Total", count, "multiples of", div, "are found")