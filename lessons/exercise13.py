# make a seperate file named printing_functions.

import printing_functions as pd



print_begin = ['Logo', 'Text', 'Picture']
done_designs = []

pd.print_designs(print_begin, done_designs)
pd.show_done(done_designs)


# 8-15, 8-16 Import past program and use it. and use the several apporaches listed
import exercise11

from exercise11 import Restaurant

from exercise11 import User as fn

import exercise11 as mn

from exercise11 import *

#9-10 import restaurant from last problems. Already imported from resturant and called statment
#9-11 import classes user privileges and admin as one module and create as seperate file
#9-12 stored modules (priv.py and admin.py) in separate files and tested them

import adminuser as pd

John = Admin('John', 'David')
John.describe_user()


john_privileges = ['add/remove users', 'add/remove passwords', 'can add new content']
John.privileges.privileges = john_privileges
John.privileges.show_privileges()

# 9-16 read about a module on pymotw.com
# I read about pprint a module that is prints data pretty - pretty print.





































