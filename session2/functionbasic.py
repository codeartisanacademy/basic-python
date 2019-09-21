# create a function
def say_hello():
    print("Hello there")


say_hello()


def greet(name):
    print("Hello {0}".format(name.title()))


greet('john')


# function that returns something
def add(x, y):
    return x + y


result = add(3, 6)

print(result)

print(add(8, 10))