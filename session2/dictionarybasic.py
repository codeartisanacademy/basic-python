

indonesia = {
    'capital': 'Jakarta',
    'language': 'Bahasa Indonesia'
}

print(indonesia['capital'])

indonesia['capital'] = 'Kutai Kartanegara'

for k in indonesia.keys():
    print("{0} is {1}".format(k, indonesia[k]))


for v in indonesia.values():
    print(v)


'''
capital is Jakarta
language is Bahasa Indonesia
'''