class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print('WOOOF')


rex = Dog()

rex.walk()
