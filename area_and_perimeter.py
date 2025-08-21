length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))
area = length * breadth
perimeter = 2 * (length + breadth)
print("Area is", area)
print("Perimeter is", perimeter)
if (area>perimeter):
    print("Area is greater than perimeter")
else:
    print("Perimeter is greater than area")