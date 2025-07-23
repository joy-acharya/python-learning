user = {
    'username':'joyacharya',
    'fname':'Joy',
    'lname':'Acharya'
}


for key,value in user.items():
    print(key)
    print(value)

for key in user.keys():
    print(key)


for value in user.values():
    print(value)


# dictionary in list

list = []

for k in range(0,3):
    alien = {'color':'black', 'points':5, 'speed':'slow'}
    list.append(alien)


for alien in list:
    print(alien['color'])
