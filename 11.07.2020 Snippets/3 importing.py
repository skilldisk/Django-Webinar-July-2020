# importing functions or modules from another python file
# use import keyword

import functions

functions.printing()

# if i need to import only perticular function

from functions import adding

adding(2,5)

# to import many function from one file use comma after a module r class name
from functions import adding, add

c = add(6,-3)

