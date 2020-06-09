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
        if operator == 'Mts_by':
            number = country_code.get(country) + operator_code.get(operator) + str(random.randint(1000000, 9999999))
            return number
        elif operator == 'A1':
            number = country_code.get(country) + operator_code.get(operator) + str(random.randint(1000000, 9999999))
            return number
        elif operator == 'life':
            number = country_code.get(country) + operator_code.get(operator) + str(random.randint(1000000, 9999999))
            return number
        else:
            return 'Неверный оператор или страна!'
    if country == 'Russia':
        if operator == 'Mts_ru':
            number = country_code.get(country) + operator_code.get(operator) + str(random.randint(1000000, 9999999))
            return number
        elif operator == 'Beeline':
            number = country_code.get(country) + operator_code.get(operator) + str(random.randint(1000000, 9999999))
            return number
        elif operator == 'Megafon':
            number = country_code.get(country) + operator_code.get(operator) + str(random.randint(1000000, 9999999))
            return number
        else:
            return 'Неверный оператор или страна!'
    if country == 'Ukraine':
        if operator == 'Vodafone':
            number = country_code.get(country) + operator_code.get(operator) + str(random.randint(1000000, 9999999))
            return number
        elif operator == 'Kievstar':
            number = country_code.get(country) + operator_code.get(operator) + str(random.randint(1000000, 9999999))
            return number
        elif operator == 'lifecell':
            number = country_code.get(country) + operator_code.get(operator) + str(random.randint(1000000, 9999999))
            return number
        else:
            return 'Неверный оператор или страна!'


def request():
    """Функция проверяет наличие человека в словаре dict_a по имени и фамилии"""
    requesting = input('Введите Имя и Фамилию: ')
    for i in dict_a:
        if i == requesting:
            return dict_a.get(requesting)
        elif i != requesting:
            return 'Нет такого человека!'


"""Словарь с данными людей"""
dict_a = {'Станислав Чернявский': {'Дата рождения': random_date_birth(), 'Телефонный номер': random_phone_number()},
          'Василий Пупкин': {'Дата рождения': random_date_birth(), 'Телефонный номер': random_phone_number()},
          'Дмитрий Дятлов': {'Дата рождения': random_date_birth(), 'Телефонный номер': random_phone_number()},
          'Валентин Питонов': {'Дата рождения': random_date_birth(), 'Телефонный номер': random_phone_number()},
          'Владислав Шарпов': {'Дата рождения': random_date_birth(), 'Телефонный номер': random_phone_number()},
          }
"""Выводим данные человека из словаря dict_a в консоль"""
print(request())
