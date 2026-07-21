class cat:
    def __init__(self):
        self.name = "Cat"

    def sound(self):
        print("Meow")

class dog:
    def __init__(self):
        self.name = "Dog"

    def sound(self):
        print("Bark")

animals = [cat(), dog()]
for animal in animals:
    animal.sound()
    