student = {
    'Іван Петров': {
        'Пошта': 'Ivan@gmail.com',
        'Вік': 21,
        'Номер телефону': '+380987771221',
        'Середній бал': 95.8
    },
    'Женя Курич': {
        'Пошта': 'Geka@gmail.com',
        'Вік': 22,
        'Номер телефону': None,
        'Середній бал': 64.5
    },
    'Маша Кера': {
        'Пошта': 'Masha@gmail.com',
        'Вік': 18,
        'Номер телефону': '+380986671221',
        'Середній бал': 80
    },
}

new_student = {'Євген Кравченко': {
    'Пошта': 'Ievgen@gmail.com',
    'Вік': 38,
    'Номер телефону': '+380985678921',
    'Середній бал': 97
}
}
print(f"Adding new student {new_student}")
student.update(new_student)

print("Printing students' list with high marks")
for name in student.keys():
    if student[name]["Середній бал"] > 90:
        print(f'{name} {student[name]["Середній бал"]}')

print("Defining average mark")
total_mark = 0
for name in student.keys():
    total_mark += student[name]["Середній бал"]
average_mark = total_mark / len(student)
print(f"Average mark is {average_mark}")


print("Updating contacts")
for name in student.keys():
    if student[name]['Номер телефону'] is None:
        student[name]['Номер телефону'] = '+380981111111'
print(f"Updated students' list {student}")
