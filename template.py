class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
    @property  
    def full_name(self):
        return self.name + ' ' + self.surname
    
    @full_name.setter
    def full_name(self, new):
        self.name, self.surname = new.split(' ')
        
    @full_name.deleter
    def full_name(self):
        print('Удаление имени и фамилии')
        self.name = None
        self.surname = None

tom = Person('Sergey', 'Jkovlew')
print(tom.name)
print(tom.full_name)

tom.full_name = 'larik Jkovleskii'
print(tom.name)
print(tom.surname)
del tom.full_name
print(tom.name, tom.surname)