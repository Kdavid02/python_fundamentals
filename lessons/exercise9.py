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


