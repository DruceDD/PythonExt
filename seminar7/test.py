import os


def rename_files():
    directory = input("Введите путь к каталогу: ")
    desired_name = input("Введите желаемое имя файла: ")
    num_digits = int(input("Введите количество цифр в порядковом номере: "))
    source_extension = input("Введите исходное расширение файлов: ")
    target_extension = input("Введите конечное расширение файлов: ")
    check_save_old_name = input("Нужно ли сохранить часть старого имени?\n1 - да\n2 - нет\n")
    if check_save_old_name == 1:
        name_range_start = int(input("Введите начало промежутка сохраняемого оригинального имени: "))
        name_range_end = int(input("Введите конец промежутка сохраняемого оригинального имени: "))
        name_range = [name_range_start, name_range_end - 1]

        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.endswith(source_extension)]

        for i, file in enumerate(files):
            name, extension = os.path.splitext(file)

            if name_range:
                name = name[name_range[0]-1:name_range[1]+1]

            new_name = desired_name + '_' + name + '_' + str(i).zfill(num_digits) + target_extension
            os.rename(os.path.join(directory, file), os.path.join(directory, new_name))

    else:
        files = [f for f in os.listdir(directory) if
                 os.path.isfile(os.path.join(directory, f)) and f.endswith(source_extension)]

        for i, file in enumerate(files):
            name, extension = os.path.splitext(file)


            new_name = desired_name + '_' + str(i).zfill(num_digits) + target_extension
            os.rename(os.path.join(directory, file), os.path.join(directory, new_name))


rename_files()