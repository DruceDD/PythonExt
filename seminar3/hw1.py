# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

list_1 = [1, 2, 1, 4, 6, 4, 7, 4, 7]  # новый лист должен быть [1, 4, 7]
list_2 = []
for value in list_1:
    if list_1.count(value) > 1 and value not in list_2:
        list_2.append(value)
print(list_2)