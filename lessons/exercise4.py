# 1
print(5+3)
print(16/2)
print(4*2)
print(12-4)


# 2
# vars to numbers

num1 = 456234
num2 = 68423791
num3 = 137946284
num4 = 96374

# print numbers


def number_sets():
    print(num1)
    print(num2)
    print(num3)
    print(num4)


number_sets()

# Convert int to num, vice versa.


def convert_num(intnum, fltnum):
    print(float(intnum))
    print(int(fltnum))

convert_num(2, 2.9)


def movie_seen():
    mve = input("what is your favorite movie?")
    seen = int(input("How many times have you seen it?"))
    print(f"I have seen {mve} {seen} times.")


movie_seen()


