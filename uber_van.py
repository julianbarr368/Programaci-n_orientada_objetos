from car import Car

class Ubervan(Car):
    type_car_accepted = []
    seats_material = []

    def __init__(self, id, license, driver, type_car_accepted, seats_material):
        super().__init__(id, license, driver)
        self.type_car_accepted = type_car_accepted
        self.seats_material = seats_material
        