# get a module name "random"
import random

# use the function randint(x,y) from the module random
x = random.randint(1, 10)

print(x)

# if compare for equality
if x == 3:
    print('x is 3')
else:
    print('x is ', x)