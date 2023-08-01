# Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


n = int(input('Введите количество чисел Фибоначчи: '))
fib = fibonacci()
for i in range(n):
    print(next(fib))