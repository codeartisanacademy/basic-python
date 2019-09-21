countries = []

countries.append('indonesia')
countries.append('malaysia')
countries.append('thailand')

countries.insert(1, 'singapore')

countries.sort(reverse=True)

for c in countries:
    print(c.title())

for c in range(0, len(countries)):
    print(countries[c])