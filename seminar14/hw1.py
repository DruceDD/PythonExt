# from seminar13.hw1 import Rectangle, InvalidSideLengthError

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

## tests:

# 1 - doctest:

import doctest

def test_invalid_side_length_error():
    """
    >>> rect_1 = Rectangle(5, -3)
    Traceback (most recent call last):
        ...
    InvalidSideLengthError: Invalid side length: -3
    """
    pass

def test_get_perim():
    """
    >>> rect_1 = Rectangle(5, 3)
    >>> rect_1.get_perim()
    16
    """
    pass

def test_get_square():
    """
    >>> rect_1 = Rectangle(5, 3)
    >>> rect_1.get_square()
    15
    """
    pass

if __name__ == "__main__":
    doctest.testmod()

# 2 - unittest:

import unittest

class TestRectangle(unittest.TestCase):
    def test_invalid_side_length_error(self):
        rect_1 = Rectangle(5, -3)
        self.assertRaises(InvalidSideLengthError, rect_1.get_perim)

    def test_get_perim(self):
        rect_1 = Rectangle(5, 3)
        self.assertEqual(rect_1.get_perim(), 16)

    def test_get_square(self):
        rect_1 = Rectangle(5, 3)
        self.assertEqual(rect_1.get_square(), 15)

if __name__ == "__main__":
    unittest.main()

# 3 - pytest:

import pytest

def test_invalid_side_length_error():
    rect_1 = Rectangle(5, -3)
    with pytest.raises(InvalidSideLengthError):
        rect_1.get_perim()

def test_get_perim():
    rect_1 = Rectangle(5, 3)
    assert rect_1.get_perim() == 16

def test_get_square():
    rect_1 = Rectangle(5, 3)
    assert rect_1.get_square() == 15

if __name__ == "__main__":
    pytest.main()