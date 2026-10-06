class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        return f"{self.name} говорит гав!"
    def info(self):
        return f"{self.name}, {self.age} года."
rex = Dog("Рекс", 3)
bobik = Dog("Бобик", 5)
print(rex.bark())
print(rex.age)
print(bobik.bark())
print(bobik.age)
print(bobik.info())