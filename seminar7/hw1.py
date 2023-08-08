# Напишите функцию группового переименования файлов. Она должна:
#   1. принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
#   2. принимать параметр количество цифр в порядковом номере.
#   3. принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
#   4. принимать параметр расширение конечного файла.
#   5. принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано.
# Далее счётчик файлов и расширение.

import os


def rename_files():
    directory = input("Введите путь к каталогу: ")
    desired_name = input("Введите желаемое имя файла: ")
    num_digits = int(input("Введите количество цифр в порядковом номере: "))
    source_extension = input("Введите исходное расширение файлов: ")
    target_extension = input("Введите конечное расширение файлов: ")
    name_range_start = int(input("Введите начало промежутка сохраняемого оригинального имени: "))
    name_range_end = int(input("Введите конец промежутка сохраняемого оригинального имени: "))
    name_range = [name_range_start, name_range_end - 1]

    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.endswith(source_extension)]

    for i, file in enumerate(files):
        name, extension = os.path.splitext(file)

        if name_range:
            name = name[name_range[0]-1:name_range[1]+1]

        new_name = desired_name + name + '_' + str(i).zfill(num_digits) + target_extension
        os.rename(os.path.join(directory, file), os.path.join(directory, new_name))


rename_files()