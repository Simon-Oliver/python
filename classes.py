class Animal:
    species = ''
    name = ''
    age = 0

    def __init__(self, s, n, a):
        self.species = s
        self.name = n
        self.age = a

    def talk(self, words):
        print(self.name, words)


dog = Animal('Dog', 'Rex', '5')

print(dog.name, dog.age)
dog.talk('wooof')

class Working_Animal(Animal):
    job = ''

    def __init__(self, s, n, a, j):
        self.job = j


police_dog = Working_Animal('Dog', 'Max', '8', 'Police Dog')

print(police_dog.job)