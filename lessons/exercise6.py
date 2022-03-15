# exercise 6

# 5-3
alien_color = 'green'

if alien_color == 'green':
    print("5 points added.")

alien_color = 'red'

if alien_color == 'green':
    print("Earned 5 points.")

# 5-4
alien_color = 'green'

if alien_color == 'green':
    print("Earned 5 points.")
else:
    print("Earned 10 points.")

alien_color = 'yellow'

if alien_color == 'green':
    print("Earned 5 points.")
else:
    print("Earned 10 points.")

# 5-5

alien_color = 'red'

if alien_color == 'green':
    print("Earned 5 points.")
elif alien_color == 'yellow':
    print("Earned 10 points.")
else:
    print("Earned 15 points.")
    
alien_color = 'green'

if alien_color == 'green':
    print("Earned 5 points.")
elif alien_color == 'yellow':
    print("Earned 10 points.")
else:
    print("Earned 15 points.")
    
    alien_color = 'yellow'
if alien_color == 'green':
    print("Earned 5 points.")
elif alien_color == 'yellow':
    print("Earned 10 points.")
else:
    print("Earned 15 points.")

# 5-6

age = 20

if age < 2:
    print("Baby.")
elif age < 4:
    print("Toddler.")
elif age < 13:
    print("Kid.")
elif age < 20:
    print("Teenager.")
elif age < 65:
    print("Adult.")
else:
    print("Elder.")


def boolfunc(arg1):
    print(bool(arg1))


# true
boolfunc(12)

# true
boolfunc(1.2)

# true
boolfunc(12)

# true
boolfunc(1.2)

# false
boolfunc(0)

# true
boolfunc(0.4)

# false
boolfunc(0.0)
