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

