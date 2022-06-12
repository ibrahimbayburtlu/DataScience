MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
from os import system
from sys import flags
from turtle import Turtle
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# if prompt 'off' loops finish
flag = True
money = 0
while flag:
    control = input("What would you like? (espresso/latte/capuccino):")
    # if to enter off loops finished.
    if control == 'off':
        flag = False
    # if to enter report you shown details.
    elif control == 'report':
        print(f"Water:{resources['water']}ml\nMilk:{resources['milk']}ml\nCoffee:{resources['coffee']}g\nMoney:${money}")
    

