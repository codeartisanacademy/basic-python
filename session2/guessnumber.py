import random

rdn = random.randint(1,10)
print(rdn)
x = input("enter a number: ")

if int(x) == rdn:
    print("Correct")
else:
    print("Wrong")