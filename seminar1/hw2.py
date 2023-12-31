# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

num = int(input("Введите число от 2 до 100 000 для проверки: "))
if num <= 1 or num >= 100000:
    print("Введенное число не входит в заданный диапозон!")
else:
    count = 0
    for i in range(2, num // 2 + 1):
        if (num % i == 0):
            count = count + 1
    if (count == 0):
        print("Число является простым")
    else:
        print("Число является составным")