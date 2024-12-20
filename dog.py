class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        self.energy = 100  

    def bark(self):
        print(f"{self.name} Гав-гав!")

    def eat(self, food):
        self.energy += food
        if self.energy > 100:
            self.energy = 100
        print(f"{self.name} їсть, {self.name} отримує енергію {self.energy} ")

    def play(self):
        if self.energy >= 10:
            self.energy -= 10
            print(f"{self.name} грається енергії залишилось : {self.energy}")
        else:
            print(f"{self.name} собачка не має енергії, щоб грати")
