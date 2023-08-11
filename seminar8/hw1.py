# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# 1. Для дочерних объектов указывайте родительскую директорию.
# 2. Для каждого объекта укажите файл это или директория.
# 3. Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных
# файлов и директорий.

import os
import json
import csv
import pickle


def traverse_directory(directory):
    json_results = []
    csv_results = []
    pickle_results = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            file_type = 'file'

            json_results.append({'path': file_path, 'type': file_type, 'size': file_size})
            csv_results.append([file_path, file_type, file_size])
            pickle_results.append((file_path, file_type, file_size))

        for dir in dirs:
            dir_path = os.path.join(root, dir)
            dir_size = sum(os.path.getsize(os.path.join(dir_path, file)) for file in os.listdir(dir_path) if
                           os.path.isfile(os.path.join(dir_path, file)))
            dir_type = 'directory'

            json_results.append({'path': dir_path, 'type': dir_type, 'size': dir_size})
            csv_results.append([dir_path, dir_type, dir_size])
            pickle_results.append((dir_path, dir_type, dir_size))

    with open('results.json', 'w') as json_file:
        json.dump(json_results, json_file)

    with open('results.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(csv_results)

    with open('results.pickle', 'wb') as pickle_file:
        pickle.dump(pickle_results, pickle_file)


traverse_directory('/Users/Druce/Desktop/hwtest')
