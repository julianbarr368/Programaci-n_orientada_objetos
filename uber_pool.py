from car import Car

class Uberpool(Car):
    model = str
    brand = str

    def __init__(self, id, license, driver, model, brand):
        super().__init__(id, license, driver)
        self.brand = brand
        self.model = model