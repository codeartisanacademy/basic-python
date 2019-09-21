email = 'john@gmail.com'

start = email.find("@")

#print(start)

domain = email[4+1:]

print(domain)

name = email[0:start]

print(name)