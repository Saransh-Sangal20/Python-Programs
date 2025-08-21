radius = int(input("Enter radius of circle: "))
print("1. Calculate Area of Circle")
print("2. Calculate Perimeter of Circle")
ans = int(input("Enter your option: "))
if (ans==1):
    area = 3.14*radius*radius
    print("Area of circle is", area)
else:
    perimeter = 2*3.14*radius
    print("Perimeter of circle is", perimeter)