# Создайте класс студента.
# 1. Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# 2. Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# 3. Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# 4. Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.

import csv


class NameDescriptor:
    def __get__(self, instance, owner):
        return instance._name

    def __set__(self, instance, value):
        if not value.replace(" ", "").isalpha() or not value.istitle():
            raise ValueError("Неверное имя")
        instance._name = value


class Student:
    name = NameDescriptor()

    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade, test_result):
        if subject not in self.grades:
            self.grades[subject] = []
        self.grades[subject].append((grade, test_result))

    def get_average_grade(self, subject=None):
        if subject:
            if subject not in self.grades:
                return None
            total = 0
            count = 0
            for grade, _ in self.grades[subject]:
                total += grade
                count += 1
            return total / count
        else:
            total = 0
            count = 0
            for subject_grades in self.grades.values():
                for grade, _ in subject_grades:
                    total += grade
                    count += 1
            return total / count


class Subject:
    def __init__(self, name):
        self.name = name


def load_subjects_from_csv(file_path):
    subjects = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            subjects.append(Subject(row[0]))
    return subjects


subjects = load_subjects_from_csv("subjects.csv")
student = Student("Рябов Андрей Александрович")

student.add_grade("Математика", 5, 90)
student.add_grade("Математика", 5, 90)
student.add_grade("Физика", 4, 80)
student.add_grade("Физика", 5, 90)
student.add_grade("Химия", 3, 70)
student.add_grade("Химия", 3, 70)
student.add_grade("Русский", 3, 70)
student.add_grade("Русский", 4, 80)
student.add_grade("Английский", 5, 90)
student.add_grade("Английский", 4, 80)

print('Средний балл по всем предметам:', student.get_average_grade())  # Выводит средний балл по всем предметам
print('Средний балл по Математики:', student.get_average_grade("Математика"))  # Выводит средний балл по предмету "Math"
print('Средний балл по Физики:', student.get_average_grade("Физика"))
print('Средний балл по Химии:', student.get_average_grade("Химия"))
print('Средний балл по Русскому:', student.get_average_grade("Русский"))
print('Средний балл по Английскому:', student.get_average_grade("Английский"))
