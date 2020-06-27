from datetime import datetime
class Users:
    def __init__(self, nickname, name, surname, telephone):
        self.nickname = nickname
        self.name = name
        self.surname = surname
        self.telephone = telephone

class ads:
    def __init__(self, ad_name, ad_text, ad_pub_date):
        self.ad_name = ad_name
        self.ad_text = ad_text
        self.ad_pub_date = ad_pub_date

class new_ad(ads):
    def __init__(self, ad_name, ad_text, ad_pub_date, author):
        super().__init__(ad_name, ad_text, ad_pub_date)
        self.author = author

    def __str__(self):
        return f'Ad has been add:\n{self.ad_name}\n{self.ad_text}\n{self.ad_pub_date}\n{self.author}'



class new_user(Users):
    def __init__(self, nickname, name, surname, telephone):
        super().__init__(nickname, name, surname, telephone)
    def __str__(self):
        return f'User has been add:\nnickname: {self.nickname}\nname: {self.name}\nsurname: {self.surname}\ntelephone: {self.telephone}\n'

user = new_user(input('Input your nickname: '), input('Input your firstname: '), input('Input you surname: '), input('Input your telephone number: '))
print(user)
ad = new_ad(input('Input name ad: '), input('Input ad text: '), datetime.now(tz=None), user.nickname)
print(ad)
