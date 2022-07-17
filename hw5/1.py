#завантажити використовуючи requests структуру даних з
#https://dummyjson.com/todos
#та вивести на екран не виконані значення todo з тих даних, які до вас прийшли

import requests


url = "https://dummyjson.com/todos"
response = requests.get(url)
todos = response.json()

for todo in todos["todos"]:
    if not todo['completed']:
        print(todo['todo'])
