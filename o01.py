class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self, n):
        print(f'{self.name} says: ' + 'Woof! ' * n)

    def __str__(self):
        return f'{self.breed} {self.name}'

    def __repr__(self):
        return f'<Dog object (name={self.name}, breed={self.breed})>'

if __name__ == '__main__':
    dog1 = Dog(name='Max', breed='pitbull')
    print(dog1)
    dog1.bark(n=3)
    dog2 = Dog(name='Woolfy', breed='shepherd')
    print(dog2)
    # print(repr(dog2))
    dogs = [dog1, dog2]
    print(dogs)