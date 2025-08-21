lst = []
n = int(input("Enter number of students: "))
print("Enter marks: ")
for i in range (n):
    marks = int(input())
    lst.append(marks)
lst.sort()
print(lst)