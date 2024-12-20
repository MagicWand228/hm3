class Owner:
    def __init__(self, name, dog):
        self.name = name
        self.dog = dog  

    def feed_dog(self, food):
        print(f"{self.name} годує {self.dog.name}")
        self.dog.eat(food)

    def take_dog_for_walk(self):
        print(f"{self.name} виводить {self.dog.name} погуляти")
        self.dog.play()