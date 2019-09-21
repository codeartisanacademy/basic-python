employees = []
emails = []

name = input('enter the name of the employee: ')

# add the name to the list
if name:
    if name not in employees:
        employees.append(name)
    else:
        print("name already exists")

# print out the list
print(employees)


