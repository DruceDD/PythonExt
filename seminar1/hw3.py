# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint
num = randint(0, 1000)

for i in range(1, 11):
    # print(num)
    user_num = int(input("Введите число в диапозоне от 0 до 1000: "))
    if user_num >= 0 and user_num <= 1000:
        if i < 10:
            if user_num < num:
                print(f"Загаданное число больше вашего! Число оставшихся попыток {10-i}!")
            elif user_num > num:
                print(f"Загаданное число меньше вашего! Число оставшихся попыток {10 - i}!")
            elif user_num == num:
                print(f"Вы угадали заганное число за {i} попыток!")
                break
        else:
            print(f"Вам не удалась отгадать загаданое число - {num}!")
            break
    else:
        print(f"Указаное число не входит в диапозон! Число оставшихся попыток {10 - i}!")