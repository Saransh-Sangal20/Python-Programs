def remove_word(lst, word):
    lst1 = []
    for i in lst:
        if (word in i):
            if (word == i):
                continue
            else:
                lst1.append(i.strip(word))
        else:
            lst1.append(i)
    return lst1
lst = eval(input("Enter a list: "))
word = input("Enter word to remove: ")
print(remove_word(lst, word))