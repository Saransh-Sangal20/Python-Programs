def recursive_sum(n):
    if (n==1):
        return 1
    else:
        sum = n + recursive_sum(n-1)
    return sum
n = int(input("Enter value of n: "))
sum = recursive_sum(n)
print("Sum is", sum)