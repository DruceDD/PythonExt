# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину
# прямоугольника и встройте контроль недопустимых значений
# (отрицательных).
# Используйте декораторы свойств.

class Rectangle:
    def __init__(self, side_a: float, side_b: float = None):
        self.__side_a = float(side_a)
        if side_b == None:
            self.__side_b = side_a
        else:
            self.__side_b = float(side_b)

    @property
    def side_a(self):
        return self.__side_a

    @side_a.setter
    def side_a(self, value):
        if value > 0:
            self.__side_a = value
        else:
            raise ValueError('Недопустимое значение(отрицательное или нулевое)!')

    @property
    def side_b(self):
        return self.__side_b

    @side_b.setter
    def side_b(self, value):
        if value > 0:
            self.__side_b = value
        else:
            raise ValueError('Недопустимое значение(отрицательное или нулевое)!')

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
    rect_1.side_a = 10
    print(rect_1.side_a)
