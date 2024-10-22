#from typing import Self
"""
#Basic Data Types
names : list = ["Bob", "Anna", "Luigi"]
coordinates: tuple = (1.5, 2.5) # lista której nie można zmienić
unique: set = {1, 4, 2, 9} # to samo co lista ale nie będzie duplikatów
data: dict = {"name": "Bob", "age": 20} # key & value



#Type Annotations
name: str = "Bob"
age: int = 11 # "eleven"
print(age)



#Constant
from typing import Final
VERSION: Final[str] = '1.0.12'
VERSION: "1.1"
PI: Final[float] = 3.1415



#Functions
from datetime import datetime

def show_date() -> None:
    print("This is the current date and time: ")
    print(datetime.now())

show_date()
show_date()

#Class && Initiallisers
class Car:
    def __init__(self, colour: str, horsepower: int) -> None:
        self.colour = colour
        self.horsepower = horsepower

volvo: Car = Car("red", 200) # Class object
print(volvo.colour)
print(volvo.horsepower)

bmw: Car = Car("blue", 240)
print(bmw.colour)
print(bmw.horsepower)



#Methods
class Car:
    def __init__(self, brand: str, horsepower: int) -> None:
        self.brand = brand
        self.horsepower = horsepower

    def drive(self) -> None: # Method
        print(f"{self.brand} is driving")

    def get_info(self, var: int) -> None: # Method
        print(var)
        print(f"{self.brand} with {self.horsepower} horsepower")

    #def get_info(self, var: int) -> None: # Method
    #    print(var) MOŻNA DOŁOŻYĆ INFO ŁATWO TYLKO POTEM WPISUJ CYFRĘ W GET_INFO
    #    print(f"{self.brand} with {self.horsepower} horsepower")

volvo: Car = Car("volvo", 200) # Class object
volvo.drive()
volvo.get_info()

bmw: Car = Car("bmw", 240)
bmw.drive()
bmw.get_info(2)


#Dunder Methods



class Car:
    def __init__(self, brand: str, horsepower: int) -> None:
        self.brand = brand
        self.horsepower = horsepower

    def __str__(self) -> str:
        return f"{self.brand}, {self.horsepower}hp"
    
    #def __add__(self, other: Self) -> str:
    #    return f"{self.brand} & {other.brand}"
    
    def __add__(self, other) -> str:
        return f"{self.brand} & {other.brand}"
    
    #def __mul__(self, other):

volvo: Car = Car("volvo", 200) # Class object
bmw: Car = Car("bmw", 240)
print(volvo + bmw)


#User inputs instead of if-s
def do_this():
    print("Doing this")

def do_that():
    print("Doing that")

match input("Do this or do that? "):
    case "this":
        do_this()
    case "that":
        do_that()
    case _:
        print("Invalid input!")



#Python moves my mouse
#pip install pyautogui

import pyautogui as pag
import keyboard
import random
import time
print("Press N to exit ")
while True:
    if keyboard.is_pressed('n'):
        print("Exiting the program")
        break
    x= random.randint(600,700)
    y= random.randint(200,300)
    pag.moveTo(x,y,0.5)
    time.sleep(3)

"""