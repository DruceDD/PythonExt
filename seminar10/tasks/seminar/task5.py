# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.

class Fish:
    def __init__(self, name: str, color: str, size: float, max_depth: float):
        self.name = name
        self.color = color
        self.size = size
        self.max_depth = max_depth

    def show_max_depth(self):
        print(self.max_depth)

class Bird:
    def __init__(self, name: str, color: str, size: float, habitat: str):
        self.name = name
        self.color = color
        self.size = size
        self.habitat = habitat

    def show_habitat(self):
        print(self.habitat)

class Cat:
    def __init__(self, name: str, color: str, size: float, hairy: bool):
        self.name = name
        self.color = color
        self.size = size
        self.hairy = hairy

    def show_hairy(self):
        print(self.hairy)

if __name__ == '__main__':
    fish = Fish('Flounder', 'orange', 10.2, 15.0)
    fish.show_max_depth()
    bird = Bird('Chichi', 'white', 82.3, 'forest')
    bird.show_habitat()
    cat = Cat('Tom', 'black and white', 11, True)
    cat.show_hairy()