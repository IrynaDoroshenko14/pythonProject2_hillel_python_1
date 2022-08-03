from random import randint
from datetime import datetime


def get_attempts():
    while True:
        try:
            return int(input('Enter attempts count: '))
        except:
            print('It\'s not int')


def get_random_number():
    """
    Returns:
        (int)
    """
    number = randint(1, 101)
    return number


def get_number_from_user():
    """
    Returns:
        (int)
    """
    while True:
        try:
            return int(input('Enter int: '))
        except:
            print('It\'s not int')


def check_numbers(to_guess, user_number):
    """

    Args:
        to_guess (int):
        user_number (int):

    Returns:
        (bool):
    """
    print(f'---> {to_guess}')
    if to_guess == user_number:
        return True
    else:
        return False


def show_hint(to_guess, user_number):
    if abs(to_guess - user_number) > 10:
        print("Cold")
    elif 5 < abs(to_guess - user_number) <= 10:
        print("Warm")
    else:
        print("Hot")


def duration(func):
    def wrapper(*args, **kwargs):
        before = datetime.now()
        func(*args, **kwargs)
        after = datetime.now()
        print(after - before)
    return wrapper
