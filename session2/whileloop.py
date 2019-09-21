x = 0

while x < 6:
    print(x)
    x = x + 1


countries_total = 0
countries = []

while countries_total < 3:
    country = input("enter a country: ")
    countries.append(country)
    countries_total += 1

for c in countries:
    print(c)