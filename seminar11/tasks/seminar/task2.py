# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра

class Archive:
    """
    Хранит пару свойств
    """
    _instance = None

    def __init__(self, text: str, num: int):
        print('Init')
        # print(self.__name__)
        self.text = text
        self.num = num

    def __new__(cls, *args, **kwargs):
        """
        Добавляет строки и номера в списки
        """
        print('New')
        # print(cls.__name__)
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.num_archive = []
            cls._instance.text_archive = []
        else:
            cls._instance.num_archive.append(cls._instance.num)
            cls._instance.text_archive.append(cls._instance.text)
        return cls._instance

    def __str__(self):
        return (f'We have text: {self.text} and number: {self.num}\n'
                f'Archive of text: {Archive._instance.text_archive}\n'
                f'Archive of nums: {self.num_archive}')

    def __repr__(self):
        return f'We have text: {self.text} and number: {self.num}'

elem1 = Archive('text1', 12)
elem2 = Archive('text2', 1)
elem3 = Archive('text3', 5)

print(Archive._instance.num_archive)
print(Archive._instance.text_archive)

# print(Archive.__new__.__doc__)

print(elem1)
print(repr(elem1))