class Bird():
    def __init__(self, name, voice, color):
        self.name = name
        self.voice = voice
        self.color = color

    def fly(self):
        print(f'{self.name} летает')

    def eat(self):
        print(f'{self.name} ест')

    def sing(self):
        print(f"{self.name} поет- чирик")

    def info(self):
        print(f"Имя: {self.name}")
        print(f"Голос: {self.voice}")
        print(f"Цвет: {self.color}")

    def walk(self):
        print(f"{self.name} гуляет")
class Pigeon(Bird):
    def __init__(self, name, voice, color,favorite_food):
        super().__init__(name, voice, color)
        self.favorite_food = favorite_food

    def sing(self):
        print(f"{self.name} поет- курлык курлык")


bird1 = Pigeon(name = "Гоша", voice = "курлык", color ="серый", favorite_food = "Хлебные крошки")
bird2 = Bird(name ="Маша", voice = "чирик", color = "белый")

bird2.sing()
bird2.info()
bird2.walk()