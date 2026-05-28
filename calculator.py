from typing import Union
import math

def add(a, b):
    return a + b


def power(a, b):
    return a ** b

def sqrt(a):
    return math.sqrt(a)

def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b

def divide(a: Union[float, int], b: Union[float, int]) -> float:
    """Return a divided by b. Raise ValueError if b is zero."""
    try:
        return a / b
    except:
        print("Деление на ноль невозможно")


if __name__ == "__main__":
    print(add(2,3), subtract(5,2), multiply(3,4), divide(10,2))