import datetime

class Person:
    '''This is called a DOCSTRING which is an documentation of a class'''

    def __init__(self, first_name, last_name, dob, height, weight):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.height = height
        self.weight = weight

    def calculate_age(self):
        current_year = current_year = datetime.datetime.now().year
        return current_year - self.dob
    
    def print_name(self):
        print(f'{self.last_name}, {self.first_name}')

    def eat(self, food):
        print(f'{self.first_name} eats {food}! Yum yum!')


    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        else:
            if self.dob == other.dob and self.first_name == other.first_name and self.last_name == other.last_name:
                return True
        return False
    
    def __str__(self):
        return f'First Name: {self.first_name}. Last Name: {self.last_name}. Age: {self.calculate_age()}'
    
    def __repr__(self):
        return f'Class: Person. First Name: {self.first_name}. Last Name: {self.last_name}. Height: {self.height}. Weight: {self.weight}. DOB: {self.dob}. Age: {self.calculate_age()}'

    
kaba = Person("Emmanuel", "Kaba", 2000, 175, 70)

# kaba_age = kaba.calculate_age()
# print(kaba_age)
# kaba.print_name()
# kaba.eat("acheke")

emmanual = Person("Emmanuel", "Kaba", 2000, 175, 70)
cindy = Person("Cindy", "Achiri", 2000, 160, 50)

print(emmanual)

# print(repr(emmanual))