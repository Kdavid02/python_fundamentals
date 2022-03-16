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

