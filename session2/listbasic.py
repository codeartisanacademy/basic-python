names = ['john', 'jackie']

names.append('budiansyah')
names.insert(1, 'jane')
print(len(names))

print(names.sort(reverse=True))

for name in names:
    print(name.title())
    print("Your name has {x} characters".format(x=len(name)))
    print("Your new email is {name}@gmail.com".format(name=name))

'''
for x in range(1, 10):
    print(x)
'''


# print list of even numbers between 30-50
for x in range(30, 51):
    if x % 2 == 0:
        print(x)


print(names.count('jane'))

print("joko" in names)

print(names[0].title())



