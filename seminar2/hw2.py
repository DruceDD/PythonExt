# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

import fractions


def find_lcm(x: int, y: int) -> int:
    if x > y:
        bigger = x
    else:
        bigger = y
    while True:
        if bigger % x == 0 and bigger % y == 0:
            lcm = bigger
            break
        bigger += 1
    return lcm


def get_fractions_from_user() -> [str, str]:
    data = input("Введите 2 дроби через пробел, например, 2/5 1/7: ")
    fraction_1, fraction_2 = data.split()
    return str(fraction_1), str(fraction_2)


def get_numerator_denominator_from_str(fraction: str) -> [int, int]:
    numerator, denominator = fraction.split("/")
    numerator = int(numerator)
    denominator = int(denominator)
    return numerator, denominator


def addition_of_fractions(fraction_1: str, fraction_2: str) -> str:
    numerator_1, denominator_1 = get_numerator_denominator_from_str(fraction_1)
    numerator_2, denominator_2 = get_numerator_denominator_from_str(fraction_2)
    if denominator_1 == denominator_2:
        if str(numerator_1 + numerator_2) == str(denominator_1):
            result = "Сумма дробей: " + fraction_1 + " + " + fraction_2 + " = " + str(
                (numerator_1 + numerator_2) // denominator_1)
        else:
            result = "Сумма дробей: " + fraction_1 + " + " + fraction_2 + " = " + \
                     str(numerator_1 + numerator_2) + "/" + str(denominator_1)
        return result
    else:
        lsm = find_lcm(denominator_1, denominator_2)
        if str((numerator_1 * (lsm // denominator_1)) + (numerator_2 * (lsm // denominator_2))) == str(lsm):
            result = "Сумма дробей: " + fraction_1 + " + " + fraction_2 + " = " + \
                     str(((numerator_1 * (lsm // denominator_1)) + (numerator_2 * (lsm // denominator_2))) // lsm)
        else:
            result = "Сумма дробей: " + fraction_1 + " + " + fraction_2 + " = " + \
                     str((numerator_1 * (lsm // denominator_1)) + (numerator_2 * (lsm // denominator_2))) + "/" + str(
                lsm)
        return result


def multiplication_of_fractions(fraction_1: str, fraction_2: str) -> str:
    numerator_1, denominator_1 = get_numerator_denominator_from_str(fraction_1)
    numerator_2, denominator_2 = get_numerator_denominator_from_str(fraction_2)
    if (denominator_1 * denominator_2) % (numerator_1 * numerator_2) == 0:
        result = "Произведение дробей: " + fraction_1 + " * " + fraction_2 + " = " + \
                 str((numerator_1 * numerator_2) // (numerator_1 * numerator_2)) + "/" + str((denominator_1 * denominator_2) // (numerator_1 * numerator_2))
    else:
        result = "Произведение дробей: " + fraction_1 + " * " + fraction_2 + " = " + \
             str(numerator_1 * numerator_2) + "/" + str(denominator_1 * denominator_2)
    return result


fraction1, fraction2 = get_fractions_from_user()
print(addition_of_fractions(fraction1, fraction2))
print(multiplication_of_fractions(fraction1, fraction2))

num_1, denom_1 = get_numerator_denominator_from_str(fraction1)
num_2, denom_2 = get_numerator_denominator_from_str(fraction2)
res1 = fractions.Fraction(num_1, denom_1)
res2 = fractions.Fraction(num_2, denom_2)
print(f"\nПроверка с помощью модуля 'fractions': \n\tСумма дробей = {res1 + res2} \n\t"
      f"Произведение дробей = {res1 * res2}")
