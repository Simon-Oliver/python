class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print('WOOOF')


class Cat(Mammal):
    def meow(self):
        print('Meow')


rex = Dog()
snowball = Cat()

rex.walk()
snowball.meow()
snowball.walk()
