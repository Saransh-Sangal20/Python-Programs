dict = {"warrior": "योद्धा", "brave": "साहसी", "courage": "साहस", "strength": "शक्ति", "battle": "युद्ध",}
word = input("Enter the word you want to translate: ")
if (word in dict):
    hindi = dict[word]
    print(word, "=", hindi)
else:
    print(word, "not in dictionary")