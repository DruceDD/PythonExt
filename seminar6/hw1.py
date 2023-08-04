# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

def if_leap(year: int):
    return not (year % 4 != 0 or year % 100 == 0 and year % 400 != 0)

def check_date(str_date: str) -> bool:
    day, mon, year = map(int, str_date.split('.'))
    if not 1 <= day <= 31 and 1 <= mon <= 12 and 1 <= year <= 9999:
        return False

    if mon in (4, 6, 9, 11) and day > 30:
        return False

    if mon == 2 and if_leap(year) and day > 29:
        return False

    if mon == 2 and not if_leap(year) and day > 28:
        return False

    return True


date = input('Введите дату формата ДД.ММ.ГГГГ (разделитель - точка): ')
print(check_date(date))