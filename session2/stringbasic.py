first_name = "john doe"
salutation = "Mr"
age = 35


print("{0} {1}".format(salutation, first_name))

print(first_name)

# uppercase, lower

print(first_name.upper())

# title function of string
print(first_name.title())

# concatenate +
print("hello " + first_name.title() + ", how are you?")
# print("my name is " + first_name + " and I'm " + age + " years old")

# format function of string

print("Hello {0} {1}, how are you".format(salutation, first_name.title()))

email = "john@gmail.com"

# is a built-in character that return the total characters in a string
print(len(email))

# find is an object method / function that finds a character and return the position (index) of that finding
print(email.find("@"))

# count, is a function that count occurrences of a character(s)
print(email.count("@"))

# accessing the first letter in the email
print(email[0])

print(email[len(email)-1])
print(email[-1])

print(email[0:3])

password = 'abc'

print(password.isalpha())
