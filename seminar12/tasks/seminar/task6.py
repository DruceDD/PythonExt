# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину
# на дескриптор с валидацией размера.

class Descr:
    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.name, value)
        else:
            raise ValueError('Недопустимое значение(отрицательное или нулевое)!')


class Rectangle:
    side_a = Descr()
    side_b = Descr()

    def __init__(self, side_a: float, side_b: float = None):
        self.__side_a = float(side_a)
        if side_b == None:
            self.__side_b = side_a
        else:
            self.__side_b = float(side_b)

    def get_perim(self) -> float:
        return 2 * (self.__side_a + self.__side_b)

    def get_square(self) -> float:
        return self.__side_a * self.__side_b


class RectanglePro(Rectangle):
    def __add__(self, other):
        sum_of_perim: int = self.get_perim() + other.get_perim()
        side_a = self.__side_a + other.__side_a
        side_b = sum_of_perim / 2 - side_a
        return RectanglePro(side_a, side_b)

    def __sub__(self, other):
        if self.get_perim() < other.get_perim():
            self, other = other, self
        diff = self.get_perim() - other.get_perim()
        side_a = abs(self.__side_a - other.__side_a)
        side_b = diff / 2 - side_a
        return RectanglePro(side_a, side_b)

    def __eq__(self, other):
        return self.get_square() == other.get_square()

    def __gt__(self, other):
        return self.get_square() > other.get_square()

    def __le__(self, other):
        return self.get_square() <= other.get_square()


if __name__ == '__main__':
    rect_1 = RectanglePro(5, 10)
    rect_2 = RectanglePro(10, 20)
    print(rect_1.side_a)
    rect_2.side_b = 5
