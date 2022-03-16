# 8-3 - 8.4 make a function that accepts the size and text of a message that should be printed on a shirt.
# 2 parameters that include a message and size of the shirt.
# Make a default value for message and size. 'I love python' and 'large'
def make_shirt(size='large', msg='I love Python'):
    print(f'Message will say, "{msg}"')
    print(f"Size of will be a {size} t-shirt.")


make_shirt('small', 'Test Message')
make_shirt(msg="Test Message2", )
make_shirt()

# 8-5 make a function describe_city() that accepts the city name and its country.
# There should be a default value for the country. It should print where the country and city is in a simple sentence.


def describe_city(city, country='United States of America'):
    message = f"{city} is in {country}."

    print(message)


describe_city('London, England')
describe_city('Wichita')
describe_city('Topeka')

# 8.9 make a list containing a series of short text messages. Then pass the list to a function call show_messages().

def show_messages(msgs):
    for msg in msgs:
        print(msg)


msgs = ["How are you?","Nice to meet you.","What are you doing?"]
show_messages(msgs)

print("_________") # next problem
# 8.10 copy problem from 8-9.
# Make a function call send messages that prints and moves\"sends" to a new list as it is printed.
# Print both once to see if they were transferred correctly
# 8-11 use 8-10 to call a function send_messages with a copy of the messages.
# print both to show if the original list has kept its messages.

def show_messages(msgs):
    print("Showing messages")
    for msg in msgs:
        print(msg)


def send_messages(msgs, sent_msgs):
    print("\nSending messages.")
    while msgs:

        current_msg = msgs.pop()

        print(current_msg)
        sent_msgs.append(current_msg)


msgs = ["How are you?", "Nice to meet you.", "What are you doing?"]
show_messages(msgs)

sent_msgs = []
send_messages(msgs[:], sent_msgs)

print("\nList of moved messages")
print(msgs)
print(sent_msgs)

print("________________")
# 9-1 make a class called Restarant.
# 2 attributes should be stored by the __init__() method: restaurant_name and cuisine_type.
# make a method called describe_restaurant() that prints the attributes' information.
# and a method called open_restaurant() that prints a message that tells if the restaurant is open


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

restaurant = Restaurant('McDonalds', 'Burgers')
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2 call describe_restaurant 3 different times.

DQ = Restaurant('Dairy Queen', 'Ice Cream')
DQ.describe_restaurant()
Jimmy = Restaurant('Jimmys', 'Sandwiches')
Jimmy.describe_restaurant()
SushiPals = Restaurant('Sushi Pals', 'Sushi')
SushiPals.describe_restaurant()
# 9-3 make a class called user create two attributes called first name and last name.
# make a method called describe user that prints a summary of the user's information
# make another method called greet_user that prints a personalized greeting to the user.
# create different user to make different instances of each

class User():

    def __init__(self, first_name,last_name):
        self.login_attempts = 0
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"name: \n{self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"Hello, {self.first_name}")
# add login attempts for the users with a reset function as well that resets the attempts and test this
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

Kostner = User('Kostner','David')
Kostner.describe_user()
Kostner.greet_user()
print("\nlogging in attempt")
Kostner.increment_login_attempts()
Kostner.increment_login_attempts()
print(f"login attempts: {Kostner.login_attempts}")
print("reset login attempts")
Kostner.reset_login_attempts()
print(f" login attempts: {Kostner.login_attempts}")
Josh = User('Josh', 'Smith')
Josh.describe_user()
Josh.greet_user()


# function calls for problem 9-4
print(f"\nNumber served {restaurant.number_served}")
restaurant.number_served = 39
print(f"Number served {restaurant.number_served}")

restaurant.set_number_served(12)
print(f"Number served {restaurant.number_served}")

restaurant.increment_number_served(3284)
print(f"Number served: {restaurant.number_served}")