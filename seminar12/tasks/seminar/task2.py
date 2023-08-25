# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.

from collections import deque
import json


class Factorial:
    def __init__(self, k):
        self._history = deque(maxlen=k)

    def __call__(self, number: int):
        mul_num = 1
        for i in range(2, number + 1):
            mul_num *= i
        self._history.append({number: mul_num})
        return mul_num

    def show_history(self):
        return self._history

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        data = {}
        while self._history:
            data.update(self._history.popleft())
        with open('task2.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file)


if __name__ == '__main__':
    fact = Factorial(5)
    with fact as f:
        print(f(10))
        print(f(15))
        print(f(20))
        print(f.show_history())
