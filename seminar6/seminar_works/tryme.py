from random import randint as rnd
START = 0
STOP = 100
AMOUNT = 10


def get_random_num(start: int, end: int, amount = AMOUNT):
    flag = False
    num = rnd(start, end)
    while amount > 0:
        num_user = int(input('Введите число: '))
        if num_user == num:
            print('Вы угадали!')
            flag = True
            break
        elif num_user < num:
            print('Больше!')
            amount -= 1
        else:
            print('Меньше!')
            amount -= 1

    return flag


data = input('Введите начало диапозона и конец через пробел: ')
start, stop = map(int, data.split())
print(get_random_num(start, stop))