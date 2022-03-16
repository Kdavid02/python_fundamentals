# 9-6 Write a class named IceCreamStand that inherits from the Restaurant class in 9-1
# There should be an attribute called flavors that stores a list of flavors.
# call the method and create an instance.

class Restaurant():
    def __init__(self, name, cuisine_type,):
        self.number_served = 0
        self.name = name
        self.cuisine_type = cuisine_type

    def open_restaurant(self):
        msg = f"{self.name} is open."
        print(f"\n{msg}")

    def describe_restaurant(self):
        msg=f"{self.name} makes {self.cuisine_type}"
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, add_served):
        self.number_served += add_served

class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type='ice_cream'):
        self.flavors = []
        super().__init__(name, cuisine_type)
    def show_flavors(self):
        print("\nThere are these flavors")
        for flavor in self.flavors:
            print({flavor.title()})

dairy_king = IceCreamStand("Dairy King")
dairy_king.flavors = ['strawberry', 'vanilla', 'cherry', 'lemon']
dairy_king.describe_restaurant()
dairy_king.show_flavors()

# 9-7 write a class called admin that inherits from the user class
class User():

    def __init__(self, first_name,last_name):
        self.login_attempts = 0
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"\nfirst name: {self.first_name.upper()} \nlast name: {self.last_name.upper()}")

    def greet_user(self):
        print(f"Hello, {self.first_name}")
# add login attempts for the users with a reset function as well that resets the attempts and test this
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name):

        super().__init__(first_name, last_name)
        self.privileges = Privileges()

# part of 9-7 before 9-8 was required to remove it.
#John = Admin('john', 'david')
#John.describe_user()
#John.privileges = ['add/remove users', 'add/remove passwords', 'can add new content']
#John.show_privileges()

Kostner = User('Kostner','David')
Kostner.describe_user()
Kostner.greet_user()

# 9-8 Have a seperate previleges class.
# The class should have one attribute, privileges that storers a list of strings
# move the show_privileges()


class Privileges():

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges-")
        if self.privileges:
            for privilege in self.privileges:
                print(f"{privilege}")
        else:
            print("No privileges found")

John = Admin('John', 'David')
John.describe_user()


john_privileges = ['add/remove users', 'add/remove passwords', 'can add new content']
John.privileges.privileges = john_privileges
John.privileges.show_privileges()


