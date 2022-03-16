
# 5-8 list 5 or more usernames including admin
# if admin add special message and loop through a list of names as if they were logging into a website.
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

# add new users and check if username is available or it is taken and print the result.

new_users = ['bill', 'steven', 'jack', 'jake', 'rona']
current_users = ['bob', 'steve', 'matthew', 'admin', 'tony']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user}, username is taken.")
    else:
        print(f"{new_user}, username is still available.")