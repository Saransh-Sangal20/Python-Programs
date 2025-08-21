n = int(input("Enter value of n: "))
a = 0
b = 1
print("Fibonacci numbers upto", n, "are")
for i in range (1,n+1):
    print(a, end = " ")
    c = a + b
    a = b
    b = c