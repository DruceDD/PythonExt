# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные  варианты и выведите 4 успешных расстановки.

from random import randint as rnd

def is_valid_queens(queens):
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1] or \
               abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                return False
    return True

queens = []
queens_true1 = [(6, 8), (4, 7), (7, 6), (1, 5), (8, 4), (2, 3), (5, 2), (3, 1)]
queens_true2 = [(5, 8), (2, 7), (4, 6), (7, 5), (3, 4), (8, 3), (6, 2), (1, 1)]
queens_true3 = [(8, 8), (7, 3), (6, 1), (5, 6), (4, 2), (3, 5), (2, 7), (1, 4)]
queens_true4 = [(8, 6), (7, 4), (6, 7), (5, 1), (4, 8), (3, 2), (2, 5), (1, 3)]

for i in range(8):
    while True:
        x = rnd(1, 8)
        y = rnd(1, 8)
        if (x, y) not in queens:  # Проверка, что место не занято
            queens.append((x, y))
            print(x, y)
            break

print('\nСлучайный вариант:', queens, '\nПроверка:', is_valid_queens(queens))

print('\nВерный вариант №1:', queens_true1, '\nПроверка:', is_valid_queens(queens_true1))
print('\nВерный вариант №2:', queens_true2, '\nПроверка:', is_valid_queens(queens_true2))
print('\nВерный вариант №3:', queens_true3, '\nПроверка:', is_valid_queens(queens_true3))
print('\nВерный вариант №4:', queens_true4, '\nПроверка:', is_valid_queens(queens_true4))