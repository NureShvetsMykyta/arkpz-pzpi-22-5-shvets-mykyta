#type: ignore

# Поганий приклад
x = 10

# Гарний приклад
item_count = 10


# Поганий приклад
def f():
    pass

# Гарний приклад
def calculate_total():
    pass


# Поганий приклад
class myclass:
pass

# Гарний приклад
class MyClass:
pass


# Гарний приклад
class Example:
    def __init__(self):
    self.public = "Доступний усім"
    self._protected = "Для класу та підкласів"
    self.__private "Тільки для цього класу"


# Поганий приклад
if score > 90:
    print("Excellent!")

# Гарний приклад
EXCELLENT_THRESHOLD = 90
if score > EXCELLENT_THRESHOLD:
    print("Excellent!")


# Поганий приклад
if x > 5:
 y = 10
print(x + y)

# Гарний приклад
if x > 5:
    y = 10
print(x + y)


# Поганий приклад
some_variable = "This is an extremely long string that exceeds seventy-nine characters, which makes it hard to read."

# Гарний приклад
some_variable = (
    "This is an example of breaking a long string "
    "into multiple lines for better readability."
)


# Поганий приклад
result = ( x + y ) * z

# Гарний приклад
result = (x + y) * z


# Поганий приклад
from math import *

# Гарний приклад
from math import sqrt


# Поганий приклад
from models.user import User
import os
from math import sqrt

# Гарний приклад
import os
from math import sqrt

from models.user import User


# Гарний приклад
project/
    main.py
    utils/
        __init__.py
        helpers.py
    models/
        __init__.py
        user.py


# Поганий приклад
if len(data) != 0:
    print("Дані є!")

# Гарний приклад
if data:
    print("Дані є!")


# Поганий приклад
def process(data):
    if data:
        if len(data) > 10:
            for item in data:
                if item > 5:
                    print(item)

# Гарний приклад
def process(data):
    if not data or len(data) <= 10:
        return
    for item in data:
        if item > 5:
            print(item)


# Поганий приклад
def greet(name):
    return "Hello " + name

# Гарний приклад
def greet(name: str) -> str:
    return "Hello " + name


# Поганий приклад
def process_data(data):
    # обробка
    # перевірка
    # форматування

# Гарний приклад
def process_data(data):
    check_data(data)
    format_data(data)


# Поганий приклад
def append_to_list(value, lst=[]):
    lst.append(value)
    return lst

# Гарний приклад
def append_to_list(value, lst=None):
    if lst is None:
        lst = []
    lst.append(value)
    return lst


# Поганий приклад
# Це функція
def func(x):
    return x**2

# Гарний приклад
# Повертає квадрат числа
def calculate_square(number):
    return number ** 2


# Гарний приклад
def calculate_area(radius: float) -> float:
    """
    Обчислює площу круга за заданим радіусом.

    Args:
        radius (float): Радіус круга.

    Returns:
        float: Площа круга.
    """
    return 3.14159 * radius ** 2


# Поганий приклад
global_count = 0

def increment():
    global global_count
    global_count += 1

# Гарний приклад
def increment (count):
    return count + 1


# Поганий приклад
if value == None:

# Гарний приклад
if value is None:


# Поганий приклад
print("Привіт, {}".format(name))

# Гарний приклад
print(f"Привіт, {name}")


# Поганий приклад
data = open("file.txt").read()

# Гарний приклад
try:
    data = open("file.txt").read()
except FileNotFoundError:
    print("File not found")


# Поганий приклад
try:
    result = 10 / 0
except Exception:
    print("Error occurred!")

# Гарний приклад
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")


# Поганий приклад
try:
    value = int(input("Enter a number: "))
except ValueError:
    value = 0 # Контроль логіки через виняток

# Гарний приклад
user_input = input("Enter a number: ")
if user_input.isdigit():
    value = int(user_input)
else:
    value = 0


# Гарний приклад
class CustomError(Exception):
    pass

try:
    raise CustomError("Це власний виняток")
except CustomError as e:
    print(e)


# Поганий приклад
squares = []
for i in range(10):
    squares.append(i ** 2)

# Гарний приклад
squares = [i ** 2 for i in range(10)]


# Поганий приклад
even_numbers = []
for i in range(10):
    if i % 2 == 0:
        even_numbers.append(i)

# Гарний приклад
even_numbers = [i for i in range(10) if i % 2 == 0]
