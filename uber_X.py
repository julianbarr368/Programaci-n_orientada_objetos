from tkinter.tix import Form
from turtle import st


from car import Car


class Uberx(Car):
    model = str
    brand = str

    def __init__(self, id, license, driver, brand, model):
        super().__init__(id, license, driver)
        self.brand = brand
        self.model = model
