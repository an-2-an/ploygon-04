# INCAPSULATION

class Boy:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return f'{self.__name} is {self.__age} years old'

    def __repr__(self):
        return f'<Boy: {self.__name}, {self.__age}>'

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_age(self):
        return self.__age

    def __grow_a_year(self):
        self.__age += 1

    def grow(self, years):
        for _ in range(years):
            self.__grow_a_year()

if __name__ == '__main__':
    boy1 = Boy(name='Misha', age=17)
    print(boy1)
    # print(boy1.__name)
    print(boy1.get_name())
    # boy1.name = 'Michael'
    boy1.set_name(new_name='Michael')
    print(boy1)
    # boy1.age = 18
    # boy1.__grow_a_year()
    boy1.grow(years=2)
    print(boy1)
