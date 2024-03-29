# Візьміть гру з заняття і доопрацюйте її наступним чином:
# всі функції в окремий файл
# додайте підказки привгадуванні
# (якщо різниця між числом користувача і загаданим більше 10 - вивести "Холодно",
# якщо 5-10 - "Тепло", якщо 1-4 "Гаряче")
# додайте можливість на початку програми вказати кількість спроб вгадування.
# користувач має вгадати число за вказану кількість спроб
# Напишіть декоратор, який вимірює і виводить на екран час виконання функції
# в секундах і задекоруйте ним основну функцію гри. Після закінчення гри декоратор
# має сповістити, скільки тривала гра.

# from hw9.functions import g
from hw9.functions import get_attempts, get_random_number, get_number_from_user, show_hint, check_numbers, duration


@duration
def game():
    attempts = get_attempts()
    number_to_guess = get_random_number()

    for _ in range(attempts):
        user_number = get_number_from_user()
        show_hint(number_to_guess, user_number)
        if check_numbers(number_to_guess, user_number):
            print('You WIN!!!!')
            break
    else:
        print('You lost')


if __name__ == '__main__':
    game()
