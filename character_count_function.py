def char_count(str1):
    dict = {}
    for i in str1:
        if (i in dict):
            continue
        else:
            count = str1.count(i)
            dict[i] = count
    return dict
str1 = input("Enter a string: ")
result = char_count(str1)
print(result)