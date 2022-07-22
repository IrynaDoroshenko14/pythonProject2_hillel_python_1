# 1 Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент,
# перетворений на float. Якщо перетворити не вдається функція має повернути 0.


def to_float(value):
    try:
        float_value = float(value)
        print(f"{value} converted to {float_value}")
        return float_value
    except ValueError:
        print(f"Couldn't convert {value}, returned 0")
        return 0


# 2 Напишіть функцію, що приймає два аргументи. Функція повинна
# a аргументи відносяться до числових типів (int, float) - повернути перемножене значення цих аргументів,
# b якщо обидва аргументи це строки - обʼєднати в одну строку та повернути
# c якщо перший строка, а другий ні - повернути dict де ключ це перший аргумент, а значення - другий
# d у будь-якому іншому випадку повернути кортеж з цих аргументів


def my_num(val_1, val_2):
    if isinstance(val_1, (int, float)) and isinstance(val_2, (int, float)):
        return val_1 * val_2
    elif isinstance(val_1, str) and isinstance(val_2, str):
        return val_1 + val_2
    elif isinstance(val_1, str) and not isinstance(val_2, str):
        return {val_1: val_2}
    else:
        return val_1, val_2
