# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.


def keys_to_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if not isinstance(key, (str, int, float, bool)):
            key = str(key)
        result[value] = key
    return result


print(keys_to_dict(arg1='value1', arg2='value2', arg3='value3'))