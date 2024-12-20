from dog import Dog
from owner import Owner

dog1 = Dog(name="Собачий Вбивця", breed="Чіхуахуа", age=5)

owner1 = Owner(name="Валерій", dog=dog1)

owner1.feed_dog(20)  
owner1.take_dog_for_walk()  
owner1.take_dog_for_walk() 
dog1.bark() 