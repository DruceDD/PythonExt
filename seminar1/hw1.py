# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

a = int(input("Введите сторону треугольника a: "))
b = int(input("Введите сторону треугольника b: "))
c = int(input("Введите сторону треугольника c: "))
if (a + b > c and b + c > a and a + c > b):
    print("Треугольник с такими сторонама существует")
    if (a == b == c):
        print("и является равносторонним")
    elif (a == b != c or b == c !=a or a == c !=b):
        print("и является равнобедренным")
    else:
        print("и является разносторонним")
else:
    print("Треугольника с такими сторонама не существует!")