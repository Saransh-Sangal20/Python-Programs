def longest_word(lst1):
    lword = len(lst1[0])
    for i in lst1:
        if (lword < len(i)):
            lword = len(i)
    for i in lst1:
        if (lword == len(i)):
            return i
lst1 = eval(input("Enter a list: "))
word = longest_word(lst1)
print("Longest word is", word)