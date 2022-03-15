# 4-3 print numbers 1 to 20
numbers = list(range(1, 21))

for number in numbers:
    print(number)

# 4-6 print odd numbers 1 - 20
numbers = list(range(1, 21))

for number in numbers:
    odd = number % 2
    if odd == 1:
        print(number)

# 4-7 list of multiples of 3 from 3 to 0. in a for loop print the numbers of the list.
threes = list(range(3, 31, 3))

for number in threes:
    print(number)


# 4-8 make a list of cubed numbers 1 through 10. and use a for loop to print the values.
cubes = []

for num in range(1, 11):
    cube = num**3
    cubes.append(cube)

for cubed in cubes:
    print(cubed)

