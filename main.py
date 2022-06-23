from car import Car
from account import Account



def run():
    # uberx = Car()
    # uberx.license = 'AJH365'
    # uberx.id = 1017208625
    # uberx.driver = 'Juan Velez'
    # uberx.passanger = 4
    car = Car(1, 'AJG988', Account(123,'Juan Velez','1017208625'))
    print(vars(car))
    print(vars(car.driver))
  
    



if __name__ == '__main__':
    run()