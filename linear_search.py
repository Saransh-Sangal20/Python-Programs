n = int(input("Enter size of list: "))
lst = []
print("Enter elements of list")
for i in range(n):
    element = int(input())
    lst.append(element)
print("Entered list is", lst)
x = int(input("Enter element to search: "))
check = 0
for i in range(n):
    if (lst[i]==x):
        check = 1
        break
if (check==1):
    print("Element found at index", i)
else:
    print("Element not found")