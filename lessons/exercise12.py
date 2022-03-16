# 10-6 make a simple calculator that adds 2 numbers and exits if input is not a number using a try block.
# 10-7 wrap code in a while loop so the user can keep inputing numbers
while True:
    try:
        x = input("enter 1st number-")
        x = int(x)

        y = input("enter 2nd number- ")
        y = int(y)

    except ValueError:
        print("error, not a number.")
    else:

        xy_sum = x + y
        print(f"sum of {x} and {y} is {xy_sum}.")
        break

# 10-8 Make 2 files and store at least 3 names of each.
# write a program that tries to read these files and print the contents of the file to the screnn
# wrap code in a try-expect block to catch the FileNotFound error
# move file to another place in the system, to see if expect blocks executes properly.
# 10-9 modify your exept block in exercise to fail silently if either file is missing
filnms = ['cats.txt', 'dogs.txt']

for filnm in filnms:

    try:
        with open(filnm) as f:
            contents = f.read()


    except FileNotFoundError:
        pass
    else:
        print(f"\nFile Output {filnm}")
        print(contents)