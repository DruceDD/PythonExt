# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании экземпляра.
# У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.

class Rectangle:
    def __init__(self, side_a: int, side_b: int = None):
        self.side_a = side_a
        if side_b == None:
            self.side_b = side_a
        else:
            self.side_b = side_b

    def get_perim(self) -> int:
        return 2 * (self.side_a + self.side_b)

    def get_square(self) -> int:
        return self.side_a * self.side_b



rect_1 = Rectangle(2, 3)
rect_2 = Rectangle(5)
print(rect_1.get_perim())
print(rect_1.get_square())
print(rect_2.get_perim())
print(rect_2.get_square())