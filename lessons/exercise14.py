# 11-1
# city

from city_functions import cit_country
import unittest
class CitiesTestCase(unittest.TestCase):
    def test_cit_country(self):
        wichitaUS = cit_country('Wichita', 'United States')

        self.assertEqual(wichitaUS, 'Wichita, United States')
# 11-2 modify the functions, so it uses a 3rd parameter. it should fail. then make it so it is optional.
# write a second test called test_city_country_population()
# that calls your function with the values 'santiago' 'chile' and population=5000000

    def test_city_country_population(self):
        santiagoCL = cit_country('santiago', 'chile', population=5000000)

        self.assertEqual(santiagoCL, 'Santiago, Chile, population 5000000')


    if __name__ == '__main__':
        unittest.main()

#11-3 Employee Write a class called employee.
# The __init__() method should take ina a first anme and a last name
# and an annual_annual_salary and store each of these as attributes
# write a method
# called give_raise adding $5000 to the annual annual_annual_salary.

from employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.Kostner = Employee('Kostner', 'David', 65000)

    def test_give_default_raise(self):
        self.Kostner.give_raise()
        self.assertEqual(self.Kostner.annual_salary, 70000)

    def test_give_custom_raise(self):
        self.Kostner.give_raise(10000)
        self.assertEqual(self.Kostner.annual_salary, 75000)

if __name__ == '__main__':
    unittest.main()