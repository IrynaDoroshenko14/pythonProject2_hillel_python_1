# Зформуйте строку, яка містить певну інформацію про символ в відомому слові. Наприклад "The [номер символу] symbol
# in [тут слово] is '[символ з відповідним порядковим номером]'". Слово та номер отримайте за допомогою input() або
# скористайтеся константою. Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in "Python" is 't' ".

word = input("Enter word: ")
index_str = input("Enter index: ")

if not index_str.isdigit():
    print("Index is not number.")
elif int(index_str) > len(word):
    print("Index too big.")
elif int(index_str) < 1:
    print("Index less than 1.")
else:
    index = int(index_str)
    output = f"The {index} symbol in '{word}' is '{word[index-1]}'"
    print(output)
