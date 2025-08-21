def recursive_factorial(n):
    if (n==1 or n==0):
        return 1
    else:
        fact = n * recursive_factorial(n-1)
    return fact
n = int(input("Enter the value of n: "))
fact = recursive_factorial(n)
print("Factorial is", fact)