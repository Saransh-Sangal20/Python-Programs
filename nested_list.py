n = int(input("Enter total number of pairs: "))
lst1 = []
for i in range(2*n):
    lst2 = []
    name = input("Enter name: ")
    age  = int(input("Enter age: "))
    lst2.append(name)
    lst2.append(age)
    lst1.append(lst2)
print("Nested list is:", lst1)
