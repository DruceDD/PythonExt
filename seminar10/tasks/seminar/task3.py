# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.

from enum import Enum

class Gender(Enum):
    male = 'male'
    female = 'female'

class Human:
    def __init__(self, name: str, patr_name: str, last_name: str, age: int, gender: Gender):
        self.name = name
        self.patr_name = patr_name
        self.last_name = last_name
        self._age = age
        self.gender = gender

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def full_name(self) -> str:
        return f'{self.last_name} {self.name} {self.patr_name}'

if __name__ == '__main__':
    human1 = Human('Bob', '---', 'Johnson', 27, Gender.male)
    print(human1.get_age())
    human1.birthday()
    print(human1.get_age())
    print(human1.full_name())

    human2 = Human('Alice', '---', 'Windsor', 31, Gender.female)
    print(human2.get_age())
    human2.birthday()
    print(human2.get_age())
    print(human2.full_name())