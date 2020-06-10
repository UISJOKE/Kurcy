import random
import datetime

"""Cловарь телефонных кодов Беларуси,России,Украины"""
countries_codes = {'Belarus': '+375', 'Russia': '+7', 'Ukraine': '+380'}

"""Коды операторов связи Беларуси,России,Украины"""
operators_codes = {'Kievstar': '96', 'Vodafone': '95', 'lifecell': '93', 'Beeline': '903', 'Mts_ru': '910',
                 'Megafon': '925', 'Mts_by': '33', 'A1': '29', 'life': '25'}

"""Спрашиваем у пользователя Страну и оператора связи"""
country = input('Belarus,Russia,Ukraine? : ')
operator = input('Mts_by, A1, life, Mts_ru, Beeline, Megafon, Kievstar, Vodafone, lifecell ? : ')
contries_with_operators = {'Belarus': ['Mts_by', 'A1', 'life'], 'Russia': ['Mts_ru', 'Beeline', 'Megafon'], 'Ukraine': ['Vodafone', 'Kievstar', 'lifecell']}


def random_date_birth():
    """Функция которая рандомизирует дату рождения"""
    year = random.randint(1950, 2020)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return str(datetime.date(year, month, day))


def random_phone_number():
    if country in contries_with_operators.keys():
        if operator in operators_codes.keys():
            if operator in contries_with_operators.get(country, []):
                return countries_codes[country] + operators_codes[operator] + str(random.randint(1000000, 9999999))
            else:
                return 'Unknow country in this operator'
        else:
            return 'Unknown operator'
    else:
        return 'Unknown country'

def add():
    for contact in dict_a:
        if contact in dict_a:
            contact.update({'Birth': random_date_birth()})
            contact.update({'Phone': random_phone_number()})
            return contact



def request():
    """Функция проверяет наличие человека в словаре dict_a по имени и фамилии"""
    name = input('Введите Имя и Фамилию: ')
    for contact in dict_a:
        if contact['Name'] == name:
            contact.update({'Birth': random_date_birth()})
            contact.update({'Phone':random_phone_number()})
            print(contact['Name'], contact['Birth'], contact['Phone'])


"""Словарь с данными людей"""
dict_a = [{'Name': 'Станислав Чернявский'},
          {'Name': 'Василий Пупкин'},
          {'Name': 'Владислав Питонов'},
          {'Name': 'Андрей Шарпов'},
          {'Name': 'Станислав Чернявский'},
          ]
"""Выводим данные человека из словаря dict_a в консоль"""
request()
