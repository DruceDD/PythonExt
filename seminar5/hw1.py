# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def split_path(full_path):
    file_parts = full_path.split("/")
    file_name = file_parts[-1]
    file_dir = "/".join(file_parts[:-1])
    file_name_parts = file_name.split(".")
    file_ext = "." + file_name_parts[-1]
    file_name = "".join(file_name_parts[:-1])
    return file_dir, file_name, file_ext


full_path = 'C:/example/cwd/test_dir/test_file.txt'
result = split_path(full_path)
print(result)