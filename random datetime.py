import random
import datetime

"""Cловарь телефонных кодов Беларуси,России,Украины"""
country_code = {'Belarus': '+375', 'Russia': '+7', 'Ukraine': '+380'}

"""Коды операторов связи Беларуси,России,Украины"""
operator_code = {'Kievstar': '96', 'Vodafone': '95', 'lifecell': '93', 'Beeline': '903', 'Mts_ru': '910',
                 'Megafon': '925', 'Mts_by': '33', 'A1': '29', 'life': '25'}

"""Спрашиваем у пользователя Страну и оператора связи"""
country = input('Belarus,Russia,Ukraine? : ')
operator = input('Mts_by, A1, life, Mts_ru, Beeline, Megafon, Kievstar, Vodafone, lifecell ? : ')


def random_date_birth():
    """Функция которая рандомизирует дату рождения"""
    year = random.randint(1950, 2020)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return str(datetime.date(year, month, day))


def random_phone_number():
    """Функция принимает проверяет значения переменных country и operator введенных пользователем и генерирует
    случайный номер телефона с указаными одами стран(country) и кодами операторов(operator) """
    if country == 'Belarus':
        if operator == 'Mts_by' or operator == 'A1' or operator == 'life':
            number = country_code.get(country) + operator_code.get(operator) + str(random.randint(1000000, 9999999))
            return number
        else:
            return 'Неверный оператор'
    if country == 'Russia':
        if operator == 'Mts_ru' or operator == 'Beeline' or operator == 'Megafon':
            number = country_code.get(country) + operator_code.get(operator) + str(random.randint(1000000, 9999999))
            return number
        else:
            return 'Неверный оператор!'
    if country == 'Ukraine':
        if operator == 'Vodafone'or operator == 'Kievstar' or operator == 'lifecell':
            number = country_code.get(country) + operator_code.get(operator) + str(random.randint(1000000, 9999999))
            return number
        else:
            return 'Неверный оператор или страна!'
    else:
        return 'Неверная страна!'

def add():
    for contact in dict_a:
        if contact in dict_a:
            contact.setdefault({'Birth':random_date_birth()})
            contact.setdefault({'Phone':random_phone_number()})
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
