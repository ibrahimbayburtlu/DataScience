from multiprocessing import Value
from pyexpat import model
from numpy import multiply


def add(*args):
    print(sum(args))

add(2,3,4,5,7,6,7,2,1,3,4,6)


def calculate(n,**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n += kwargs["multiply"]
    print(n)

calculate(2,add = 3 , multiply = 5)


class Car:
    def __init__(self,**kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan",model="Skyline")
print(my_car.model)