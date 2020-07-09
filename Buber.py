from random import randint, choice

users = []
drivers = []
cars = []
current_user = None


class BaseUser:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    @staticmethod
    def get_location():
        location = randint(1, 150)
        return location


class User(BaseUser):
    pass


class Driver(BaseUser):
    pass


class Car:
    def __init__(self, model, number, colour, seat):
        self.model = model
        self.number = number
        self.colour = colour
        self.seat = seat


class Order:
    PRICEFORKM = 0.6
    SPEED = 75

    def __init__(self, driver, user, point):
        user_loc = User.get_location()
        driver_loc = Driver.get_location()
        self.point = point
        self.wait = int(abs(((user_loc - driver_loc) / self.SPEED) * 60))
        self.driver = driver
        self.user = user
        self.price = self.point * self.PRICEFORKM

    def __str__(self):
        return f'User: {self.user}\nDriver: {self.driver}\nWaypoint: {self.point}км.\nCar waiting: {self.wait}мин.\n' \
               f'Price: {int(self.price)}р. '


def signup(name, email, password, user_type):
    global current_user
    if user_type == 'user':
        user = User(name, email, password)
        users.append(user)
    elif user_type == 'driver':
        user = Driver(name, email, password)
        drivers.append(users)
    else:
        return 'Wrong user type!'
    current_user = user
    return 'You has been signed up!'


def login(email, password):
    global current_user
    for user in users:
        if user.email == email:
            if user.password == password:
                current_user = user
                return 'Hello, ' + user.name + '!'
            else:
                return 'Wrong password!'
    return 'Wrong e-mail or password!'


def add_car(model, number, colour, seat):
    car = Car(model, number, colour, seat)
    cars.append(car)
    return 'Car has been add!'


def dell_car(number):
    for car in cars:
        if car.number == number:
            cars.remove(car)
            return 'Car has been removed!'
    return 'Wrong car number!'


while True:
    request = int(input('''1 - Driver signup
2 - Login as driver
3 - User signup
4 - Login as user
5 - add car
6 - delete car
7 - make order
'''))
    if request is 1:
        driver_name = input("Input You'r name: ")
        driver_email = input("Input You'r e-mail: ")
        driver_password = input("Input password: ")
        driver_signup = signup(driver_name, driver_email, driver_password, 'driver')
        print(driver_signup)
        print(User.get_location())
    elif request is 2:
        driver_email = input("Input You'r e-mail: ")
        driver_password = input("Input password: ")
        driver_login = login(driver_email, driver_password)
        print(driver_login)
    elif request is 3:
        user_name = input("Input You'r name: ")
        user_email = input("Input You'r e-mail: ")
        user_password = input("Input password: ")
        user_signup = signup(user_name, user_email, user_password, 'user')
        print(user_signup)
    elif request is 4:
        user_email = input("Input You'r e-mail: ")
        user_password = input("Input password: ")
        user_login = login(user_email, user_password)
        print(user_login)
    elif request is 5:
        car_model = input('Input model: ')
        car_number = input('Input number(xxxxAA-x): ')
        car_colour = input('Input colour: ')
        car_seat = int(input('Input count of seats: '))
        car_add = add_car(car_model, car_number, car_colour, car_seat)
        print(car_add)
        print(cars)
    elif request is 6:
        car_number = input('Input number(xxxxAA-x): ')
        car_del = dell_car(car_number)
        print(car_del)
        print(cars)
    elif request is 7:
        driver = choice(drivers)
        user = current_user
        point = int(input('Input waypoint: '))
        order = Order(driver, user, point)
        print(order)
