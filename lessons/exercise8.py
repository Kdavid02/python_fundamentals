
# 5-8 list 5 or more usernames including admin
# 5-10 if admin add special message and loop through a list of names as if they were logging into a website.
usrnames = ['bob', 'steve', 'matthew', 'admin', 'tony']

for usrname in usrnames:
    if usrname == 'admin':
        print("Hello admin, special permissions granted")
    else:
        print(f"Hello {usrname}")


# 5-9 if no usernames are present than say 'We need to find some users!'
    usrnames = []

if usrnames:
    for usrname in usrnames:
        if usrname == 'admin':
            print("Hello admin, special permissions granted.")
        else:
            print(f"Hello {usrname}")
    else:
        print("We need to find some users!")

# 5-11 add new users and check if username is available or it is taken and print the result.

new_users = ['bill', 'steven', 'jack', 'jake', 'rona']
current_users = ['bob', 'steve', 'matthew', 'admin', 'tony']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user}, username is taken.")
    else:
        print(f"{new_user}, username is still available.")


# 5-11 Ordinal Numbers. Out put should read 1st 2nd 3rd.... 9th. use loops with a list.
nums = list(range(1,10))

for nums in nums:
    if nums == 1:
        print("1st")
    elif nums == 2:
        print("2nd")
    elif nums == 3:
        print("3rd")
    else:
        print(f"{nums}th")

# 6-1 "Use a dictionary to store information about a person you know" Give first\last name, age and city and print them.

person = {
    'first_nme': 'Kostner',
    'last_nme': 'David',
    'age': 20,
    'city': 'wichita',
    }

print(person['age'])
print(person['city'])
print(person['first_nme'])
print(person['last_nme'])

# Create multiple people's with their data then append it to a dictionary
# Then use a loop to print out their respective age, city and names.
people = []
person = {
    'first_name': 'Kostner',
    'last_name': 'David',
    'age': 20,
    'city': 'wichita',
    }

people.append(person)

person = {
    'first_name': 'Mike',
    'last_name': 'David',
    'age': 70,
    'city': 'wichita',
    }
people.append(person)

person = {
    'first_name': 'John',
    'last_name': 'David',
    'age': 46,
    'city': 'wichita',
    }
people.append(person)

for person in people:
    name = f"{person['first_name']} {person['last_name']}"

    city = person['city']

    age = person['age']


    print(f"{name}, {city}, and is {age} years old.")



