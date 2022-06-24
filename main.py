from car import Car
from account import Account
from user import User


def run():
   
    car = Car(1, 'AJG988', Account(123,'Juan Velez','1017208625'))
    print(vars(car))
    print(vars(car.driver))

    user =User(1234, 'Julian Barragan', 101896599, 'jj@gmail.com', 'jjrr899')
    print(vars(user))
  

if __name__ == '__main__':
    run()