n = int(input("Enter number of elements in list: "))
lst = []
sum = 0
print("Enter the elements: ")
for i in range (n):
    num = int(input())
    lst.append(num)
    sum = sum + num
print("List is", lst)
print("Sum is", sum)