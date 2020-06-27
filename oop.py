from datetime import datetime


class User:
    def __init__(self, nickname, name, surname, telephone):
        self.nickname = nickname
        self.name = name
        self.surname = surname
        self.telephone = telephone


class Ad:
    def __init__(self, ad_name, ad_text, ad_pub_date):
        self.ad_name = ad_name
        self.ad_text = ad_text
        self.ad_pub_date = ad_pub_date


class New_ad(Ad):
    def __init__(self, ad_name, ad_text, ad_pub_date, author):
        super().__init__(ad_name, ad_text, ad_pub_date)
        self.author = author

    def __str__(self):
        return f'Ad has been add:\n{self.ad_name}\n{self.ad_text}\n{self.ad_pub_date}\n{self.author}'


class New_user(User):
    def __init__(self, nickname, name, surname, telephone):
        super().__init__(nickname, name, surname, telephone)

    def __str__(self):
        return f'User has been add:\nnickname: {self.nickname}\nname: {self.name}\nsurname: {self.surname}\n' \
               f'telephone: {self.telephone}\n '


class Admin(User):
    pass


user = New_user(input('Input your nickname: '), input('Input your firstname: '), input('Input you surname: '),
                input('Input your telephone number: '))
print(user)
ad = New_ad(input('Input name ad: '), input('Input ad text: '), datetime.now(tz=None), user.nickname)
print(ad)
