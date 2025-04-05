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

    
kaba = Person("Emmanuel", "Kaba", 2000, 175, 70)

kaba_age = kaba.calculate_age()
print(kaba_age)