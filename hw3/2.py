#Вести з консолі строку зі слів за допомогою input() (або скористайтеся константою).
# Напишіть код, який визначить кількість слів, в цих даних.

string = input("Enter string: ")
if len(string) == 0:
    print("0")
else:
    string_list = string.split(" ")
    print(len(string_list))
