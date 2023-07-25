# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

import itertools

things_for_travel = {'Палатка': 5,
                     'Спальный мешок': 2,
                     'Каремат(коврик)': 1,
                     'Еда': 4,
                     'Посуда': 2,
                     'Аптечка': 3,
                     'Теплая одежда': 7,
                     'Вода': 5,
                     'Дождевик': 1
                     }

max_weight_of_backpack = int(input('Введите максимальную грузоподъёмность рюкзака: '))

take_things = []

for i in range(1, len(things_for_travel) + 1):
    for variation in itertools.combinations(things_for_travel.items(), i):
        sum_of_weight = sum([things_for_travel[1] for things_for_travel in variation])
        if sum_of_weight <= max_weight_of_backpack:
            take_things.append(dict(variation))

for option in take_things:
    print(option)