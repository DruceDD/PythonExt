class InvalidSideLengthError(Exception):
    def __init__(self, side_length):
        self.side_length = side_length

    def __str__(self):
        return f"Invalid side length: {self.side_length}"


class Rectangle:
    def __init__(self, side_a: int, side_b: int = None):
        if side_a <= 0 or (side_b is not None and side_b <= 0):
            raise InvalidSideLengthError(side_a if side_b is None else side_b)
        self.side_a = side_a
        if side_b is None:
            self.side_b = side_a
        else:
            self.side_b = side_b

    def get_perim(self) -> int:
        return 2 * (self.side_a + self.side_b)

    def get_square(self) -> int:
        return self.side_a * self.side_b

rect_1 = Rectangle(5, -3)
print(rect_1.get_perim())
print(rect_1.get_square())