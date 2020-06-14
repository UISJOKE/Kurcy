from random import randint
from datetime import datetime, timedelta

"""Cловарь телефонных кодов Беларуси,России,Украины"""
countries_codes = {'Belarus': '375', 'Russia': '7', 'Ukraine': '380'}

"""Коды операторов связи Беларуси,России,Украины"""
operators_codes = {'Kievstar': '96', 'Vodafone': '95', 'lifecell': '93', 'Beeline': '903', 'Mts_ru': '910',
                   'Megafon': '925', 'Mts_by': '33', 'A1': '29', 'life': '25'}

"""Спрашиваем у пользователя Страну и оператора связи"""
country = input('Belarus,Russia,Ukraine? : ')
operator = input('Mts_by, A1, life, Mts_ru, Beeline, Megafon, Kievstar, Vodafone, lifecell ? : ')
contries_with_operators = {'Belarus': ['Mts_by', 'A1', 'life'], 'Russia': ['Mts_ru', 'Beeline', 'Megafon'],
                           'Ukraine': ['Vodafone', 'Kievstar', 'lifecell']}


def random_number():
    a = ''
    for i in range(0, 7):
        a += str(randint(0, 9))
    return a


def random_phone_number():
    if country in contries_with_operators.keys():
        if operator in operators_codes.keys():
            if operator in contries_with_operators.get(country, []):
                return countries_codes[country] + operators_codes[operator] + random_number()
            else:
                return 'Unknow country in this operator'
        else:
            return 'Unknown operator'
    else:
        return 'Unknown country'


def add_user(name_sonames, mns):
    soname, name = name_sonames.split(' ', 3)
    birth = str(datetime(randint(1950, 2000), randint(1, 12), 1) + timedelta(randint(1, 31)))
    users = {'name': name, 'soname': soname, 'middle_name': '-', 'birth': birth, 'telephone': random_phone_number()}
    if mns == 'yes' or mns == 'да':
        middle_name = input('Enter middle name: ')
        input_middle_name = [middle_name]
        users.update(dict(map(lambda k: {'middle_name': k[0], middle_name: k[1]}, input_middle_name)))
    for i in users.items():
        for j in i:
            if j.isdigit():
                if int(j[6]) > 4:
                    print('sorting completed')
                    return users
                else:
                    return 'sorting completed, unknow number'


name_soname = input('Enter last name and first name: ')
mn = input('Would you like to add a middle name?: ')
print(add_user(name_soname, mn))

