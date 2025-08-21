def inches_to_cm(inches):
    cm = inches * 2.54
    return cm
inches = float(input("Enter length in inches: "))
cm = inches_to_cm(inches)
print("Length in cm is", cm)