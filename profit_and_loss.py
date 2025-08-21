cp =int(input("Enter cost price: "))
sp = int(input("Enter selling price: "))
if (sp>cp):
    profit = sp-cp
    print("Profit of", profit, "is made")
elif (cp>sp):
    loss = cp-sp
    print("Loss of", loss, "is made")
else:
    print("No profit or loss is made")