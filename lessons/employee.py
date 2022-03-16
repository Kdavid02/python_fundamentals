#11-3 Write a class called employee. The __init__() method should take ina a first anme and a last name
# and an annual_salary and store each of these as attributes
#write a method called give_raise adding $5000 to the annual annual_salary.

class Employee():
    def __init__(self, first_name, last_name, annual_salary):
        self.first = first_name
        self.last = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        self.annual_salary += amount