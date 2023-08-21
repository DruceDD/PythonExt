# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь

from task3 import Human, Gender
from random import randint as rnd

class Employee(Human):
    MAX_LEVEL = 7
    MIN_ID = 100_000
    MAX_ID = 999_999

    def __init__(self, name: str, patr_name: str, last_name: str, age: int, gender: Gender, emp_id: int):
        super().__init__(name, patr_name, last_name, age, gender)
        if self.MIN_ID <= emp_id <= self.MAX_ID:
            self.emp_id = emp_id
        else:
            self.emp_id = rnd(self.MIN_ID, self.MAX_ID)


    def get_level(self) -> int:
        nums_of_id = sum(int(n) for n in str(self.emp_id))
        return nums_of_id % self.MAX_LEVEL


emp1 = Employee('Bob', '---', 'Johnson', 27, Gender.male, 777_777)
print(emp1.get_level())
print(hash(emp1))
emp2 = Employee('Bob', '---', 'Johnson', 27, Gender.male, 777_777)
print(emp2.get_level())
print(hash(emp2))