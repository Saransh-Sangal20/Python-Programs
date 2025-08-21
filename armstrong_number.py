dno = int(input("Enter number of digits in the number: "))
num = int(input("Enter the number: "))
ogno = num
sum = 0
while (num!=0):
    ld = num%10
    sum = sum + (ld**dno)
    num = num // 10
if (sum==ogno):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")