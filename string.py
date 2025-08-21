string = input("Enter a string: ")
if (string.endswith("ion") == 1):
    string1 = string.replace("ion", "en")
    print(string1)
elif (len(string)<3):
    print(string)
else:
    print(string)