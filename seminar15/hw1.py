import logging
import argparse

logging.basicConfig(level=logging.INFO)  # Настройка логгера для вывода информации в консоль
logger = logging.getLogger(__name__)

class InvalidSideLengthError(Exception):
    def __init__(self, side_length):
        self.side_length = side_length

    def __str__(self):
        return f"Invalid side length: {self.side_length}"


class Rectangle:
    def __init__(self, side_a: int, side_b: int = None):
        if side_a is None or side_a <= 0 or (side_b is not None and side_b <= 0):
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rectangle parameters")
    parser.add_argument("--side_a", type=int, help="Length of side A")
    parser.add_argument("--side_b", type=int, help="Length of side B (optional)")
    args = parser.parse_args()

    if args.side_a is None:
        side_a = int(input("Enter the length of side A: "))
    else:
        side_a = args.side_a

    if args.side_b is None:
        side_b = int(input("Enter the length of side B (optional): "))
    else:
        side_b = args.side_b

    try:
        rect_1 = Rectangle(side_a, side_b)
        logger.info(f"Perimeter: {rect_1.get_perim()}")
        logger.info(f"Square: {rect_1.get_square()}")
    except InvalidSideLengthError as e:
        logger.error(e)