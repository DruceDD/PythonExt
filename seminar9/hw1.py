from random import randint as rnd
import math
import csv
import json


def find_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root
    else:
        return "No real roots"


def generate_csv(filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for i in range(100):
            row = [rnd(1, 100) for i in range(3)]
            writer.writerow(row)


def roots_decorator(func):
    def wrapper(filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                a, b, c = map(int, row)
                print(f"Roots of {a}x^2 + {b}x + {c}: {func(a, b, c)}")

    return wrapper


def save_to_json(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            data = {
                "parameters": args,
                "result": result
            }
            with open(filename, 'a') as file:
                file.write(json.dumps(data) + '\n')
            return result

        return wrapper

    return decorator


@roots_decorator
@save_to_json("result.json")
def find_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root
    else:
        return "No real roots"


generate_csv("data.csv")
find_roots("data.csv")
