import datetime

bday_str = input('enter your birthday yyyy/mm/dd: ')

bday = datetime.datetime.strptime(bday_str, '%Y/%m/%d')

age = (datetime.datetime.today()-bday).days/365

if age >= 17:
    print('welcome')
else:
    print('need to wait')